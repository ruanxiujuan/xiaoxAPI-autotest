import requests
import unittest
from do_tasks.test_task_list import TestTaskList
import json


class TestTaskAccept(unittest.TestCase):

    # 接受待办任务
    def test_get_task_accept(self):
        info = TestTaskList.test_get_task_list(self)
        idlist = info[0]
        task_type = [1, 2]

        url = "http://test-xiaoxapi.aoji.cn/task/accept"

        for id in idlist:
            taskId = id
        for type in task_type:
            type = type
        payload = {"taskId": taskId,
                   "type": type}

        token = info[1]
        memberId = info[2]
        headers = {
            'platform': "3",
            'memberId': memberId,
            'token': token,
            'countryId': ""
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(json.dumps(response.json(), indent=2, ensure_ascii=False, sort_keys=True))


if __name__=="__main__":
    unittest.main(verbosity=2)


