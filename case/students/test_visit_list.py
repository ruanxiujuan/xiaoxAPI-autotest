import unittest, requests
from ddt import ddt, data, unpack
from common.login import *
from data_file import default_data
from case.students.student import visit_list, test_student_list_status_0


@ddt
class TestVisitList(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform

    remark = "自动化添加回访测试啦！"

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

        cls.resourceId = test_student_list_status_0(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)[0][0]

    @data(1, 2, 3)
    # type资源类别: 1资源阶段，2潜在阶段，3已签约
    def test_visit_list(self, type):
        visit_list(self.s, self.uri, self.token, self.memberId, self.platform, self.resourceId, type)


if __name__ == "__main__":
    unittest.main()