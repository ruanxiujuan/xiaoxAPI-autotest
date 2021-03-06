import unittest
import logging
from common.login import *
from data_file import default_data


class TestGetRob(unittest.TestCase):
    s = requests.session()
    platform = default_data.platform
    uri = default_data.baseUrl

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberid = aa['body']['memberid']

    def test_get_rob_resources_list(self):
        '''
        抢单列表接口
        :return: 抢单列表数据gn r 
        '''
        url = "/rob/getRobResources"

        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberid
        }
        response = requests.post(url=self.uri+url, headers=headers, data=None)

        logging.info("请求url:{0},请求头{1}".format(self.uri+url, headers))
        logging.info("响应体:" + response.text)

        list = jsonpath.jsonpath(response.json(), '$.body.data_file.list[*]')
        status = jsonpath.jsonpath(response.json(), '$.body.data_file.list[*].status')
        remainingTime = jsonpath.jsonpath(response.json(), '$.body.data_file.remainingTime')
        next = jsonpath.jsonpath(response.json(), '$.body.data_file.next')

        '''
        断言：
        1. 新单资源,抢单列表抢单状态status = 0(未被抢); 且有本轮结束倒计时
        2. 抢单中,抢单列表部分资源已被抢status in [0,1]; 且有本轮结束倒计时
        3. 抢单结束,抢单列表所有资源被抢status = 1; 且有下一轮开始时间
        4. 无资源,抢单资源列表为空
        '''

        if list is not None:
            for i in status:
                if i == 0:
                    logging.info("抢单列表为新资源{0},本轮倒计时为{1}".format(list, remainingTime))
                elif i == 1:
                    logging.info("抢单结束,抢单资源为{0},下一轮抢单时间为{1}".format(list, next))
                else:
                    logging.info("正在抢单中,抢单列表部分数据已被抢,资源数据为{0},本轮倒计时为{1}".format(list, remainingTime))
        else:
            logging.info("抢单列表为空,抢单列表无资源!")


if __name__ == '__main__':
    unittest.main()
