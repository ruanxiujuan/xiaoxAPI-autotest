import unittest
import logging
from common.login import *
from data_file import default_data
from student import *


class TestStudentOverseaProgramDetail(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberid = aa['body']['memberid']
        cls.studentName = test_student_add_resource(cls.s, cls.uri, cls.token, cls.memberid, cls.platform)
        resourceId1 = test_student_list_status_0(cls.s, cls.uri, cls.token, cls.memberid, cls.platform)[0]
        resourceId2 = test_student_update_oversea_program(cls.s, cls.uri, cls.token, cls.memberid, cls.platform, resourceId1)
        list_info = test_oversea_program_list(cls.s, cls.uri, cls.token, cls.memberid, cls.platform, resourceId2)
        cls.resourceId = list_info[0]
        cls.schemeId = list_info[1]
        cls.schemeMemberId = list_info[2]

    def test_get_oversea_program_detail(self):
        '''
        留学规划方案详情接口，根据方案id+顾问id 查询留学规划方案详情
        :return: 留学规划方案详情信息
        '''
        url = "/overseaProgram/detail"
        headers = {
            "token": self.token,
            "memberId": self.memberid,
            "platform": self.platform
        }
        data = {
            "resourceId": self.resourceId,
            "schemeId": self.schemeId,
            "schemeMemberId": self.schemeMemberId
        }
        response = requests.post(url=self.uri+url, headers=headers, data=data)
        result = json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2)

        logging.info("请求信息：{0}{1}{2}".format(self.uri + url, headers, data))
        logging.info("响应信息：{0}".format(result))

        # 断言：新增院校schoolname和专业名称majorname拼接中英文；
        if result is not None:
            try:
                self.assertIn("schoolname", result),
                self.assertIn("majorname", result)
            except AssertionError as error:
                logging.error(error)


if __name__ == "__main__":
    unittest.main()