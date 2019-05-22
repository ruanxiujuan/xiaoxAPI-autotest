import unittest
import requests
import json
import jsonpath
import logging
from lib.login import *


class TestGetSchoolRankMemberList(unittest.TestCase):
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

    def test_school_rank(self):  # 获取院校排名列表，并返回院校id
        url = "/school/rank"
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
        schoolId = jsonpath.jsonpath(response.json(), "$.body.schoolRankList[*].schoolId")

        logging.info("请求url:{0},请求头:{1},请求体:{2}".format(url, headers, params))
        logging.info("院校排名列表数据为：", json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))
        logging.info("院校排名学校id为：", schoolId)

        return schoolId

    def test_get_school_member_list(self):  # 根据院校排名id，查询院校推荐顾问列表信息
        url = "/school/memberList"
        headers = {
            "token": self.token,
            "memberId": self.memberId,
            "platform": self.platform
        }
        params = {
            "startIndex": "0",
            "pageSize": "10",
            "schoolId": str(self.test_school_rank()[0])
        }
        response = requests.get(url=self.baseUrl+url, headers=headers, params=params)
        member_list = jsonpath.jsonpath(response.json(), "$.body.list[*].memberId")

        logging.info("请求url:{0},请求头:{1},请求体:{2}".format(url, headers, params))
        logging.info("院校排名推荐顾问信息为：", json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))
        logging.info("推荐顾问信息：", member_list)


if __name__ == "__main__":
    unittest.main()




