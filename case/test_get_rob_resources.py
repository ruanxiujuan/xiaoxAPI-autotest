import unittest
import requests
import json
import jsonpath
import logging
from lib.login import outside_consultants_login_normal


class TestGetRob(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 登录用户
        cls.user_info = outside_consultants_login_normal()
        cls.token = cls.user_info[0]
        cls.memberId = cls.user_info[1]

    # 抢单列表
    def test_get_rob_resources_list(self):
        url = "http://test-xiaoxapi.aoji.cn/rob/getRobResources"

        headers = {
            "platform": "3",
            "token": self.token,
            "memberId": self.memberId
        }

        response = requests.post(url=url, headers=headers, data=None)
        # print(json.dumps(response.json(), indent=2, ensure_ascii=False, sort_keys=True))

        logging.info("请求url:{0},请求头{1}".format(url, headers))
        logging.info("响应体:" + response.text)

        list = jsonpath.jsonpath(response.json(), '$.body.data.list[*]')
        status = jsonpath.jsonpath(response.json(), '$.body.data.list[*].status')
        remainingTime = jsonpath.jsonpath(response.json(), '$.body.data.remainingTime')
        next = jsonpath.jsonpath(response.json(), '$.body.data.next')
        logid = jsonpath.jsonpath(response.json(), '$.body.data.list[*].logId')
        resourceId = jsonpath.jsonpath(response.json(), '$.body.data.list[*].resourceId')

        # 1. 新单资源,抢单列表抢单状态status = 0(未被抢); 且有本轮结束倒计时
        # 2. 抢单中,抢单列表部分资源已被抢status in [0,1]; 且有本轮结束倒计时
        # 3. 抢单结束,抢单列表所有资源被抢status = 1; 且有下一轮开始时间
        # 4. 无资源,抢单资源列表为空

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

        return logid, resourceId


if __name__ == '__main__':
    unittest.main()
