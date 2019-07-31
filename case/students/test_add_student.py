import unittest
import logging
from common.login import *
from data_file import default_data
from students.student import *


class TestStudentAddResource(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberid = aa['body']['memberid']
        coutryId_all = resource_country_list(cls.s, cls.uri, cls.token, cls.memberid, cls.platform)
        cls.countryId = coutryId_all[0]

    def test_student_add_resource(self):
        '''
        添加学生接口
        :return: 添加的学生信息
        '''
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

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, data))
        logging.info("响应信息：{0}".format(response.json()))
        logging.info("录入的学生信息为", data)


if __name__ == "__main__":
    unittest.main()
