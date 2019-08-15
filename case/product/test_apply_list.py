import unittest
import logging
from common.login import *
from data_file import default_data


class TestProductApplyList(unittest.TestCase):

    s = requests.session()  # 创建请求会话对象
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)  # 实例化登录对象
        aa = cls.a.outside_consultants_login(cls.uri)  # 调用外部顾问登录方法并返回用户数据
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

    def test_product_apply_list_default(self):
        '''
        测试精选产品 - 筛选接口
        :return: 默认国家、产品线、服务
        '''

        url = "/product/applyListV214"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }

        res = requests.post(url=self.uri+url, headers=headers)
        result = (json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2))

        logging.info("请求信息：{0}{1}".format(self.uri+url, headers))
        logging.info("响应信息：{0}".format(result))

        # 断言：默认国家、产品线、服务为“澳洲(65)+留学(1)+全程服务(1)
        defaultCountryId = jsonpath.jsonpath(res.json(), "$.body.defaultCountryId[0]") # 默认国家id
        defaultLineId = jsonpath.jsonpath(res.json(), "$.body.defaultLineId[0]")  # 默认产品线id
        defaultApplyId = jsonpath.jsonpath(res.json(), "$.body.defaultApplyId[0]")  # 默认服务id
        try:
            self.assertEqual([65], defaultCountryId)
            self.assertEqual([1], defaultLineId)
            self.assertEqual([1], defaultApplyId)
        except Exception as e:
            logging.error(e)


if __name__ == "__main__":
    unittest.main()





