import unittest, requests, json
from ddt import ddt, file_data
from common.login import *
from data_file import default_data
from case.students.student import get_student_detail_sms_template_list, send_sms


@ddt
class TestSendSms(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

        cls.smsCode = get_student_detail_sms_template_list(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)[1]


    def test_write_file(self):
        '''
        写文件接口，将短信模板中code写入到文件中，供发短信接口取值
        :return:
        '''
        fh = open(r"D:\xiaoxiAPI\case\students\sms_code.json", "w")
        templateCode = str(self.smsCode)
        smsCode = templateCode.replace("\'", '\"')  # 替换字符：将''替换成""
        fh.write(smsCode)
        fh.close()


    @file_data('sms_code.json')
    def test_send_sms(self, templateCode):
        '''
        测试发送短信接口
        :param templateCode:
        :return:
        '''
        print(templateCode)
        result = send_sms(self.s, self.uri, self.token, self.memberId, self.platform, templateCode)
        code = result[0]
        message = result[1]
        try:
            if code == 0:
                self.assertEqual(code, 0)
                self.assertEqual(message, "操作成功")
                print("短信发送成功！")
            else:
                print("短信发送失败！", message)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()
