import requests
import json
import jsonpath


def member_save_country(s, uri, token, memberId, platform, countryId):
    '''
    用户保存国家接口
    :param s:
    :param uri:
    :param token:
    :param memberId:
    :param platform:
    :return: countryId
    '''
    url = "/member/saveCountry"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    data = {
        "countryId": countryId
    }
    res = s.get(url=uri + url, headers=headers)

    countryId = data['countryId']
    return countryId


def member_get_area_list(s, uri, token, memberId,  platform, countryId):
    '''
    院校地区列表接口
    :param s:
    :param uri:
    :param platform:
    :param memberId:
    :param token:
    :param countryId:
    :return: AreaId
    '''
    url = "/member/getAreaList"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }

    params = {
        "countryId": str(countryId)
    }

    res = s.get(url=uri + url, headers=headers, params=params)

    # print("请求信息为：{0}{1}{2}".format(uri + url, headers, params))
    # print("响应信息为：{}".format(res.json()))

    # 获取地区列表信息id并返回
    AreaId = jsonpath.jsonpath(res.json(), "$.body.list[*].id")
    return AreaId


def school_major_qs(s, uri, token, memberId, platform):
    '''
    选择专业-专业大小类列表接口
    :param s:
    :param uri:
    :param token:
    :param memberId:
    :param platform:
    :return:kindIds
    '''
    url = "/school/majorQs/v2.6"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }

    res = s.get(url=uri + url, headers=headers)
    kindIds = jsonpath.jsonpath(res.json(), "$.body.majorQsResponseList[*].project[*].kindId")
    return kindIds


def school_hot(s, uri, token, memberId, platform, countryId):
    '''
    热门院校列表接口
    :param s:
    :param uri:
    :param platform:
    :param memberId:
    :param token:
    :param countryId:
    :return: schoolId
    '''
    url = "/school/hot"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform,
        "countryId": str(countryId)
    }
    params = {
        "startIndex": 0,
        "pageSize": 10
    }
    res = s.get(url=uri+url, headers=headers, params=params)

    # print("请求信息为：{0}{1}{2}".format(uri + url, headers, params))
    # print("响应信息为：{}".format(res.text))

    schoolId = jsonpath.jsonpath(res.json(), "$.body.hotList[*].schoolId")
    return schoolId


def school_rank(s, uri, token, memberId,  platform, countryId):

    url = "/school/rank/v2.6"
    headers = {
        "platform": platform,
        "token": token,
        "memberId": memberId,
        "countryId": str(countryId)
    }

    params = {
        "schoolType": 0,  # 学校类型,0-全部(默认值)，1-中小学,2-大学,3-语言,4-预科
        "areaId": 0,  # 全部地区
        "cooperationType": 0,  # 合作关系,0-全部(默认值)，1-独家,2-合作
        "rankType": 0,  # 排名类型，0-QS(默认),1-US NEWS, 2-TIMES, 3-Maclean
        "rankRange": 0,  # 排名区间，0-全部(默认),1：1到10, 2：11到30, 3：31到50， 4：50到100， 5：100以上
        "startIndex": "0",
        "pageSize": "10"
    }

    res = s.get(url=uri + url, headers=headers, params=params)

    # print("请求信息为：{0}{1}{2}".format(uri + url, headers, params))
    # print("响应信息为：{}".format(res.text))

    schoolIds = jsonpath.jsonpath(res.json(), "$.body.schoolRankList[*].schoolId")
    return schoolIds

def school_detail(s, uri, token, memberId,  platform, countryId, schoolId):
    '''
    院校详情接口
    :param s:
    :param uri:
    :param token:
    :param memberId:
    :param platform:
    :param countryId:
    :param schoolId:
    :return: memberIds  顾问memberId
    '''
    url = "/school/detail"
    headers = {
        "platform": platform,
        "token": token,
        "memberId": memberId,
        "countryId": str(countryId)
    }

    params = {
        "schoolId": schoolId
    }

    res = s.get(url=uri + url, headers=headers, params=params)
    result = json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2)

    # print("请求信息为：{0}{1}{2}".format(uri + url, headers, params))
    # print("响应信息为：{}".format(result))

    memberIds = jsonpath.jsonpath(res.json(), "$.body.memberList[*].memberId")

    return memberIds
