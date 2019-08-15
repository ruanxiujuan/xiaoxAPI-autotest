import unittest
import logging
from common.login import *
from data_file import default_data
from case.product.product import apply_list_default


class TestProductProductDefaultList(unittest.TestCase):

    s = requests.session()  # 创建请求会话对象
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)  # 实例化登录对象
        aa = cls.a.outside_consultants_login(cls.uri)  # 调用外部顾问登录方法并返回用户数据
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

        # 精选产品默认筛选项
        select_info = apply_list_default(cls.s, cls.uri, cls.platform, cls.token, cls.memberId)
        cls.defaultCountryId = select_info[0][0]
        cls.defaultLineId = select_info[1][0]
        cls.defaultApplyId = select_info[2][0]

    def test_product_list_default(self):
        '''
        测试精选产品 - 精选产品列表
        :return: 默认国家、产品线、服务
        '''

        url = "/product/productListv214"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }
        data = {
            "countryIds": self.defaultCountryId,
            "lineId": self.defaultLineId,
            "applyIds": self.defaultApplyId,
            "startIndex": 0,
            "pageSize": 10
        }

        res = requests.post(url=self.uri+url, headers=headers, data=data)
        result = (json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2))

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, data))
        logging.info("响应信息：{0}".format(result))

        productCode = jsonpath.jsonpath(res.json(), "$.body.list[*].productCode")
        return productCode


if __name__ == "__main__":
    unittest.main()





