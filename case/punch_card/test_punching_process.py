import unittest
from common.login import *
from data_file import default_data
from case.punch_card.set_attend import *


class TestPunchingProcessOnLine(unittest.TestCase):
    '''
    测试打卡流程：
    1. 请求打卡
    2. 获取打卡信息
    '''
    s = requests.session()
    platform = default_data.platform
    uri = default_data.baseUrl
    ClockType = [0, 1]   # 打卡类型0上线打卡 1离线打卡

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberid = aa['body']['memberid']

    def test_punching_process_on_line(self):
        # 1.上线打卡
        test_set_attend_type(self.s, self.uri, self.token, self.memberid, self.platform, self.ClockType[0])

        # 2. 获取打卡信息
        test_get_attend_by_id(self.s, self.uri, self.token, self.memberid, self.platform)

    def test_punching_process_off_line(self):
        # 1. 离线打卡
        test_set_attend_type(self.s, self.uri, self.token, self.memberid, self.platform, self.ClockType[1])

        # 2. 获取打卡信息
        test_get_attend_by_id(self.s, self.uri, self.token, self.memberid, self.platform)


if __name__ == "__main__":
    unittest.main()



