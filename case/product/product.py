import requests
import jsonpath
import json


def apply_list_default(s, uri, platform, token, memberId):
    '''
    精选产品 - 筛选接口
    :param s:
    :param uri:
    :param platform:
    :param token:
    :param memberId:
    :return: defaultCountryId、defaultLineId、defaultApplyId
    '''

    url = "/product/applyListV214"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }

    res = s.post(url=uri+url, headers=headers)

    # 默认国家、产品线、服务为“澳洲(65)+留学(1)+全程服务(1)
    defaultCountryId = jsonpath.jsonpath(res.json(), "$.body.defaultCountryId[0]")  # 默认国家id
    defaultLineId = jsonpath.jsonpath(res.json(), "$.body.defaultLineId[0]")  # 默认产品线id
    defaultApplyId = jsonpath.jsonpath(res.json(), "$.body.defaultApplyId[0]")  # 默认服务id

    return defaultCountryId, defaultLineId, defaultApplyId


def apply_list(s, uri, platform, token, memberId):
    '''
    精选产品 - 筛选接口
    :param s:
    :param uri:
    :param platform:
    :param token:
    :param memberId:
    :return: countryList、lineIds、applyid
    '''

    url = "/product/applyListV214"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }

    res = s.post(url=uri+url, headers=headers)

    # 产品线与服务是一对多关系
    countryList = jsonpath.jsonpath(res.json(), "$.body.countryList[*].countryid")  # 国家列表
    lineIds = jsonpath.jsonpath(res.json(), "$.body.diclines[*].lineId")  # 产品线表
    # lineName = jsonpath.jsonpath(res.json(), "$.body.diclines[*].lineName")  # 产品线名称
    # services = jsonpath.jsonpath(res.json(), "$.body.diclines[*].services")  # 产品对应服务
    applyids = jsonpath.jsonpath(res.json(), "$.body.diclines[*].services[0].applyid")  # 服务id

    return countryList, lineIds,  applyids


def product_list_default(s, uri, platform, token, memberId, countryIds, lineId, applyIds):
    '''
    精选产品列表接口
    :param s:
    :param uri:
    :param platform:
    :param token:
    :param memberId:
    :param countryIds:
    :param lineId:
    :param applyIds:
    :return: productCode
    '''

    url = "/product/productListv214"
    headers = {
        "platform": platform,
        "token": token,
        "memberId": memberId
    }
    data = {
        "countryIds": countryIds,
        "lineId": lineId,
        "applyIds": applyIds,
        "startIndex": 0,
        "pageSize": 10
    }

    res = s.post(url=uri + url, headers=headers, data=data)

    productCode = jsonpath.jsonpath(res.json(), "$.body.list[*].productCode")

    return productCode






