import unittest
import requests
import jsonpath
import logging
from test_get_rob_resources import TestGetRob
from lib.login import outside_consultants_login_normal
from lib.smart_counselor_db import *


class TestRob(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 登录用户
        cls.user_info = outside_consultants_login_normal()
        cls.token = cls.user_info[0]
        cls.memberId = cls.user_info[1]
        # 创建数据库连接
        cls.conn = get_smart_counselor_db_connect()

    def test_rob_resource(self):
        # 环境准备-检查数据库是否有该账号数据
        USER = self.memberId
        query_sql = "SELECT * FROM rob_resource_detail WHERE member_id = '{}' ".format(USER)
        delete_sql = "DELETE FROM rob_resource_detail WHERE member_id = '{}'".format(USER)
        conn = self.conn
        result = query_db(query_sql)
        if result:
            change_db(delete_sql)

        # 请求及响应
        url = "http://test-xiaoxapi.aoji.cn/rob/robResource"
        headers = {
            'platform': "3",
            'token': self.token,
            'memberId': self.memberId
        }
        logId = TestGetRob.test_get_rob_resources_list(self)[0]
        resourceId = TestGetRob.test_get_rob_resources_list(self)[1]
        data = {
            "logId": logId[-1],
            "resourceId": resourceId[-1]
        }
        response = requests.post(url=url, headers=headers, data=data)

        logging.info("请求url:{0},请求头{1},请求体{2}".format(url, headers, data))
        logging.info("响应体:"+response.text)

        code = jsonpath.jsonpath(response.json(), '$.body.code')
        message = jsonpath.jsonpath(response.json(), '$.body.message')
        resourceId_result = jsonpath.jsonpath(response.json(), '$.body.resourceId')

        # 断言
        if code[0] == 0:
            logging.info("抢单成功:{}".format(message), "资源编号:{}".format(resourceId_result))
            self.assertEqual(resourceId, resourceId_result)

            # 数据库断言
            result2 = query_db(query_sql)  # 返回的结果为嵌套元组
            member_id = result2[0][10]
            self.assertEqual(USER, member_id)

            # 环境清理
            change_db(delete_sql)
            conn.close()

        elif code[0] == 1:
            logging.info("手慢已被抢：{}".format(message))
        elif code[0] == 2:
            logging.info("抢单资源达到上限：{}".format(message))
        else:
            logging.info("其它原因")


if __name__ == '__main__':
    unittest.main()
