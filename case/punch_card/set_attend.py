import requests
import json


def test_set_attend_type(s, uri, token, memberid, platform, ClockType):
    '''
    测试打卡接口：上线打卡/离线打卡
    '''
    url = "/counselor/setAttend"
    headers = {
        "platform": platform,
        "token": token,
        "memberId": memberid
    }
    params = {
        "ClockType": ClockType   # 打卡类型0上线打卡 1离线打卡
    }
    res = s.get(url=uri + url, headers=headers, params=params)

    print("请求信息：{0}{1}{2}".format(uri + url, headers, params))
    print("响应信息：{0}".format(res.json()))

    # 断言：上线打卡成功，返回code=0,msg=上线打卡成功
    detail = res.json()['body']['detail']
    code = res.json()['body']['detail']['code']
    msg = res.json()['body']['detail']['msg']
    if detail:
        print(code, msg)
    else:
        print("无法获取到打卡详情信息")


def test_get_attend_by_id(s, uri, token, memberid, platform):
    '''
    测试获取打卡信息接口：根据用户id查询打卡信息
    '''
    url = "/counselor/getAttendById"
    headers = {
        "platform": platform,
        "token": token,
        "memberId": memberid
    }
    res = s.get(url=uri + url, headers=headers)

    print("请求信息：{0}{1}".format(uri + url, headers))
    print("响应信息：{0}".format(res.json()))

    # 断言：打卡后，可获取到打卡信息
    result = res.json()['body']['result']
    clockType = res.json()['body']['result']['clockType']
    clockTypeId = res.json()['body']['result']['clockTypeId']
    if result:
        print(clockTypeId, clockType)
    else:
        print("未获取到打卡信息")
