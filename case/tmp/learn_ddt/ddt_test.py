import requests
import unittest
from ddt import ddt, data, unpack
from common.login import login
from common.resource_country import resource_country_list
from data_file import default_data
from case.tasks.task import test_task_list


@ddt
class TestTaskList(unittest.TestCase):
    s = requests.session()
    platform = default_data.platform
    uri = default_data.baseUrl

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberid = aa['body']['memberid']
        countryIds = resource_country_list(cls.s, cls.uri, cls.token, cls.memberid, cls.platform)[0]
        cls.countryId = str(countryIds[1])

        # cls.taskType = [0, 1, 2, 3, 4]  # 任务类型 0-全部，1-接单任务，2-定期回访任务，3-留学规划任务，4-定校任务
        # cls.taskStatus = [1, 2, 3]      # 任务状态 1-待办,2-未处理(过期),3-完成
        # cls.endType = [0, 1, 2, 3]      # 截止时间类型 0-全部，1-3小时内，2-今天，3-3天内

        '''
        一、全部-待办/未处理（过期）/完成任务测试
        '''

# 1. 全部-待办任务
    @data([(0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 1, 3)])
    @unpack
    def test_task_list_010(self, taskType, taskStatus, endType):
        # 010 全部-待办-全部
        print("case1: 010 全部-待办-全部 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, taskType, taskStatus, endType)


if __name__ == "__main__":
    unittest.main()