import unittest
from common.login import *
from data_file import default_data
import logging
from common.resource_country import resource_country_list
from school import member_save_country


class TestSchoolMajorQs(unittest.TestCase):

    s = requests.session()     # 创建请求会话对象
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)   # 实例化登录对象
        aa = cls.a.outside_consultants_login(cls.uri)   # 调用外部顾问登录方法并返回用户数据
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

        # 调用国家列表接口获取国家id
        countryInfo = resource_country_list(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)
        countryIds = countryInfo[0]
        countryId = countryIds[1]  # 澳洲

        # 调用用户保存国家接口获取国家id
        cls.countryId = member_save_country(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, countryId)

    def test_school_major_qs(self):
        '''
        测试热门院校接口
        '''
        url = "/school/majorQs/v2.6"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId,
        }

        res = requests.get(url=self.uri+url, headers=headers)

        logging.info("请求信息为：{0}{1}".format(self.uri + url, headers))
        logging.info("响应信息为：{}".format(res.json()))

        # 断言：检查QS排名
        majorQsResponseList = res.json()['body']['majorQsResponseList']
        try:
            if majorQsResponseList:
                self.assertIsNotNone(majorQsResponseList)
                logging.info("QS专业排名为:", majorQsResponseList)
            else:
                logging.info("QS专业排名无数据")
        except Exception as e:
            logging.info(e)


if __name__ == "__main__":
    unittest.main()










