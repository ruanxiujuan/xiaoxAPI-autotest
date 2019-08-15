import unittest, requests
from common.login import *
from data_file import default_data
from source.resource import carts


class TestCarts(unittest.TestCase):
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


    def test_carts(self):
        '''
        测试添加资源接口
        :param resourceType:
        :return:
        '''
        list = carts(self.s, self.uri, self.vcode, self.platform, self.token, self.memberId)

        try:
            if list:
                self.assertIsNotNone(list)
                print("名片列表信息为：", json.dumps(list, ensure_ascii=False, sort_keys=True, indent=2))
            else:
                print("获取名片列表失败！")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()
