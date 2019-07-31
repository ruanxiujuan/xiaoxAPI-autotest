import requests
import unittest
import json
import jsonpath
from common.login import login
from data_file import default_data


class TestTaskType(unittest.TestCase):
    s = requests.session()
    platform = default_data.platform
    uri = default_data.baseUrl

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberid = aa['body']['memberid']

    def test_task_type(self):
        url = "/task/type"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberid
        }
        res = requests.post(url=self.uri+url, headers=headers)
        # print(res.json())

        type_list = json.dumps(res.json()['body']['list'], ensure_ascii=False, sort_keys=True, indent=2)
        print(type_list)

        type_id = jsonpath.jsonpath(res.json(), "$.body.list[*].id")
        type_name = jsonpath.jsonpath(res.json(), "$.body.list[*].name")
        print(type_id, type_name)


if __name__ == "__main__":
    unittest.main()
