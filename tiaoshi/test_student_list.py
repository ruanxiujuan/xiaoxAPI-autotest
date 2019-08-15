import unittest
import requests
import json

from .login import *
from data_file import default_data


class TestStudentList(unittest.TestCase):

    s = requests.session()
    platform = default_data.platform
    uri = default_data.baseUrl

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login_normal(cls.uri)
        token = aa['body']['token']
        memberid = aa['body']['memberid']

        countryAll = cls.a.test_get_resource_country_list(cls.uri, token, memberid, cls.platform)
        countryId = countryAll[0]

        cls.info = cls.a.test_student_add_resource(cls.uri, token, memberid, cls.platform, countryId)
        print(cls.info)

        cls.studentName = cls.info[0]
        print(cls.studentName)
        cls.token = cls.info[1]
        print(cls.token)
        cls.memberId = cls.info[2]
        cls.platform = cls.info[3]

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

        resourceId = jsonpath.jsonpath(response.json(), "$.body.list[*].resourceId")

        return resourceId


if __name__ == "__main__":
    unittest.main()