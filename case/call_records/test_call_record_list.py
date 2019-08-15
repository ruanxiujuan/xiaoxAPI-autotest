import unittest
from common.login import *
from data_file import default_data
import logging



class TestCallRecordList(unittest.TestCase):

    s = requests.session()     # 创建请求会话对象
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)   # 实例化登录对象
        aa = cls.a.outside_consultants_login(cls.uri)   # 调用外部顾问登录方法并返回用户数据
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

    def test_call_record_list_type0(self):
        '''
        全部通话接口
        :return: 全部通话列表
        '''

        url = "/callRecords/recordList"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }

        data = {
            "type": 0   # 全部通话
        }

        res = requests.post(url=self.uri+url, headers=headers, data=data)

        logging.info("请求信息为：{0}{1}{2}".format(self.uri + url, headers, data))
        logging.info("响应信息为：{}".format(res.json()))

        # 获取通话列表
        list = res.json()['body']['list']

        # 断言：1. list为空，无通话; 2. list不为空，打印全部通话
        try:
            if list is None:
                self.assertIsNone(list)
                logging.info("暂无通话")
            else:
                self.assertIsNotNone(list)
                logging.info("所有通话记录为：" + str(len(list)))
                for i in list:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    def test_call_record_list_type1(self):
        '''
        未接通话接口
        :return: 未接通话列表
        '''

        url = "/callRecords/recordList"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }

        data = {
            "type": 1   # 未接通话
        }

        res = requests.post(url=self.uri+url, headers=headers, data=data)

        logging.info("请求信息为：{0}{1}{2}".format(self.uri + url, headers, data))
        logging.info("响应信息为：{}".format(res.json()))

        # 获取通话列表
        list = res.json()['body']['list']

        # 断言：1. list为空，无通话; 2. list不为空，打印未接通话
        try:
            if len(list) == 0:
                logging.info("暂无通话")
            else:
                logging.info("未接通话记录为：" + str(len(list)))
                for i in list:
                    logging.info(i)
        except Exception as e:
            logging.error(e)


if __name__ == "__main__":
    unittest.main()










