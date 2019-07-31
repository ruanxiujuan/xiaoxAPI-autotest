import unittest
import logging
from common.login import *
from data_file import default_data
from student import *


class TestStudentOverseaProgramList(unittest.TestCase):
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
        resourceId = test_student_list_status_0(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, cls.studentName)[0]
        cls.resourceId = test_student_update_oversea_program(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, resourceId)

    def test_oversea_program_list(self):
        '''
        留学规划方案接口，根据学生资源id获取学生留学规划方案
        :return: 留学规划方案列表信息
        '''
        url = "/overseaProgram/list"
        headers = {
            "token": self.token,
            "memberId": self.memberId,
            "platform": self.platform
        }
        data = {
            "resourceId": self.resourceId,
            "startIndex": "0",
            "pageSize": "10"
        }
        response = requests.post(url=self.uri+url, headers=headers, data=data)
        detail = json.dumps(response.json()['body']['list'], ensure_ascii=False, sort_keys=True, indent=2)
        list = json.dumps(response.json()['body']['list'], ensure_ascii=False, sort_keys=True, indent=2)

        logging.info("请求信息：{0}{1}{2}".format(self.uri + url, headers, data))
        logging.info("响应信息:{}".format(detail))

        # 断言：新增是否文件isfile、文件名filename、文件地址filepath字段
        if list is not None:
            try:
                self.assertIn("isfile", list),
                self.assertIn("filename", list),
                self.assertIn("filepath", list)
            except AssertionError as error:
                logging.error(error)


if __name__ == "__main__":
    unittest.main()