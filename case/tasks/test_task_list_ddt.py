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


    '''
    做任务接口测试：
    按照任务完成情况、任务总类、截止时间3个维护写遍历每种场景测试~
    如：待办任务-接单-全部
    '''

    @data((0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 1, 3),
          (0, 2, 0), (0, 2, 1), (0, 2, 2), (0, 2, 3),
          (0, 3, 0), (0, 3, 1), (0, 3, 2), (0, 3, 3),
          (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 1, 3),
          (1, 2, 0), (1, 2, 1), (1, 2, 2), (1, 2, 3),
          (1, 3, 0), (1, 3, 1), (1, 3, 2), (1, 3, 3),
          (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 1, 3),
          (2, 2, 0), (2, 2, 1), (2, 2, 2), (2, 2, 3),
          (2, 3, 0), (2, 3, 1), (2, 3, 2), (2, 3, 3),
          (3, 1, 0), (3, 1, 1), (3, 1, 2), (3, 1, 3),
          (3, 2, 0), (3, 2, 1), (3, 2, 2), (3, 2, 3),
          (3, 3, 0), (3, 3, 1), (3, 3, 2), (3, 3, 3),
          (4, 1, 0), (4, 1, 1), (4, 1, 2), (4, 1, 3),
          (4, 2, 0), (4, 2, 1), (4, 2, 2), (4, 2, 3),
          (4, 3, 0), (4, 3, 1), (4, 3, 2), (4, 3, 3))
    @unpack
    def test_task_list_010(self, taskType, taskStatus, endType):
            test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, taskType,
                           taskStatus, endType)


if __name__ == "__main__":
    unittest.main()