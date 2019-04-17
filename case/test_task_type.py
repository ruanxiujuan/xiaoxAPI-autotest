import requests
import unittest
from lib.login import outside_consultants_login_normal


class TestTaskType(unittest.TestCase):
    # 获取待办任务类型
    def test_get_task_type(self):
        url = "http://test-xiaoxapi.aoji.cn/task/type"
        userinfo = outside_consultants_login_normal()
        token = userinfo[0]
        memberId = userinfo[1]
        headers = {
            'platform': "3",
            'token': token,
            'memberId': memberId
        }

        response = requests.post(url=url, headers=headers)

        print(response.json())

        self.assertEqual(0, response.json()['body']['code'])
        self.assertEqual('操作成功', response.json()['body']['message'])
        self.assertIn({'id': 0, 'name': '全部'}, response.json()['body']['list'])

        list = response.json()['body']['list']

        list_id = []
        for i in list:
            list_id.append(i['id'])
        print(list_id)

        return list_id, token, memberId


if __name__ == "__main__":
    unittest.main(verbosity=2)


