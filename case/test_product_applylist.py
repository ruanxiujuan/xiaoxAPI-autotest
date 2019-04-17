import requests
from lib.login import outside_consultants_login_normal
import jsonpath
import unittest


class TestGetProductApplyList(unittest.TestCase):
    def test_get_product_apply_list(self):
        url = "http://test-xiaoxapi.aoji.cn/product/applyList"

        user_info = outside_consultants_login_normal()
        token = user_info[0]
        memberId = user_info[1]

        headers = {
            'platform': "3",
            'token': token,
            'memberId': memberId
        }

        response = requests.post(url, headers=headers)

        # print(json.dumps(response.json(), indent=2, ensure_ascii=False, sort_keys=True))

        apply_list = jsonpath.jsonpath(response.json(), '$.body.applyList[*].applyid')
        country_list = jsonpath.jsonpath(response.json(), '$.body.countryList[*].countryid')

        # 判断返回的服务类型和国家不为空
        self.assertIsNotNone(apply_list)
        self.assertIsNotNone(country_list)

        print(apply_list, country_list)

        return apply_list, country_list, token, memberId


if __name__ == "__main__":
    unittest.main(verbosity=2)

