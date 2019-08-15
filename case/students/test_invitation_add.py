import unittest, requests, json
from common.login import *
from data_file import default_data
from case.students.student import invitation_add, test_student_list_status_0


class TestInvitationAdd(unittest.TestCase):
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
        cls.visitor = inviterInfo[1]
        cls.receiver = cls.memberId

    def test_invitation_add(self):
        '''
        测试邀约来访接口
        :return: 判断是否添加回访成功，并返回信息
        '''
        visitId = invitation_add(self.s, self.uri, self.token, self.memberId, self.platform, self.resourceId, self.visitor, self.receiver)

        try:
            if visitId:
                self.assertIsNotNone(visitId)
                print("添加邀约来访成功！id为：", visitId)
            else:
                print("添加邀约来访失败！")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()

