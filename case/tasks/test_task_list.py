import requests
import unittest

from common.login import login
from common.resource_country import resource_country_list
from data_file import default_data
from case.tasks.task import test_task_list


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

        cls.taskType = [0, 1, 2, 3, 4]  # 任务类型 0-全部，1-接单任务，2-定期回访任务，3-留学规划任务，4-定校任务
        cls.taskStatus = [1, 2, 3]      # 任务状态 1-待办,2-未处理(过期),3-完成
        cls.endType = [0, 1, 2, 3]      # 截止时间类型 0-全部，1-3小时内，2-今天，3-3天内

        '''
        一、全部-待办/未处理（过期）/完成任务测试
        '''

# 1. 全部-待办任务

    def test_task_list_010(self):
        # 010 全部-待办-全部
        print("case1: 010 全部-待办-全部 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[0], self.taskStatus[0], self.endType[0])

    def test_task_list_011(self):
        # 011 全部-待办-3小时内
        print("case2: 011 全部-待办-3小时内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[0],
                       self.taskStatus[0], self.endType[1])

    def test_task_list_012(self):
        # 012 全部-待办-今天
        print("case3: 012 全部-待办-今天 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[0],
                       self.taskStatus[0], self.endType[2])

    def test_task_list_013(self):
        # 013 全部-待办-3天内
        print("case4: 013 全部-待办-3天内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[0],
                       self.taskStatus[0], self.endType[-1])

# 2. 全部-未处理（过期）任务
    def test_task_list_020(self):
        # 020 全部-未处理（过期）-全部
        print("case21: 020 全部-待办-全部 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[0],
                       self.taskStatus[1], self.endType[0])

    def test_task_list_021(self):
        # 021 全部-未处理（过期）-3小时内
        print("case22: 021 全部-待办-3小时内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[0],
                       self.taskStatus[1], self.endType[1])

    def test_task_list_022(self):
        # 022 全部-未处理（过期）-今天
        print("case23: 022 全部-待办-今天 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[0],
                       self.taskStatus[1], self.endType[2])

    def test_task_list_023(self):
        # 023 全部-未处理（过期）-3天内
        print("case24: 023 全部-待办-3天内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[0],
                       self.taskStatus[1], self.endType[-1])

# 3. 全部-完成任务
    def test_task_list_030(self):
        # 030 全部-完成-全部
        print("case25: 030 全部-完成-全部 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[0],
                       self.taskStatus[-1], self.endType[0])


    def test_task_list_031(self):
        # 031 全部-完成-3小时内
        print("case26: 031 全部-完成-3小时内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[0],
                       self.taskStatus[-1], self.endType[1])


    def test_task_list_032(self):
        # 032 全部-完成-今天
        print("case27: 032 全部-完成-今天 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[0],
                       self.taskStatus[-1], self.endType[2])


    def test_task_list_033(self):
        # 033 全部-完成-3天内
        print("case28: 033 全部-完成-3天内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[0],
                       self.taskStatus[-1], self.endType[-1])


        '''
        二、接单-待办任务测试
        '''
# 1. 接单-待办任务
    def test_task_list_110(self):
        # 110 接单-待办-全部
        print("case5: 110 接单-待办-全部 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[1],
                       self.taskStatus[0], self.endType[0])

    def test_task_list_111(self):
        # 111 接单-待办-3小时内
        print("case6: 111 接单-待办-3小时内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[1],
                       self.taskStatus[0], self.endType[1])

    def test_task_list_112(self):
        # 112 接单-待办-今天
        print("case7: 112 接单-待办-今天 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[1],
                       self.taskStatus[0], self.endType[2])

    def test_task_list_113(self):
        # 113 接单-待办-3天内
        print("case8: 113 接单-待办-3天内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[1],
                       self.taskStatus[0], self.endType[-1])

# 2. 接单-未处理（过期）任务
    def test_task_list_120(self):
        # 120 接单-未处理（过期）-全部
        print("case29: 120 接单-待办-全部 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[1],
                       self.taskStatus[1], self.endType[0])

    def test_task_list_121(self):
        # 121 接单-未处理（过期）-3小时内
        print("case30: 121 接单-待办-3小时内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[1],
                       self.taskStatus[1], self.endType[1])

    def test_task_list_122(self):
        # 122 接单-未处理（过期）-今天
        print("case31: 122 接单-待办-今天 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[1],
                       self.taskStatus[1], self.endType[2])

    def test_task_list_123(self):
        # 123 接单-未处理（过期）-3天内
        print("case32: 123 接单-待办-3天内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[1],
                       self.taskStatus[1], self.endType[-1])

        '''
        三、定期回访-待办任务测试
        '''

    def test_task_list_210(self):
        # 210 定期回访-待办-全部
        print("case9: 210 定期回访-待办-全部 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[2],
                       self.taskStatus[0], self.endType[0])

    def test_task_list_211(self):
        # 211 定期回访-待办-3小时内
        print("case10: 211 定期回访-待办-3小时内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[2],
                       self.taskStatus[0], self.endType[1])

    def test_task_list_212(self):
        # 212 定期回访-待办-今天
        print("case11: 212 定期回访-待办-今天 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[2],
                       self.taskStatus[0], self.endType[2])

    def test_task_list_213(self):
        # 213 定期回访-待办-3天内
        print("case12: 213 定期回访-待办-3天内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[2],
                       self.taskStatus[0], self.endType[-1])

        '''
        四、留学规划-待办任务测试
        '''

    def test_task_list_310(self):
        # 310 留学规划-待办-全部
        print("case13: 310 留学规划-待办-全部 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[3],
                       self.taskStatus[0], self.endType[0])

    def test_task_list_311(self):
        # 311 留学规划-待办-3小时内
        print("case14: 311 留学规划-待办-3小时内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[3],
                       self.taskStatus[0], self.endType[1])

    def test_task_list_312(self):
        # 312 留学规划-待办-今天
        print("case15: 312 留学规划-待办-今天 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[3],
                       self.taskStatus[0], self.endType[2])

    def test_task_list_313(self):
        # 313 留学规划-待办-3天内
        print("case16: 313 留学规划-待办-3天内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[3],
                       self.taskStatus[0], self.endType[-1])

        '''
        五、定校任务-待办任务测试
        '''

    def test_task_list_410(self):
        # 410 定校任务-待办-全部
        print("case17: 410 留学规划-待办-全部 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[3],
                       self.taskStatus[0], self.endType[0])

    def test_task_list_411(self):
        # 411 定校任务-待办-3小时内
        print("case18: 411 留学规划-待办-3小时内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[3],
                       self.taskStatus[0], self.endType[1])

    def test_task_list_412(self):
        # 412 定校任务-待办-今天
        print("case19: 412 留学规划-待办-今天 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[3],
                       self.taskStatus[0], self.endType[2])

    def test_task_list_413(self):
        # 413 定校任务-待办-3天内
        print("case20: 413 留学规划-待办-3天内 任务列表")
        test_task_list(self.s, self.uri, self.token, self.memberid, self.platform, self.countryId, self.taskType[3],
                       self.taskStatus[0], self.endType[-1])


if __name__ == "__main__":
    unittest.main()
