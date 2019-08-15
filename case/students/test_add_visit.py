import unittest, requests
from ddt import ddt, data, unpack
from common.login import *
from data_file import default_data
from case.students.student import add_visit, test_student_list_status_0


@ddt
class TestAddVisit(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform

    remark = "自动化添加回访测试啦！"

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

        cls.resourceId = test_student_list_status_0(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)[0][0]

    '''    【添加回访】
           参数说明：
           callType：区分是公海还是死海扫码打电话 0-资源阶段扫码 2-根资源阶段扫码
           type：回访方式0:点击添加回访记录，手写回访记录，1:电话回访后填写回访记录
           stage：资源所处阶段1、客户意向不明确阶段2、具体沟通需求阶段 3、即将来访阶段4、来访后跟进阶段5、即将签约阶段6、放弃资源阶段
           非必填项：
           abandonReason：1、3天*每天3次电话均无人接听2、客户明确告知没有留学意向3、资源出现错号、空号等情况4、已签约小希平台5、已签约其他公司6、无法提供咨询服务7、其他
           '''
    # 第一种：手动添加回访
    @data(
        (0, 0, 1),    # 资源阶段-手写回访-客户意向不明确阶段
        (0, 0, 2),
        (0, 0, 3),
        (0, 0, 4),
        (0, 0, 5),
        (0, 0, 6),
        (2, 0, 1),
        (2, 0, 2),
        (2, 0, 3),
        (2, 0, 4),
        (2, 0, 5),
        (2, 0, 6)
    )
    @unpack
    def test_add_visit(self,callType, type, stage):
        add_visit(self.s, self.uri, self.token, self.memberId, self.platform, self.resourceId, self.remark, callType, type, stage)

    # 第二种：电话回访-未接通
    @data(
        (0, 1, 0, 1),    # 资源阶段-电话回访-3天*每天3次电话均无人接听
        (0, 1, 0, 2),
        (0, 1, 0, 3),
        (0, 1, 0, 4),
        (0, 1, 0, 5),
        (0, 1, 0, 6),
        (0, 1, 0, 7),
        (2, 1, 0, 1),
        (2, 1, 0, 2),
        (2, 1, 0, 3),
        (2, 1, 0, 4),
        (2, 1, 0, 5),
        (2, 1, 0, 6),
        (2, 1, 0, 6)
    )
    @unpack
    def test_add_visit_call(self,callType, type, stage, abandonReason):
        add_visit(self.s, self.uri, self.token, self.memberId, self.platform, self.resourceId, self.remark, callType, type, stage, abandonReason)

    # 第三种：电话回访-接通
    @data(
        (0, 1, 0),    # 资源阶段-电话回访-3天*每天3次电话均无人接听
        (0, 1, 0),
        (0, 1, 0),
        (0, 1, 0),
        (0, 1, 0),
        (0, 1, 0),
        (0, 1, 0),
        (2, 1, 0),
        (2, 1, 0),
        (2, 1, 0),
        (2, 1, 0),
        (2, 1, 0),
        (2, 1, 0),
        (2, 1, 0)
    )
    @unpack
    def test_add_visit_call(self,callType, type, stage):
        add_visit(self.s, self.uri, self.token, self.memberId, self.platform, self.resourceId, self.remark, callType, type, stage)


if __name__ == "__main__":
    unittest.main()


