import jsonpath
import random


class login():

    def __init__(self, s):

        self.s = s

    # 外部顾问登录
    def outside_consultants_login_normal(self, uri):
        url = uri + "/login/newLogin"

        data = {"type": 2,
                "acount": "15845381735",
                "password": "123456"}
        headers = {
            'platform': "3",
            'uuid': "11"
        }

        response = self.s.post(url, data=data, headers=headers)
        # print(json.dumps(response.json(), ensure_ascii=False, sort_keys=False, indent=2))
        data = response.json()
        print("请求头信息：{}{}{}".format(url, headers, data))
        print("响应体信息：{}".format(data))

        return data  # 返回用户token，memberid


    # 内部顾问登录
    def internal_consultants_login_normal(self, uri):
        url = uri + "/login/newLogin"

        data = {"type": 2,
                "acount": "13021117364",
                "password": "000000"}
        headers = {
            'platform': "3",
            'uuid': "11"
        }

        response = self.s.post(url, data=data, headers=headers)

        token = response.json()['body']['token']
        memberid = response.json()['body']['memberid']
        # token = jsonpath.jsonpath(response.json(), "$.body.token")
        # memberId = jsonpath.jsonpath(response.json(), "$.body.memberid")
        # print(token, memberid)

        return token, memberid  # 返回用户token，memberid





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





    def test_student_add_resource(self, uri, token, memberId, platform, countryId):
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
            "countryId": countryId,
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

