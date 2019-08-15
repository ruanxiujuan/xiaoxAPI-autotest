import unittest
from ddt import ddt, data
from common.login import *
from data_file import default_data
from case.school_notice.notice import member_save_country


@ddt
class TestMemberSaveCountry(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

    @data(12, 20, 11, 13, 10, 3, 1)
    def test_member_save_country(self, countryId):
        '''
        测试院校通知选择国家并保存接口
        :param countryId:
        :return: 遍历所有国家选项，并返回国家ID
        '''
        result = member_save_country(self.s, self.uri, self.platform, self.token, self.memberId, countryId)

        try:
            if result:
                self.assertIsNotNone(result)
                print("选中国家ID为", result)
        except Exception as e:
            print(e)
        else:
            print("保存国家成功！")


if __name__ == "__main__":
    unittest.main()


