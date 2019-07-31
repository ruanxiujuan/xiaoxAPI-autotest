import unittest
from common.login import *
from data_file import default_data
import logging


class TestUnreadCount(unittest.TestCase):

    s = requests.session()     # 创建请求会话对象
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)   # 实例化登录对象
        aa = cls.a.outside_consultants_login(cls.uri)   # 调用外部顾问登录方法并返回用户数据
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

    def test_get_unread_count(self):
        '''
        通话记录红点接口
        :return: 通话记录红点数
        '''

        url = "/callRecords/unReadCount"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }

        res = requests.post(url=self.uri+url, headers=headers)

        logging.info("请求信息为：{0}{1}{2}".format(self.uri + url, headers, default_data))
        logging.info("响应信息为：{}".format(res.json()))

        # 获取未接通话数
        unReadCount = res.json()['body']['unReadCount']

        # 断言：1. 无未接通话，unReadCount=0; 2. 有未接通话，unReadCount>0
        try:
            if unReadCount == 0:
                self.assertEqual(0, unReadCount)
                logging.info("无新的未接通话！")
            elif unReadCount > 0:
                self.assertNotEqual(0, unReadCount)
                logging.info("有新的未接通话：" + str(unReadCount))
            else:
                logging.info("返回未知异常！")
        except Exception as e:
            logging.error(e)


if __name__ == "__main__":
    unittest.main()









