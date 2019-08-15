import unittest
import requests
from ddt import ddt, data
from common.login import login
from data_file import default_data
from case.students.student import test_student_list_status_0
from case.call.call import *


@ddt
class TestAxOnLinceCall(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberid = aa['body']['memberid']

        studentInfo = test_student_list_status_0(cls.s, cls.uri, cls.token, cls.memberid, cls.platform)
        cls.resourceId = studentInfo[0]

        cls.callNumber = get_res_ext_info(cls.s, cls.uri, cls.token, cls.memberid, cls.platform, cls.resourceId, 0)

    @data(0, 1, 2)
    # data中的入参为资源来源 0:资源线索的回访 1:为名片的回访 2:根资源的回访
    def test_ax_onlince_call(self, source):
        ax_onlince_call(self.s, self.uri, self.token, self.memberid, self.platform, self.resourceId, self.callNumber, source)


if __name__ == "__main__":
    unittest.main()






