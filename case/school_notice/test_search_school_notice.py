import unittest, requests
from ddt import ddt, data
from common.login import *
from data_file import default_data
from common.resource_country import resource_country_list
from case.school_notice.notice import search_school_notice


@ddt
class TestSearchSchoolNotice(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

        cls.countryId = resource_country_list(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)[0][1]

    @data("", "澳大利亚", "ceshi", 123)
    def test_search_school_notice(self, keyword):
        '''
        测试院校通知搜索:
        1. 测试不输入关键字搜索的院校通知
        2. 测试输入关键字进行搜索的院校通知（搜索关键字包含：数字、英文、汉字）
        :param keyword:
        :return: 相应院校通知信息
        '''
        result = search_school_notice(self.s, self.uri, self.platform, self.token, self.memberId, self.countryId, keyword)[0]

        try:
            if result:
                print("院校通知搜索结果为：", json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
                self.assertIsNotNone(result)
            else:
                print("搜索结果为空")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()



