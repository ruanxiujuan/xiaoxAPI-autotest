import unittest
from common.login import *
from data_file import default_data
from common.resource_country import resource_country_list
from school import member_save_country


class TestMemberGetAreaList(unittest.TestCase):

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
        countryId = countryIds[1]  # 澳洲

        # 调用用户保存国家接口获取国家id
        cls.countryId = member_save_country(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, countryId)

    def test_member_get_area_list(self):
        '''
        测试地区列表接口
        '''
        url = "/member/getAreaList"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }

        params = {
            "countryId": str(self.countryId)
        }

        res = requests.get(url=self.uri+url, headers=headers, params=params)

        print("请求信息为：{0}{1}{2}".format(self.uri + url, headers, params))
        print("响应信息为：{}".format(res.json()))

        # 断言：获取地区列表信息并判断是否存在，存在则打印
        list = res.json()['body']['list']
        try:
            if list:
                print("地区信息~")
                for i in list:
                    print(i)
            else:
                print("无对应地区信息")
        except Exception as e:
            print(e)

        # 获取地区列表信息id并返回
        AreaId = jsonpath.jsonpath(res.json(), "$.body.list[*].id")
        print(AreaId)


if __name__ == "__main__":
    unittest.main()










