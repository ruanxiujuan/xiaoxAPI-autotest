import unittest
from common.login import *
from data_file import default_data
from common.resource_country import resource_country_list
from case.school_notice.notice import search_school_notice, school_notice_detail


class TestSchoolNoticeDetail(unittest.TestCase):
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
        cls.noticeId = search_school_notice(cls.s, cls.uri, cls.platform, cls.token, cls.memberId, cls.countryId, "")[1]

    def test_school_notice_detail(self):
        school_notice_detail(self.s, self.uri, self.platform, self.token, self.memberId, self.noticeId)


if __name__ == "__main__":
    unittest.main()



