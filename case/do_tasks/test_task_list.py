import requests
import unittest
from lib.login import outside_consultants_login_normal
import json


class TestTaskList(unittest.TestCase):

    #  获取待办任务列表
    def test_get_task_list(self):
        url = "http://test-xiaoxapi.aoji.cn/task/list"

        # [测试方法：可用数据驱动的方式，将data中入参场景遍历一次！]
        data = {"taskType": "0",    # 任务类型 0-全部，1-接单任务，2-定期回访任务，3-留学规划任务，4-定校任务
                "taskStatus": "1",  # 任务状态 1-待办,2-未处理(过期),3-完成
                "name": "",         # 按名字搜索时名字参数
                "endType": "0",     # 截止时间类型 0-全部，1-3小时内，2-今天，3-3天内
                "startIndex": "0",
                "pageSize": "10"
                }
        userinfo = outside_consultants_login_normal()
        token = userinfo[0]
        memberId = userinfo[1]
        headers = {
            'platform': "3",
            'memberId': memberId,
            'token': token,
            'countryId': "65"
        }

        response = requests.post(url=url, data=data, headers=headers)

        print(json.dumps(response.json(), indent=2, ensure_ascii=False, sort_keys=True))

        self.assertEqual(0, response.json()['body']['code'])
        self.assertIsNotNone(response.json()['body']['list'])

        # taskIdList = jsonpath((response.json(),"$.body.list[*].id"))
        # taskTypeList = jsonpath(response.json(),"$.body.list[*].type")

        list = response.json()['body']['list']

        task_id_list = []
        for i in list:   # 获取所有taskId
            task_id_list.append(i['id'])

        task_type_list = []
        for j in list:   # 获取所有taskType
            task_type_list.append(j['type'])

        print(task_id_list, task_type_list)

        return task_id_list, token, memberId


if __name__ == "__main__":
    unittest.main(verbosity=2)


