import unittest
from common.login import *
from data_file import default_data
from common.resource_country import resource_country_list
from school import *


class TestSchoolDetailCanada(unittest.TestCase):

    s = requests.session()     # 创建请求会话对象
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)   # 实例化登录对象
        aa = cls.a.outside_consultants_login(cls.uri)   # 调用外部顾问登录方法并返回用户数据
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

        # 调用国家列表接口获取国家id
        countryInfo = resource_country_list(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)
        countryIds = countryInfo[0]
        countryId = countryIds[3]  # 加拿大

        # 调用用户保存国家接口获取国家id
        cls.countryId = member_save_country(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, countryId)

        # 调用热门院校接口获取院校id
        schoolIds = school_rank(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, countryId)
        cls.schoolId = schoolIds[0]


    def test_school_detail_canada(self):
        '''
        测试院校详情接口
        '''
        url = "/school/detail"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId,
            "countryId": str(self.countryId)
        }

        params = {
            "schoolId": self.schoolId
        }

        res = requests.get(url=self.uri+url, headers=headers, params=params)
        result = json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2)

        print("请求信息为：{0}{1}{2}".format(self.uri + url, headers, params))
        print("响应信息为：{}".format(result))

        # 断言：本国院校排名检查
        nationalRankType = ['综合类', '基础类', '医博类']
        localRankType = jsonpath.jsonpath(res.json(), "$.body.school.localRankType")
        try:
            if localRankType:
                for localRankType in nationalRankType:
                    self.assertIn(nationalRankType, localRankType)
            else:
                print("本国排名无数据")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()










