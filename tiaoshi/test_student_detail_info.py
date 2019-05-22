import unittest
import requests
import json
from .login import *
from . import test
from data import data


class TestStudentDetailInfo(unittest.TestCase):

    s = requests.session()
    platform = data.platform
    uri = data.baseUrl

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login_normal(cls.uri)
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']
        a = test.test_student_list_status_0(cls.s, cls.token, cls.memberId, cls.platform, "autotest77", cls.uri)
        cls.resourceId = jsonpath.jsonpath(a.json(), "$.body.list[*].resourceId")
        print(cls.resourceId)


    def test_student_detail_info_type1(self):
            url = "/counselor/Student/detailInfo"
            headers = {
                "token": self.token,
                "memberId": self.memberId,
                "platform": self.platform
            }
            data = {
                "resourceId": self.resourceId[0],
                "type": "1"    # 资源类别 1资源阶段，2潜在阶段，3已签约(待定校、待申请、待签证、结案)
            }
            response = requests.post(url=self.uri+url, headers=headers, data=data)
            # print(json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))
            detail = json.dumps(response.json()['body']['detail'], ensure_ascii=False, sort_keys=True, indent=2)
            # print(detail)

            # 断言：学生详情信息，增加咨询顾问手机号、文签手机号
            if detail is not None:
                try:
                    self.assertIn("customermobile", detail)
                    self.assertIn("visaTel", detail)
                except AssertionError as msg:
                    print(msg)

    def test_student_detail_info_type2(self):
        url = "/counselor/Student/detailInfo"
        headers = {
            "token": self.token,
            "memberId": self.memberId,
            "platform": self.platform
        }
        data = {
            "resourceId": self.resourceId,
            "type": "2"    # 资源类别 1资源阶段，2潜在阶段，3已签约(待定校、待申请、待签证、结案)
        }
        response = requests.post(url=self.uri+url, headers=headers, data=data)
        # print(json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))
        detail = json.dumps(response.json()['body']['detail'], ensure_ascii=False, sort_keys=True, indent=2)
        # print(detail)

        # 断言：学生详情信息，增加咨询顾问手机号、文签手机号
        if detail is not None:
            try:
                self.assertIn("customermobile", detail)
                self.assertIn("visaTel", detail)
            except AssertionError as msg:
                print(msg)

    def test_student_detail_info_type3(self):
        url = "/counselor/Student/detailInfo"
        headers = {
            "token": self.token,
            "memberId": self.memberId,
            "platform": self.platform
        }
        data = {
            "resourceId": self.resourceId,
            "type": "3"    # 资源类别 1资源阶段，2潜在阶段，3已签约(待定校、待申请、待签证、结案)
        }
        response = requests.post(url=self.uri+url, headers=headers, data=data)
        # print(json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))
        detail = json.dumps(response.json()['body']['detail'], ensure_ascii=False, sort_keys=True, indent=2)
        # print(detail)

        # 断言：学生详情信息，增加咨询顾问手机号、文签手机号
        if detail is not None:
            try:
                self.assertIn("customermobile", detail)
                self.assertIn("visaTel", detail)
            except AssertionError as msg:
                print(msg)


if __name__ == "__main__":
    unittest.main()