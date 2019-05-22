"""结算平台接口"""
import json

from app.utils.http_request import Http
from app.utils.common import load_const
from app.utils.log import log_action

class Settle(Http):
    """结算平台相关接口"""
    def __init__(self):
        super(Settle, self).__init__()
        self.headers = None
        self.url = load_const("settle", "url.yaml")
        self.line_type_list_cache = {}
        self.doc_type_list_cache = None
        self.doc_type_data = {}
        self.logger_data_cache = None

    def login(self, username: str, password: str) -> bool:
        """
        登录
        :param username: 用户名
        :param password: 密码
        :returns
        """
        self.logger.info("登录结算平台")
        res = self.post(self.url.get("LOGIN_URL"), data={"userName": username, "pwd": password})
        if not res:
            return False

        try:
            assert res.json().get("msg").get("context") == "成功"
            assert res.cookies["tokenKey"] is not None
        except (json.decoder.JSONDecodeError, AssertionError):
            self.logger.error(res.text)
            return False
        else:
            self.headers = {"tokenKey": res.cookies["tokenKey"]}
            self.logger.info("登录成功")
            return True

    def http_get(self, url_name, params=None, data=None, index=None):
        url = self.url.get(url_name, None)
        if url is not None:
            res_dict = self.json_get(url, headers=self.headers, params=params)
            if res_dict is not None and isinstance(res_dict, dict):
                data_list = res_dict.get("data", {}).get("data", [])
                if index is not None:
                    if index < len(data_list):  # TODO index is number
                        return data_list[index]
                else:
                    return data_list

    def http_post(self, url_name, params=None, data=None, index=None):
        url = self.url.get(url_name, None)
        if url is not None:
            res_dict = self.json_get(url, headers=self.headers, params=params, data=data)
            if res_dict is not None and isinstance(res_dict, dict):
                data_list = res_dict.get("data", {}).get("data", [])
                if index:
                    if index < len(data_list):  # TODO index is number
                        return data_list[index]
                else:
                    return data_list

    @log_action(verbosity=2)
    def get_doc_type_data(self, doc_type_code=None, doc_type_name=None):
        """获取结算单类型对应的编码"""
        if self.doc_type_list_cache is not None:
            doc_type_list = self.doc_type_list_cache
        else:
            self.doc_type_list_cache = doc_type_list = self.http_get("GET_ALL_DOC_TYPE_URL")

        if doc_type_code is not None:
            result = [item for item in doc_type_list if item.get("value") == doc_type_code]
        elif doc_type_name is not None:
            result = [item for item in doc_type_list if item.get("label") == doc_type_name]
        else:
            raise ValueError("doc_type_code和doc_type_name不能都为空")
        return result[0] if result else None

    @log_action(verbosity=2)
    def query_head(self, header_id) -> list:
        """获取订单数据
        :param header_id: 结算单id
        """
        params = {
            "currentPage": 1,
            "pageSize": 10,
            "id": header_id
        }
        return self.http_get("GET_LEDGER_DATA_URL", params=params, index=0)

    @log_action(verbosity=2)
    def query_able_write_off(self, segment1, currency_code, supplier_code_self, direction):
        """
        获取可核销预付款结算单
        :param segment1:
        :param currency_code:
        :param supplier_code_self:
        :param direction:
        :return:
        """
        params = {
            "segment1": segment1,
            "currencyCode": currency_code,
            "supplierCodeSelf": supplier_code_self,
            "direction": direction
        }
        return self.http_get("GET_ABLE_WRITE_OFF", params=params)


    @log_action(verbosity=2)
    def get_supplier_info(self, segment1, supplier_name, supplier_code=""):
        params = {
            "segment1": segment1,
            "type": 1,
            "supplierName": supplier_name,
            "supplierCode": supplier_code
        }
        supplier_list = self.http_get("GET_SUPPLIER_URL", params=params)
        if supplier_code:
            supplier_list = [supplier_data for supplier_data in supplier_list
                             if supplier_data.get("supplierCode") == supplier_code]
        return supplier_list[0] if supplier_list else None

    @log_action(verbosity=2)
    def get_line_type(self, segment1, doc_type_code, line_type_code):
        cache_key = "{}{}".format(segment1, doc_type_code)
        if cache_key in self.line_type_list_cache:
            return self.line_type_list_cache[cache_key]
        else:
            params = {
                "segment1": segment1,
                "settleTypeCode": doc_type_code
            }
            line_type_list = self.http_get("GET_LINE_TYPE_URL", params=params)
            result = [line_type for line_type in line_type_list
                      if line_type.get("value") == line_type_code]
            if result and isinstance(result, list):
                self.line_type_list_cache[cache_key] = result[0]
            return result[0]

    @log_action(verbosity=2)
    def query_line(self, write_off_header_id):
        params = {"id": write_off_header_id}
        return self.http_get("GET_LINE_DATA_URL", params=params, index=0)

    @log_action(verbosity=2)
    def get_deposit_list(self, header_id):
        params = {"headerId": header_id}
        return self.http_get("GET_DEPOSIT_URL", params=params)

    @log_action(verbosity=2)
    def get_invoice_list(self, header_id):
        params = {"id": header_id}
        return self.http_get("GET_INVOICE_URL", params=params)

    @log_action(verbosity=2)
    def find_settlement_by_header_id(self, header_id):
        params = {"headerId": header_id}
        return self.http_get("GET_SETTLEMENT_URL", params=params)

    @log_action(verbosity=2)
    def find_pay_plan_by_header_id(self, header_id):
        params = {"headerId": header_id}
        return self.http_get("GET_PAY_PLAN_URL", params=params)

    @log_action(verbosity=2)
    def find_bank_by_header_id(self, header_id):
        params = {"headerId": header_id}
        return self.http_get("GET_BANK_URL", params=params)

    @log_action(verbosity=2)
    def find_match_transaction_by_head(self, header_id):
        data = {"pageNumber": 1, "pageSize": 1, "settlementHeaderId": header_id}
        res_dict = self.json_post(url=self.url.get("FIND_TRANSACTION_URL"), json=data, headers=self.headers)
        return res_dict.get('data', {}).get('datas', []) if res_dict and isinstance(res_dict, dict) else []


    @log_action(verbosity=2)
    def modify_settlement(self, params, data):
        """
        修改结算单核销金额
        :param params: 请求参数
        :param data: 请求体
        :return:
        """
        res_dict = self.json_post(url=self.url.get("MODIFY_SETTLEMENT_URL"),
                                  params=params, json=data, headers=self.headers)
        res_data = res_dict.get("data", {}) if res_dict and isinstance(res_dict, dict) else {}
        return res_data.get("success"), res_data.get("message")

    def get_header_id(self, apply_number):
        ledger_data = self.query_head(apply_number)
        return ledger_data.get("id", None) if ledger_data and isinstance(ledger_data, dict) else None

    def pack_line_list(self, header_id, segment1, doc_type_code):
        """将line_type数据放入line_data"""
        line_data = self.query_line(header_id)
        if not line_data or not isinstance(line_data, dict):
            raise ValueError("结算单数据为空")
        line_data = {key: value for key,value in line_data.items() if key is not None}  # 去除None字段
        line_type_code = line_data.get("lineTypeCode")
        line_type = self.get_line_type(segment1, doc_type_code, line_type_code)
        line_data["lineType"] = line_type
        return [line_data]

    def get_bail_list(self, header_id):
        return []

if __name__ == "__main__":
    s = Settle()
    s.login("zhangxin", "123456")
    print(s.get_header_id("100120190300003"))
