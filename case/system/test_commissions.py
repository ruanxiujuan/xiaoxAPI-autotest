import unittest
import time
from common.login import *
from data_file import default_data


class TestCommissions(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

    def test_commissions(self):
        url = "/system/commissions"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }
        month = time.strftime("%y-%m",time.localtime(time.time()))
        data = {
            "date": month,
            "startIndex": 0,
            "pageSize": 10
        }

        res = self.s.post(url=self.uri+url, headers=headers, data=data)

        commission = res.json()['body']['commission']

        try:
            if commission:
                self.assertIsNotNone(commission)
        except Exception as e:
            print(e)
        else:
            print("钱包列表信息为：", commission)


if __name__ == "__main__":
    unittest.main()

