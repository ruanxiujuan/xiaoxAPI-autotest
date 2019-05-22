import requests
import json
import jsonpath


class login():
    def __init__(self, s):

        self.s = s

    # 外部顾问登录
    def outside_consultants_login(self, uri):
        url = uri + "/login/newLogin"

        data = {"type": 2,
                "acount": "8613021117364",
                "password": "000000"}
        headers = {
            'platform': "3",
            'uuid': "11"
        }
        response = self.s.post(url, data=data, headers=headers)
        data = response.json()
        return data  # 返回用户token，memberid

    # 内部顾问登录
    def inside_consultants_login(self, host, TYPE, IA, IP, PLATFORM, UUID ):
        url = host + "login/newLogin"
        data = {
            "type": TYPE,
            "acount": IA,
            "password": IP
        }
        headers = {
            "platform": PLATFORM,
            "uuid": UUID
        }

        response = self.s.post(url=url, headers=headers, data=data)
        result = json.dumps(response.json(), ensure_ascii=False, sort_keys=False, indent=2)
        print(result)
        token = response.json()['body']['token']
        memberid = response.json()['body']['memberid']
        return token, memberid










