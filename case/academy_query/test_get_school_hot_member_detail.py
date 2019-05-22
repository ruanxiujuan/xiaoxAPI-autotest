import unittest
import requests
import json
import jsonpath
import logging
from lib.login import *


class TestGetSchoolHotMemberDetial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 登录平台顾问账户
        cls.user_info = outside_consultants_login_normal()
        cls.token = cls.user_info[0]
        cls.memberId = cls.user_info[1]
        cls.platform = "3"
        cls.baseUrl = "http://test-xiaoxapi.aoji.cn"

    def test_get_resource_country_list(self):  # 获取资源系统国家列表并返回国家id
        url = "/country/getResourceCountryList"
        headers = {
            "token": self.token,
            "memberId": self.memberId,
            "platform": self.platform
        }
        response = requests.get(url=self.baseUrl+url, headers=headers)
        countryId = jsonpath.jsonpath(response.json(), "$.body.resourceCountryList[*].id")
        countryName = jsonpath.jsonpath(response.json(), "$.body.resourceCountryList[*].name")

        logging.info("请求url:{0},请求头:{1}".format(url, headers))
        logging.info("国家列表数据为：", json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))
        logging.info("国家id为:{0},国家名称为:{1}".format(countryId, countryName))

        return countryId

    def test_school_hot(self):  # 获取热门院校列表，并返回院校id
        url = "/school/hot"
        headers = {
            "token": self.token,
            "memberId": self.memberId,
            "platform": self.platform,
            "countryId": str(self.test_get_resource_country_list()[0])
        }
        params = {
            "startIndex": "0",
            "pageSize": "10"
        }
        response = requests.get(url=self.baseUrl+url, headers=headers, params=params)  # get请求，请求体使用params传入参数
        schoolId = jsonpath.jsonpath(response.json(), "$.body.hotList[*].schoolId")

        logging.info("请求url:{0},请求头:{1},请求体:{2}".format(url, headers, params))
        logging.info("热门院校列表数据为：", json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))
        logging.info("热门院校列表信息为：", schoolId)

        return schoolId

    def test_get_school_member_list(self):  # 根据热门院校id，查询院校推荐顾问列表信息，并返回顾问memberId
        url = "/school/memberList"
        headers = {
            "token": self.token,
            "memberId": self.memberId,
            "platform": self.platform
        }
        params = {
            "startIndex": "0",
            "pageSize": "10",
            "schoolId": str(self.test_school_hot()[0])
        }
        response = requests.get(url=self.baseUrl+url, headers=headers, params=params)
        member_list = jsonpath.jsonpath(response.json(), "$.body.list[*].memberId")

        logging.info("请求url:{0},请求头:{1},请求体:{2}".format(url, headers, params))
        logging.info("热门院校推荐顾问信息为：", json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))
        logging.info("推荐顾问信息：", member_list)

        self.assertIn("8617", member_list)  # 断言：顾问列表中包含此顾问8617
        return member_list

    def test_get_school_member_detail(self):  # 根据顾问id查询顾问详情页信息
        url = "/member/detail"
        headers = {
            "token": self.token,
            "memberId": self.memberId,
            "platform": self.platform,
            "vcode": "21300"
        }
        params = {
            "persionMemberId": self.test_get_school_member_list()[0]
        }
        response = requests.get(url=self.baseUrl+url, headers=headers, params=params)
        logging.info("请求url:{0},请求头:{1},请求体:{2}".format(url, headers, params))
        logging.info("推荐顾问详情信息为：", json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    unittest.main()



