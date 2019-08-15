import unittest
from common.login import *
from data_file import default_data
import logging
from common.resource_country import resource_country_list
from school import member_save_country


class TestSchoolHot(unittest.TestCase):

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

    def test_school_hot(self):
        '''
        测试热门院校接口
        '''
        url = "/school/hot"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId,
            "countryId": str(self.countryId)
        }

        params = {
            "startIndex": "0",
            "pageSize": "10"
        }

        res = requests.get(url=self.uri+url, headers=headers, params=params)

        logging.info("请求信息为：{0}{1}{2}".format(self.uri + url, headers, params))
        logging.info("响应信息为：{}".format(res.json()))

        # 断言：获取热门院校信息并判断是否存在，存在则打印
        hotList = res.json()['body']['hotList']
        try:
            if hotList:
                logging.info("热门院校信息~")
                for i in hotList:
                    logging.info(i)
            else:
                logging.info("无热门院校信息")
        except Exception as e:
            logging.error(e)


if __name__ == "__main__":
    unittest.main()










