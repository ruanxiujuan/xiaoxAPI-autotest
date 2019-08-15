import unittest
from common.login import *
from data_file import default_data
from common.resource_country import resource_country_list


class TestMemberSaveCountry(unittest.TestCase):

    s = requests.session()     # 创建请求会话对象
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)   # 实例化登录对象
        aa = cls.a.outside_consultants_login(cls.uri)   # 调用外部顾问登录方法并返回用户数据
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

        cls.countryInfo = resource_country_list(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)
        cls.countryIds = cls.countryInfo[0]
        cls.countryId = cls.countryIds[1]  # 澳洲

    def test_member_save_country(self):
        '''
        测试用户保存国家接口
        '''

        url = "/member/saveCountry"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }

        data = {
            "countryId": self.countryId
        }

        res = requests.post(url=self.uri+url, headers=headers, data=data)

        print("请求信息为：{0}{1}{2}".format(self.uri + url, headers, data))
        print("响应信息为：{}".format(res.json()))

        code = res.json()['body']['code']
        message = res.json()['body']['message']
        try:
            self.assertEqual(0, code)
            self.assertEqual('操作成功', message)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()










