import unittest, requests
from ddt import ddt, data
from common.login import *
from data_file import default_data
from source.resource import add_resource
from common.resource_country import resource_country_list


@ddt
class TestAddResource(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform
    vcode = default_data.vcode

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

        cls.countryId = resource_country_list(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)[0][1]

    @data(0, 1)
    def test_add_resource(self, resourceType):
        '''
        测试添加资源接口
        :param resourceType:
        :return:
        '''
        result = add_resource(self.s, self.uri, self.vcode, self.platform, self.token, self.memberId, resourceType, self.countryId)
        code = result[0]
        message = result[1]

        try:
            if code == 0:
                print("资源录入成功！")
            else:
                print("资源录入失败", code, message)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()
