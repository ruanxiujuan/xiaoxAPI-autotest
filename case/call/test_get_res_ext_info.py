import unittest
import requests
from ddt import ddt, data
from common.login import login
from data_file import default_data
from case.students.student import test_student_list_status_0
from case.call.call import get_res_ext_info


@ddt
class TestGetResExtInfo(unittest.TestCase):
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

    @data(0, 1, 2, 3)
    # data中的入参为资源类型(0:销售线索；1:名片；2:根资源,3:签约),遍历所有资源类型进行测试
    def test_get_res_ext_info(self, sourceType):
        get_res_ext_info(self.s, self.uri, self.token, self.memberid, self.platform, self.resourceId, sourceType)


if __name__ == "__main__":
    unittest.main()






