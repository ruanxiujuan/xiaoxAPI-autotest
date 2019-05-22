import unittest
import requests
import json
import jsonpath
import logging
from lib.login import *


class TestGetSchoolDetailMemberList(unittest.TestCase):
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
        logging.info("国家列表数据为：", )
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

    def test_get_school_detail(self):   # 查询院校详情, 检查推荐顾问列表信息并返回推荐顾问列表
        url = "/school/detail"
        headers = {
            "token": self.token,
            "memberId": self.memberId,
            "platform": self.platform,
            "countryId": str(self.test_get_resource_country_list()[0])
        }
        params = {
            "schoolId": str(self.test_school_hot()[0])
        }
        response = requests.get(url=self.baseUrl+url, headers=headers, params=params)
        memberList = jsonpath.jsonpath(response.json(), "$.body.memberList")

        logging.info("请求url:{0}", "请求头:{1}", "请求体:{2}".format(url, headers, params))
        logging.info("热门院校详情数据为：", json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))

        if memberList is not None:  # 判断院校详情页是否存在推荐顾问信息
            logging.info("院校详情页推荐顾问信息为：", memberList)
        else:
            logging.info("院校详情页无推荐顾问信息")

        return memberList


if __name__ == "__main__":
    # t = TestGetSchoolMemberList()
    # t.test_get_resource_country_list()
    # t.test_school_hot()
    # t.test_get_school_detail()
    unittest.main()



