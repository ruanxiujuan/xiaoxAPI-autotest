import requests
import jsonpath

from lib.login import outside_consultants_login_normal


def get_product_list():
    url = "http://test-xiaoxapi.aoji.cn/product/productList"

    user_info = outside_consultants_login_normal()
    token = user_info[0]
    memberId = user_info[1]

    headers = {
        'platform': "3",
        'token': token,
        'memberId': memberId
    }

    response = requests.post(url,  headers=headers)

    # print(json.dumps(response.json(), indent=2, ensure_ascii=False, sort_keys=True))

    apply_list = jsonpath.jsonpath(response.json(), '$.body.applyList[*].applyid')
    country_list = jsonpath.jsonpath(response.json(), '$.body.countryList[*].countryid')

    print(apply_list, country_list)

    return apply_list, country_list, token, memberId


if __name__ == "__main__":
    pass


