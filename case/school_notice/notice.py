import requests, json, jsonpath


def member_save_country(s, uri, platform, token, memberId, countryId):
    '''
    保存国家接口
    :return: 国家id
    '''
    url = "/member/saveCountry"
    headers = {
        "platform": platform,
        "token": token,
        "memberId": memberId
    }
    data = {
        "countryId": countryId
    }

    res = s.post(url=uri+url, headers=headers, data=data)
    countryId = data['countryId']

    return countryId


def get_school_by_countryId(s, uri, platform, token, memberId, countryId, type):
    '''
    根据国家id获得国家下面的院校列表
    :return: 院校id
    '''
    url = "/getSchoolByCountryId"
    headers = {
        "platform": platform,
        "token": token,
        "memberId": memberId
    }
    params = {
        "countryId": countryId,
        "type": type
    }

    res = s.get(url=uri+url, headers=headers, params=params)

    # 请求及响应信息
    print("院校通知搜索请求内容{0}{1}{2}".format(url, headers, params))
    print("响应信息为{0}".format(res.json()))

    result = res.json()
    schoolId = jsonpath.jsonpath(result, "$.body.SchoolInfoList[0].id")
    return result, schoolId


def search_school_notice(s, uri, platform, token, memberId, countryId, schoolId=0, keyword="",):
    '''
    院校通知搜索接口，返回搜索结果和通知id
    :return:
    '''
    url = "/search/schoolNotice"
    headers = {
        "platform": platform,
        "token": token,
        "memberId": memberId
    }
    params = {
        "startIndex": 0,
        "pageSize": 10,
        "schoolId": schoolId,
        "countryId": countryId,
        "keyword": keyword
    }

    res = s.get(url=uri+url, headers=headers, params=params)

    # # 请求及响应信息
    # print("院校通知搜索请求内容{0}{1}{2}".format(url, headers, params))
    # print("响应信息为{0}".format(res.json()))

    # 搜索结果及通知id
    result = res.json()['body']['result']
    noticeId = jsonpath.jsonpath(res.json(), "$.body.result[0].id")

    return result, noticeId


def school_notice_detail(s, uri, platform, token, memberId, noticeId):
    '''
    院校通知详情接口，返回搜索结果和通知id
    :return:
    '''
    url = "/school/noticeDetail"
    headers = {
        "platform": platform,
        "token": token,
        "memberId": memberId
    }
    params = {
        "noticeId": noticeId
    }

    res = s.get(url=uri + url, headers=headers, params=params)

    # 请求及响应信息
    print("院校通知详情请求内容{0}{1}{2}".format(url, headers, params))
    print("响应信息为{0}".format(res.json()))

    # 通知信息及通知内容
    content = res.json()['body']['content']
    notice = res.json()['body']['notice']

    try:
        if notice:
            print("\n院校通知信息为：", json.dumps(notice, ensure_ascii=False, sort_keys=True, indent=2), "\n通知内容为：",content)
        else:
            print("无通知信息")
    except Exception as e:
        print(e)





