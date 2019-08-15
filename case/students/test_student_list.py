import unittest
import requests
import json
from common.login import login
from students.student import test_student_add_resource
from data_file import default_data
import logging


class TestStudentList(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']
        cls.studentName = test_student_add_resource(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)

    def test_student_list_status_0(self):
        '''
        全部学生列表接口
        :return: 顾问全部学生信息
        '''
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
            "pageSize": "10"
        }
        response = requests.post(url=self.uri+url, headers=headers, data=data)
        result = json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2)

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, data))
        logging.info("学生列表响应信息：{}".format(result))


if __name__ == "__main__":
    unittest.main()