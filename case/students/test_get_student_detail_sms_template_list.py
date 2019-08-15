import unittest, requests,json
from common.login import *
from data_file import default_data
from case.students.student import get_student_detail_sms_template_list


class TestGetSmsTemplateList(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

    def test_get_student_detail_sms_template_list(self):
        '''
        测试短信模板接口
        '''
        templateList = get_student_detail_sms_template_list(self.s, self.uri, self.token, self.memberId, self.platform)[0]

        try:
            if templateList is not None:
                self.assertIsNotNone(templateList)
                print("短信模板内容为：", json.dumps(templateList, ensure_ascii=False, sort_keys=True, indent=2))
            else:
                self.assertIsNone(templateList)
                print("短信模板为空！")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()

