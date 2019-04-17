import requests
import json


# 外部顾问登录
def outside_consultants_login_normal():
    url = "http://test-xiaoxapi.aoji.cn/login/newLogin"

    data = {"type": 2,
            "acount": "13426475666",
            "password": "123456"}
    headers = {
        'platform': "3",
        'uuid': "11"
    }

    response = requests.post(url, data=data, headers=headers)
    # print(json.dumps(response.json(), ensure_ascii=False, sort_keys=False, indent=2))

    token = response.json()['body']['token']
    memberid = response.json()['body']['memberid']

    # print(token, memberid)

    return token, memberid  # 返回用户token，memberid


# 内部顾问登录
def internal_consultants_login_normal():
    url = "http://test-xiaoxapi.aoji.cn/login/newLogin"

    data = {"type": 2,
            "acount": "13021117364",
            "password": "000000"}
    headers = {
        'platform': "3",
        'uuid': "11"
    }

    response = requests.post(url, data=data, headers=headers)

    token = response.json()['body']['token']
    memberid = response.json()['body']['memberid']

    # print(token, memberid)

    return token, memberid  # 返回用户token，memberid


if __name__ == "__main__":
    outside_consultants_login_normal()
    # internal_consultants_login_normal()
