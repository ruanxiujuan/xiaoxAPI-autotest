import unittest
import requests
import jsonpath
import logging
from lib.login import *
from data import data
from student import *


class TestStudentOverseaProgramShareDetail(unittest.TestCase):
    s = requests.session()
    uri = data.baseUrl
    platform = data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberid = aa['body']['memberid']
        studentName = test_student_add_resource(cls.s, cls.uri, cls.token, cls.memberid, cls.platform)
        resourceId1 = test_student_list_status_0(cls.s, cls.uri, cls.token, cls.memberid, cls.platform, studentName)[0]
        resourceId2 = test_student_update_oversea_program(cls.s, cls.uri, cls.token, cls.memberid, cls.platform, resourceId1)
        list_info = test_oversea_program_list(cls.s, cls.uri, cls.token, cls.memberid, cls.platform, resourceId2)
        resourceId3 = list_info[0]
        schemeId = list_info[1]
        schemeMemberId = list_info[2]
        detail_info = test_oversea_program_detail(cls.s, cls.uri, cls.token, cls.memberid, cls.platform, resourceId3, schemeId, schemeMemberId)
        cls.resourceId = detail_info[0]
        cls.schemeId = detail_info[1][0]
        cls.r = detail_info[2][0]
        cls.f = cls.memberid

    def test_oversea_program_share_detail(self):
        url = "/overseaProgram/shareDetail"
        headers = {
            "token": self.token,
            "memberId": self.memberid,
            "platform": self.platform,
            "browserId": "1"   # 通过微信分享
        }
        params = {
            "resourceId": self.resourceId,
            "schemeId": self.schemeId,
            "r": self.r,
            "f": self.f
        }
        response = requests.get(url=self.uri+url, headers=headers, params=params)
        result = json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2)

        print("请求url:{0},请求头：{1}，参数值：{2}".format(url, headers, params))
        print("响应体信息：{0}".format(result))

        # 断言：新增院校中文schoolchinesename、英文schoolenglishname字段，专业英文、中文majorname 字段，顾问详情expertDetail，国家优势advantageDetail；
        if result is not None:
            try:
                self.assertIn("schoolchinesename", result),
                self.assertIn("schoolenglishname", result),
                self.assertIn("majorname", result),
                self.assertIn("expertDetail", result),
                self.assertIn("advantageDetail", result),
            except AssertionError as error:
                print(error)


if __name__ == "__main__":
    unittest.main()