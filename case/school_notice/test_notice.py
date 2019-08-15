import unittest
from common.login import *
from data_file import default_data
from case.school_notice.notice import *


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

        cls.countryId = 12

    def test_notice(self):
        # 保存国家为澳洲
        member_save_country(self.s, self.uri, self.platform, self.token, self.memberId, self.countryId)

        schoolId = get_school_by_countryId(self.s, self.uri, self.platform, self.token, self.memberId, self.countryId, type=0)[1][0]

        # 选中学校搜索
        noticeId = search_school_notice(self.s, self.uri, self.platform, self.token, self.memberId, self.countryId, schoolId=schoolId,
                             keyword="", )[1][0]

        # 查询院校通知详情
        school_notice_detail(self.s, self.uri, self.platform, self.token, self.memberId, noticeId)


if __name__ == "__main__":
    unittest.main()



