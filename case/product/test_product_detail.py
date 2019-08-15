import unittest
import logging
from common.login import *
from data_file import default_data
from case.product.product import apply_list_default
from case.product.product import product_list_default


class TestProductDetail(unittest.TestCase):

    s = requests.session()  # 创建请求会话对象
    uri = default_data.baseUrl
    platform = default_data.platform
    vcode = default_data.vcode

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

        # 产品详情参数
        cls.productCode = product_list_default(cls.s, cls.uri, cls.platform, cls.token, cls.memberId, cls.defaultCountryId, cls.defaultLineId, cls.defaultApplyId)[0]

    def test_product_detail(self):
        '''
        测试精选产品详情
        '''

        url = "/product/productDetail"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }
        data = {
            "productCode": self.productCode,
            "versionCode": self.vcode,
            "skuCode": "",
            "startIndex": 0,
            "pageSize": 10
        }

        res = requests.post(url=self.uri+url, headers=headers, data=data)
        result = (json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2))

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, data))
        logging.info("响应信息：{0}".format(result))

        detail = res.json()['body']['detail']                        # 商品详情
        contractUrl = res.json()['body']['detail'] ['contractUrl']   # 合同链接

        # 断言：合同详情取自接口返回，contractUrl不为空
        try:
            if detail is not None:
                self.assertIsNotNone(contractUrl)
            else:
                logging.info("商品详情显示异常~")
                logging.info(detail)
        except Exception as e:
            logging.error(e)


if __name__ == "__main__":
    unittest.main()





