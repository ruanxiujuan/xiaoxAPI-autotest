import requests
import json
import jsonpath


def get_res_ext_info(s, uri, token, memberId, platform, resourceId, sourceType):
    '''
    根据资源号查询手机号和资源姓名
    :param s:
    :param token:
    :param memberId:
    :param platform:
    :param resourceId:
    :param sourceType:
    :return:
    '''
    url = "/counselor/getResExtInfo"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    data = {
        "resourceId": resourceId,
        "sourceType": sourceType
    }
    res = s.post(url=uri+url, headers=headers, data=data)

    # 返回资源电话
    mobile = jsonpath.jsonpath(res.json(), "$.body.data.mobile")

    # 判断是否有电话
    try:
        if mobile:
            print("资源电话号为：", mobile)
        else:
            print("无电话号！")
    except Exception as e:
        print(e)

    return mobile


def ax_onlince_call(s, uri, token, memberId, platform, resourceId, callNumber, source):
    '''
    查询AX隐私号接口，返回AX号
    :param s:
    :param uri:
    :param token:
    :param memberId:
    :param platform:
    :param resourceId:
    :param callNumber:
    :param source:
    :return: AX
    '''
    url = "/counselor/ax/onLinceCall"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    data = {
        "resourceId": resourceId,
        "callNumber": callNumber,
        "source": source
    }

    res = s.post(url=uri + url, headers=headers, data=data)

    # 返回AX隐私号
    AX = res.json()['body']['telx']

    # 判断返回是否包含隐私号
    try:
        if AX is not None:
            print('隐私号为：', AX)
        else:
            print("未绑定AX号")
    except Exception as e:
        print(e)



