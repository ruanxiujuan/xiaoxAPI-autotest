import unittest
import logging
from common.login import *
from data_file import default_data


class TestSetAttend(unittest.TestCase):
    s = requests.session()
    platform = default_data.platform
    uri = default_data.baseUrl

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberid = aa['body']['memberid']

    def test_set_attend_type0(self):
        '''
        测试打卡接口：上线打卡
        '''
        url = "/counselor/setAttend"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberid
        }
        params = {
            "ClockType": "0"   # 打卡类型0上线打卡 1离线打卡
        }
        res = requests.get(url=self.uri+url, headers=headers, params=params)

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, params))
        logging.info("响应信息：{0}".format(res.json()))

        # 断言：上线打卡成功，返回code=0,msg=上线打卡成功
        detail = res.json()['body']['detail']
        code = res.json()['body']['detail']['code']
        msg = res.json()['body']['detail']['msg']
        if detail:
            try:
                self.assertEqual("0", code)
                self.assertEqual("上线打卡成功", msg)
            except Exception as e:
                logging.error(e)
        else:
            logging.info("无法获取到打卡详情信息")

    def test_set_attend_type1(self):
        '''
        测试打卡接口：离线打卡
        '''
        url = "/counselor/setAttend"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberid
        }
        params = {
            "ClockType": "1"   # 打卡类型0上线打卡 1离线打卡
        }
        res = requests.get(url=self.uri+url, headers=headers, params=params)

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, params))
        logging.info("响应信息：{0}".format(res.json()))

        # 断言：离线打卡成功，返回code=0, msg=离线打卡成功
        detail = res.json()['body']['detail']
        code = res.json()['body']['detail']['code']
        msg = res.json()['body']['detail']['msg']
        if detail:
            try:
                self.assertEqual("0", code)
                self.assertEqual("离线打卡成功", msg)
            except Exception as e:
                logging.error(e)
        else:
            logging.info("无法获取到打卡详情信息")


if __name__ == "__main__":
    unittest.main()








