import unittest
import requests
import json
import jsonpath
from lib.login import login
from students.student import test_student_add_resource
from data import data


class TestStudentList(unittest.TestCase):
    s = requests.session()
    uri = data.baseUrl
    platform = data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']
        cls.studentName = test_student_add_resource(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)

    def test_student_list_status_0(self):   # 查询全部学生列表指定学生信息，并返回资源id
        url = "/counselor/studentsV274"
        headers = {
            "token": self.token,
            "memberId": self.memberId,
            "platform": self.platform
        }
        data = {
            "studentName": self.studentName,
            "status": "0",       # 全部列表
            "startIndex": "0",
            "pageSize": "50"
        }
        response = requests.post(url=self.uri+url, headers=headers, data=data)
        result = json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2)

        print("请求信息：", url, headers, data)
        print("响应信息：", result)




if __name__ == "__main__":
    unittest.main()