import unittest
import logging
from common.login import *
from data_file import default_data


class TestGetAttend(unittest.TestCase):
    s = requests.session()
    platform = default_data.platform
    uri = default_data.baseUrl

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberid = aa['body']['memberid']

    def test_get_attend_by_id(self):
        url = "/counselor/getAttendById"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberid
        }
        res = requests.get(url=self.uri + url, headers=headers)

        logging.info("请求信息：{0}{1}".format(self.uri + url, headers))
        logging.info("响应信息：{0}".format(res.json()))

        # 断言：打卡后，可获取到打卡信息
        result = res.json()['body']['result']
        clockType = res.json()['body']['result']['clockType']
        clockTypeId = res.json()['body']['result']['clockTypeId']
        clockResult = ["上线", "离线"]
        if result:
            logging.info(clockTypeId, clockType)
            try:
                for clockType in clockResult:
                    self.assertIn(clockType, clockResult)
            except Exception as e:
                logging.error(e)
        else:
            logging.error("未获取到打卡信息")


if __name__ == "__main__":
    unittest.main()







