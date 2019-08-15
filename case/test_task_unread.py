import requests
import unittest
from case.test_task_list import TestTaskList
import json


class TestTaskTaskUnRead(unittest.TestCase):
    # 获取待办任务详情
    def test_get_task_unread(self):
        url = "http://test-xiaoxapi.aoji.cn/task/unReadCount"
        info = TestTaskList.test_get_task_list(self)
        token = info[1]
        memberId = info[2]
        id = str(info[0])
        headers = {
            'platform': "3",
            'token': token,
            'memberId': memberId,
            'countryId': ""
        }
        response = requests.post(url=url, headers=headers)

        print(json.dumps(response.json(), indent=2, ensure_ascii=False, sort_keys=True))

        self.assertEqual(0, response.json()['body']['code'])
        self.assertEqual("操作成功", response.json()['body']['message'])



if __name__=="__main__":
    unittest.main(verbosity=2)

