import unittest, requests, json
from common.login import *
from data_file import default_data
from case.students.student import get_invitations, test_student_list_status_0


class TestGetInvitations(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

        inviterInfo = test_student_list_status_0(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)
        cls.resourceId = inviterInfo[0]

    def test_get_invitations(self):
        '''
        测试邀约来访列表接口
        :return: 判断是否获取邀约来访列表成功，并返回信息
        '''
        list = get_invitations(self.s, self.uri, self.token, self.memberId, self.platform, self.resourceId)

        try:
            if list:
                self.assertIsNotNone(list)
                print("邀约来访列表为：", json.dumps(list, ensure_ascii=False, sort_keys=True, indent=2))
            else:
                print("获取邀约来访列表失败！")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()

