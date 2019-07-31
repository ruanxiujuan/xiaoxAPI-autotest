import requests
import json
import jsonpath


def resource_country_list(s, uri, token, memberId, platform):
    '''
    资源系统的留学国家接口
    :param s:
    :param uri:
    :param token:
    :param memberId:
    :param platform:
    :return:countryId, countryName
    '''
    url = "/country/getResourceCountryList"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    res = s.get(url=uri + url, headers=headers)

    countryId = jsonpath.jsonpath(res.json(), "$.body.resourceCountryList[*].id")
    countryName = jsonpath.jsonpath(res.json(), "$.body.resourceCountryList[*].name")
    # print(countryId)
    return countryId, countryName







