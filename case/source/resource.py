import requests
import json
import time
import random


# 录名片
def add_resource(s, uri, vcode, platform, token, memberId, resourceType, countryId):
    url = "/counselor/addResource"
    now = time.strftime("%y%m%d", time.localtime(time.time()))   # 标注当前录入时间
    tel = "131"+str(now)+str(random.randint(10, 99))
    headers = {
        "vcode": vcode,
        "platform": platform,
        "token": token,
        "memberId": memberId
    }
    data = {
        "resourceType": resourceType,
        "studentName": "自动化"+str(now),
        "tel": tel,
        "countryId": countryId,
        "remark": "自动化测试录资源~"
    }

    res = s.post(url=uri+url, headers=headers, data=data)

    print("请求参数{0}{1}{2}".format(url, headers, data))
    print("响应结果{0}".format(json.dumps(res.json(),ensure_ascii=False, sort_keys=True, indent=2)))

    code = res.json()['body']['code']
    message = res.json()['body']['message']

    return code, message


# 名片列表
def carts(s, uri, vcode, platform, token, memberId):
    url = "/counselor/carts"
    headers = {
        "vcode": vcode,
        "platform": platform,
        "token": token,
        "memberId": memberId
    }
    data = {
        "startIndex": 0,
        "pageSize": 10
    }

    res = s.post(url=uri+url, headers=headers, data=data)

    print("请求参数{0}{1}{2}".format(url, headers, data))
    print("响应结果{0}".format(res.json()))

    # 名片列表
    list = res.json()['body']['list']

    return list







