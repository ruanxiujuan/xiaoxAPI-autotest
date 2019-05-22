import unittest
import requests
import jsonpath
from rob_order.get_rob_resources_list import get_rob_resources_list
from lib.login import *
from lib.smart_counselor_db import *
from data import data


class TestRob(unittest.TestCase):
    s = requests.session()
    uri = data.baseUrl
    platform = data.platform

    @classmethod
    def setUpClass(cls):
        # 初始化会话对象
        cls.a = login(cls.s)
        # 登录用户
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberid = aa['body']['memberid']
        # 抢单列表
        rob_list = get_rob_resources_list(cls.s, cls.uri, cls.token, cls.memberid, cls.platform)
        # print(rob_list)
        cls.logId = jsonpath.jsonpath(rob_list, '$.body.data.list[*].logId')
        cls.resourceId = jsonpath.jsonpath(rob_list, '$.body.data.list[*].resourceId')
        # 创建数据库连接
        cls.conn = get_smart_counselor_db_connect()

    def test_rob_resource(self):
        # 环境准备-检查数据库是否有该账号数据
        USER = self.memberid
        query_sql = "SELECT * FROM rob_resource_detail WHERE member_id = '{}' ".format(USER)
        delete_sql = "DELETE FROM rob_resource_detail WHERE member_id = '{}'".format(USER)
        conn = self.conn
        result = query_db(query_sql)
        if result:
            change_db(delete_sql)

        # 请求及响应
        url = "/rob/robResource"
        headers = {
            'platform': "3",
            'token': self.token,
            'memberId': self.memberid
        }
        data = {
            "logId": self.logId[-1],
            "resourceId": self.resourceId[-1]
        }
        response = requests.post(url=self.uri+url, headers=headers, data=data)
        result = json.dumps(response.json(),ensure_ascii=False, sort_keys=True, indent=2)
        code = jsonpath.jsonpath(response.json(), '$.body.code')
        message = jsonpath.jsonpath(response.json(), '$.body.message')
        resourceId1 = jsonpath.jsonpath(response.json(), '$.body.resourceId')

        logging.info("请求url:{0},请求头{1},请求体{2}".format(url, headers, data))
        logging.info("响应体:"+response.text)

        # 断言
        if code[0] == 0:
            logging.info("抢单成功:{}".format(message), "资源编号:{}".format(resourceId1))
            self.assertIn(self.resourceId, resourceId1)

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
