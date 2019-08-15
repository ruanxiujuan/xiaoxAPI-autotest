import unittest
from ddt import ddt, data, unpack
from common.login import *
from data_file import default_data
from case.school_notice.notice import get_school_by_countryId


@ddt
class TestGetSchoolByCountryId(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

    @unpack
    @data(
        (12, 0),  # 澳洲-全部
        (20, 0),   # 英国-全部
        (11, 0),
        (13, 0),
        (10, 0),
        (3, 0),
        (1, 0),
        (12, 1),  # 澳洲-资源系统国家
        (20, 1),
        (11, 1),
        (13, 1),
        (10, 1),
        (3, 1),
        (1, 1)
    )
    def test_get_school_ty_countryId(self,countryId,type):
        result = get_school_by_countryId(self.s, self.uri, self.platform, self.token, self.memberId, countryId, type)[0]

        try:
            if result:
                self.assertIsNotNone(result)
                print("国家对应的院校列表为：", json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        except Exception as e:
            print(e)


if __name__ == "__name__":
    unittest.main()



