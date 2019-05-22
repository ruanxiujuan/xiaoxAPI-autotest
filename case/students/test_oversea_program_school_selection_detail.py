import unittest
import requests
from lib.login import *
from data import data
from student import *


class TestStudentOverseaProgramDetail(unittest.TestCase):
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
        countryId = str(country_info[0][1])
        countryName = country_info[1][1]
        school_info = test_get_school_by_country_id(cls.s, cls.uri, countryId)
        schoolId = str(school_info[0][0])
        schoolName = school_info[1][0]
        # major_info = test_get_major_by_school_id(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, cls.schoolId)
        # cls.majorId = major_info[0]
        # cls.majorName = major_info[1]
        studentName = test_student_add_resource(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)
        resourceId1 = test_student_list_status_0(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, studentName)[0]
        resourceId2 = str(test_student_detail_info_type1(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, resourceId1)[0])
        school_selection_info = test_oversea_program_update_school_selection(cls.s,cls.uri,cls.token,cls.memberId,cls.platform,countryId,countryName,schoolId,schoolName,resourceId2)
        cls.chooseId = school_selection_info[0]

    def test_oversea_program_school_selection_detail(self):   # 根据选校id查询选校详情信息
        url = "/overseaProgram/schoolSelectionDetail"
        headers = {
            "token": self.token,
            "memberId": self.memberId,
            "platform": self.platform
        }
        data = {
            "chooseId": self.chooseId
        }
        response = requests.post(url=self.uri+url, headers=headers, data=data)
        result = json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2)
        print("请求信息：", self.uri+url, headers, data)
        print("响应信息", result)

        detail = json.dumps(response.json()['body']['detail'], ensure_ascii=False, sort_keys=True, indent=2)

        # 断言：新增院校schoolenglishname和专业名称majorname拼接中英文
        if result is not None:
            try:
                self.assertIn("schoolname", result),
                self.assertIn("majorname", result)
                print("选校建议详情为：", detail)
            except AssertionError as error:
                print(error)


if __name__ == "__main__":
    unittest.main()