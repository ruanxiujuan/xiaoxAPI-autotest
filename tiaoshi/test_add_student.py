import random, jsonpath

import urllib3
urllib3.disable_warnings()

class TestStudentAddResource():

    def __init__(self, s):
        self.s = s

    def test_get_resource_country_list(self, uri, token, memberId, platform):  # 获取资源系统国家列表并返回国家id
        url = "/country/getResourceCountryList"
        headers = {
            "token": token,
            "memberId": memberId,
            "platform": platform
        }
        response = self.s.get(url=uri+url, headers=headers)

        countryId = jsonpath.jsonpath(response.json(), "$.body.resourceCountryList[*].id")
        countryName = jsonpath.jsonpath(response.json(), "$.body.resourceCountryList[*].name")
        # print(countryId)

        return countryId

    def test_student_add_resource(self, uri, token, memberId, platform):
        url = "/counselor/addResource"
        headers = {
            "token": token,
            "memberId": memberId,
            "platform": platform,
            "vcode": "21300"
        }
        data = {
            "resourceType": "1",   #  资源类型(0:名片，1:资源)
            "studentName": "autotest{0}".format(random.randint(1, 100)),
            "tel": "130{0}".format(random.randint(11110001, 11119999)),
            "countryId": self.test_get_resource_country_list()[0],
            "remark": "自动化测试脚本添加"
        }
        response = self.s.post(url=uri+url, headers=headers, data=data)

        studentName = data['studentName']
        token = headers['token']
        memberId = headers['memberId']
        platform = headers['platform']
        info = []
        info.append(studentName)
        info.append(token)
        info.append(memberId)
        info.append(platform)
        # print(info)

        return info

