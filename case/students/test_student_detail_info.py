import unittest
import logging
from common.login import *
from students.student import *
from data_file import default_data


class TestStudentDetailInfo(unittest.TestCase):
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
        resourceId_all = test_student_list_status_0(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, cls.studentName)
        cls.resourceId = resourceId_all[0]

    def test_student_detail_info_type1(self):
        '''
        学生详情页接口 - 资源阶段
        :return: 学生详情信息
        '''
        url = "/counselor/Student/detailInfo"
        headers = {
            "token": self.token,
            "memberId": self.memberId,
            "platform": self.platform
        }
        data = {
            "resourceId": self.resourceId,
            "type": "1"    # 资源类别 1资源阶段，2潜在阶段，3已签约(待定校、待申请、待签证、结案)
        }
        response = requests.post(url=self.uri+url, headers=headers, data=data)
        detail = json.dumps(response.json()['body']['detail'], ensure_ascii=False, sort_keys=True, indent=2)

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, data))
        logging.info("响应信息:{}".format(detail))

        resourceid = jsonpath.jsonpath(response.json(), "$.body.detail.resourceid")

        # 断言：学生详情信息，增加咨询顾问手机号、文签手机号
        if detail is not None:
            try:
                self.assertIn("customermobile", detail)
                self.assertIn("visaTel", detail)
            except AssertionError as msg:
                print(msg)

    def test_student_detail_info_type2(self):
        '''
        学生详情页接口 - 潜在阶段
        :return: 学生详情信息
        '''
        url = "/counselor/Student/detailInfo"
        headers = {
            "token": self.token,
            "memberId": self.memberId,
            "platform": self.platform
        }
        data = {
            "resourceId": self.resourceId,
            "type": "2"    # 资源类别 1资源阶段，2潜在阶段，3已签约(待定校、待申请、待签证、结案)
        }
        response = requests.post(url=self.uri+url, headers=headers, data=data)
        detail = json.dumps(response.json()['body']['detail'], ensure_ascii=False, sort_keys=True, indent=2)

        logging.info("请求信息：{0}{1}{2}".format(self.uri + url, headers, data))
        logging.info("响应信息:{}".format(detail))

        # 断言：学生详情信息，增加咨询顾问手机号、文签手机号
        if detail is not None:
            try:
                self.assertIn("customermobile", detail)
                self.assertIn("visaTel", detail)
            except AssertionError as e:
                logging.error(e)

    def test_student_detail_info_type3(self):
        '''
        学生详情页接口 - 已签约
        :return: 已签约学生详情
        '''
        url = "/counselor/Student/detailInfo"
        headers = {
            "token": self.token,
            "memberId": self.memberId,
            "platform": self.platform
        }
        data = {
            "resourceId": self.resourceId,
            "type": "3"    # 资源类别 1资源阶段，2潜在阶段，3已签约(待定校、待申请、待签证、结案)
        }
        response = requests.post(url=self.uri+url, headers=headers, data=data)
        detail = json.dumps(response.json()['body']['detail'], ensure_ascii=False, sort_keys=True, indent=2)

        logging.info("请求信息：{0}{1}{2}".format(self.uri + url, headers, data))
        logging.info("响应信息:{}".format(detail))

        # 断言：学生详情信息，增加咨询顾问手机号、文签手机号
        if detail is not None:
            try:
                self.assertIn("customermobile", detail)
                self.assertIn("visaTel", detail)
            except AssertionError as msg:
                print(msg)


if __name__ == "__main__":
    unittest.main()