import unittest
import requests
import json

from data import data
from lib.login import login
from student import *


class TestUpdateSchoolSelection(unittest.TestCase):
    s = requests.session()
    uri = data.baseUrl
    platform = data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']
        country_info = test_get_resource_country_list(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)
        cls.countryId = str(country_info[0][1])
        cls.countryName = country_info[1][1]
        school_info = test_get_school_by_country_id(cls.s, cls.uri, cls.countryId)
        cls.schoolId = str(school_info[0][0])
        cls.schoolName = school_info[1][0]
        # major_info = test_get_major_by_school_id(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, cls.schoolId)
        # cls.majorId = major_info[0]
        # cls.majorName = major_info[1]
        studentName = test_student_add_resource(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)
        resourceId = test_student_list_status_0(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, studentName)[0]
        cls.resourceId = str(test_student_detail_info_type1(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, resourceId)[0])

    def test_oversea_program_update_school_selection(self):
        url = "/overseaProgram/updateSchoolSelection"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }
        data = {
            "chooseId": "0",  # 选校建议编号:新增传0,修改传id值
            "countryId": self.countryId,
            "countryName": self.countryName,
            "schoolId": self.schoolId,
            "schoolName": self.schoolName,
            # "majorId": self.majorId,
            # "majorName": self.majorName,
            "remark": "the school selection create by autotest!",
            "resourceId": self.resourceId,
            "schemeId": "0",  # 方案编号:新增传0,修改传id值
        }
        response = requests.post(url=self.uri+url, headers=headers, data=data)
        result = json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2)
        print("请求信息：", self.uri+url, headers, data)
        print("响应信息：", result)
        data = jsonpath.jsonpath(response.json(), "$.body.data")

        # 断言：如果结果存在，则添加成功
        if result:
            self.assertIn("chooseid", result)
            self.assertIn("schemeid", result)
            print("选校建议添加成功！,添加的选校信息为：{}".format(data))


if __name__ == "__main__":
    unittest.main(verbosity=2)


