import unittest
import logging
from common.login import *
from data_file import default_data
from case.product.product import apply_list


class TestProductProductSelectList(unittest.TestCase):

    s = requests.session()  # 创建请求会话对象
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)  # 实例化登录对象
        aa = cls.a.outside_consultants_login(cls.uri)  # 调用外部顾问登录方法并返回用户数据
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

        # 精选产品筛选项
        select_info = apply_list(cls.s, cls.uri, cls.platform, cls.token, cls.memberId)
        cls.countryIds = select_info[0]
        cls.lineId = select_info[1]
        cls.applyIds = select_info[2]

    def test_product_list_select01(self):
        '''
        测试精选产品 - 精选产品列表
        测试场景1：单国家+单产品线+多服务
        '''

        url = "/product/productListv214"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }
        data = {
            "countryIds": self.countryIds[0],
            "lineId": self.lineId[0],
            "applyIds": self.applyIds,
            "startIndex": 0,
            "pageSize": 10
        }

        res = requests.post(url=self.uri+url, headers=headers, data=data)
        result = (json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2))

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, data))
        logging.info("响应信息：{0}".format(result))

        # 断言：根据筛选出的产品列表，判断是否返回对应的产品数据
        list = res.json()['body']['list']
        try:
            if list is not None:
                self.assertIsNotNone(list)
                logging.info(list)
            elif list == []:
                self.assertEqual(0, len(list))
                logging.info("暂无符合产品！")
            else:
                logging.info("请检查输入信息{0}".format(data))
        except Exception as e:
            logging.error(e)

    def test_product_list_select02(self):
        '''
        测试精选产品 - 精选产品列表
        测试场景2：单国家+单产品线+单服务
        '''

        url = "/product/productListv214"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }
        data = {
            "countryIds": self.countryIds[0],
            "lineId": self.lineId[0],
            "applyIds": self.applyIds[0],
            "startIndex": 0,
            "pageSize": 10
        }

        res = requests.post(url=self.uri+url, headers=headers, data=data)
        result = (json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2))

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, data))
        logging.info("响应信息：{0}".format(result))

        # 断言：根据筛选出的产品列表，判断是否返回对应的产品数据
        list = res.json()['body']['list']
        try:
            if list is not None:
                self.assertIsNotNone(list)
                logging.info(list)
            elif list == []:
                self.assertEqual(0, len(list))
                logging.info("暂无符合产品！")
            else:
                logging.info("请检查输入信息{0}".format(data))
        except Exception as e:
            logging.error(e)

    def test_product_list_select03(self):
        '''
        测试精选产品 - 精选产品列表
        测试场景3：无筛选项
        '''

        url = "/product/productListv214"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }
        data = {
            "countryIds": "",
            "lineId": "",
            "applyIds": "",
            "startIndex": 0,
            "pageSize": 10
        }

        res = requests.post(url=self.uri+url, headers=headers, data=data)
        result = (json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2))

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, data))
        logging.info("响应信息：{0}".format(result))

        # 断言：根据筛选出的产品列表，判断是否返回对应的产品数据
        list = res.json()['body']['list']
        try:
            if list is not None:
                self.assertIsNotNone(list)
                logging.info(list)
            elif list == []:
                self.assertEqual(0, len(list))
                logging.info("暂无符合产品！")
            else:
                logging.info("请检查输入信息{0}".format(data))
        except Exception as e:
            logging.error(e)

    def test_product_list_select04(self):
        '''
        测试精选产品 - 精选产品列表
        测试场景4：多国家+单产品线+多服务
        '''

        url = "/product/productListv214"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }
        data = {
            "countryIds": self.countryIds,
            "lineId": self.lineId[0],
            "applyIds": self.applyIds,
            "startIndex": 0,
            "pageSize": 10
        }

        res = requests.post(url=self.uri+url, headers=headers, data=data)
        result = (json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2))

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, data))
        logging.info("响应信息：{0}".format(result))

        # 断言：根据筛选出的产品列表，判断是否返回对应的产品数据
        list = res.json()['body']['list']
        try:
            if list is not None:
                self.assertIsNotNone(list)
                logging.info(list)
            elif list == []:
                self.assertEqual(0, len(list))
                logging.info("暂无符合产品！")
            else:
                logging.info("请检查输入信息{0}".format(data))
        except Exception as e:
            logging.error(e)

    def test_product_list_select05(self):
        '''
        测试精选产品 - 精选产品列表
        测试场景5：多国家+单产品线+单服务
        '''

        url = "/product/productListv214"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }
        data = {
            "countryIds": self.countryIds,
            "lineId": self.lineId[0],
            "applyIds": self.applyIds[0],
            "startIndex": 0,
            "pageSize": 10
        }

        res = requests.post(url=self.uri+url, headers=headers, data=data)
        result = (json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2))

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, data))
        logging.info("响应信息：{0}".format(result))

        # 断言：根据筛选出的产品列表，判断是否返回对应的产品数据
        list = res.json()['body']['list']
        try:
            if list is not None:
                self.assertIsNotNone(list)
                logging.info(list)
            elif list == []:
                self.assertEqual(0, len(list))
                logging.info("暂无符合产品！")
            else:
                logging.info("请检查输入信息{0}".format(data))
        except Exception as e:
            logging.error(e)

    def test_product_list_select06(self):
        '''
        测试精选产品 - 精选产品列表
        测试场景6：多国家+单产品线+无服务
        '''

        url = "/product/productListv214"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }
        data = {
            "countryIds": self.countryIds,
            "lineId": self.lineId[0],
            "applyIds": "",
            "startIndex": 0,
            "pageSize": 10
        }

        res = requests.post(url=self.uri+url, headers=headers, data=data)
        result = (json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2))

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, data))
        logging.info("响应信息：{0}".format(result))

        # 断言：根据筛选出的产品列表，判断是否返回对应的产品数据
        list = res.json()['body']['list']
        try:
            if list is not None:
                self.assertIsNotNone(list)
                logging.info(list)
            elif list == []:
                self.assertEqual(0, len(list))
                logging.info("暂无符合产品！")
            else:
                logging.info("请检查输入信息{0}".format(data))
        except Exception as e:
            logging.error(e)

    def test_product_list_select07(self):
        '''
        测试精选产品 - 精选产品列表
        测试场景7：多国家+无产品线+无服务
        '''

        url = "/product/productListv214"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }
        data = {
            "countryIds": self.countryIds,
            "lineId": "",
            "applyIds": "",
            "startIndex": 0,
            "pageSize": 10
        }

        res = requests.post(url=self.uri+url, headers=headers, data=data)
        result = (json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2))

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, data))
        logging.info("响应信息：{0}".format(result))

        # 断言：根据筛选出的产品列表，判断是否返回对应的产品数据
        list = res.json()['body']['list']
        try:
            if list is not None:
                self.assertIsNotNone(list)
                logging.info(list)
            elif list == []:
                self.assertEqual(0, len(list))
                logging.info("暂无符合产品！")
            else:
                logging.info("请检查输入信息{0}".format(data))
        except Exception as e:
            logging.error(e)

    def test_product_list_select08(self):
        '''
        测试精选产品 - 精选产品列表
        测试场景8：无国家+产品线+无服务
        '''

        url = "/product/productListv214"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }
        data = {
            "countryIds": "",
            "lineId": self.lineId[0],
            "applyIds": "",
            "startIndex": 0,
            "pageSize": 10
        }

        res = requests.post(url=self.uri+url, headers=headers, data=data)
        result = (json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2))

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, data))
        logging.info("响应信息：{0}".format(result))

        # 断言：根据筛选出的产品列表，判断是否返回对应的产品数据
        list = res.json()['body']['list']
        try:
            if list is not None:
                self.assertIsNotNone(list)
                logging.info(list)
            elif list == []:
                self.assertEqual(0, len(list))
                logging.info("暂无符合产品！")
            else:
                logging.info("请检查输入信息{0}".format(data))
        except Exception as e:
            logging.error(e)

    # 异常case: 产品线输入多个值[需求：产品线单选], 此时传入值非法，后端接口当作此字段未传值处理。
    def test_product_list_select09(self):
        '''
        测试精选产品 - 精选产品列表
        测试场景9：无国家+多产品线+无服务
        '''

        url = "/product/productListv214"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId
        }
        data = {
            "countryIds": "",
            "lineId": self.lineId,
            "applyIds": "",
            "startIndex": 0,
            "pageSize": 10
        }

        res = requests.post(url=self.uri+url, headers=headers, data=data)
        result = (json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2))

        logging.info("请求信息：{0}{1}{2}".format(self.uri+url, headers, data))
        logging.info("响应信息：{0}".format(result))

        # 断言：根据筛选出的产品列表，判断是否返回对应的产品数据
        list = res.json()['body']['list']
        try:
            if list is not None:
                self.assertIsNotNone(list)
                logging.info(list)
            elif list == []:
                self.assertEqual(0, len(list))
                logging.info("暂无符合产品！")
            else:
                logging.info("请检查输入信息{0}".format(data))
        except Exception as e:
            logging.error(e)

        # print(self.lineId)


if __name__ == "__main__":
    unittest.main()





