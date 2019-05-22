import unittest
import requests
import json
import jsonpath
import logging
import random
from lib.login import *
from data import data
from students.student import *


class TestStudentAddResource(unittest.TestCase):
    s = requests.session()
    uri = data.baseUrl
    platform = data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberid = aa['body']['memberid']
        coutryId_all = test_get_resource_country_list(cls.s, cls.uri, cls.token, cls.memberid, cls.platform)
        cls.countryId = coutryId_all[0]

    def test_student_add_resource(self):
        url = "/counselor/addResource"
        headers = {
            "token": self.token,
            "memberId": self.memberid,
            "platform": self.platform,
            "vcode": "21300"
        }
        data = {
            "resourceType": "1",   #  资源类型(0:名片，1:资源)
            "studentName": "autotest{0}".format(random.randint(1, 100)),
            "tel": "130{0}".format(random.randint(11110001, 11119999)),
            "countryId": self.countryId ,
            "remark": "自动化测试脚本添加"
        }
        response = requests.post(url=self.uri+url, headers=headers, data=data)
        print("请求信息：", url, headers, data)
        print("响应信息：", response.text)
        print("录入的学生信息为", data)
        return data


if __name__ == "__main__":
    unittest.main()
