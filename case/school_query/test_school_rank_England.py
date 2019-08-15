import unittest
from common.login import *
from data_file import default_data
import logging
from common.resource_country import resource_country_list
from school import *


class TestSchoolRankEngland(unittest.TestCase):

    s = requests.session()     # 创建请求会话对象
    uri = default_data.baseUrl
    platform = default_data.platform

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)   # 实例化登录对象
        aa = cls.a.outside_consultants_login(cls.uri)   # 调用外部顾问登录方法并返回用户数据
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

        # 调用国家列表接口获取国家id
        countryInfo = resource_country_list(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)
        countryIds = countryInfo[0]
        logging.info(countryIds)
        countryId= countryIds[2]  # 英国

        # 调用用户保存国家接口获取国家id
        cls.countryId = member_save_country(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, countryId)

        # 调用地区接口获取地区id
        areaIds = member_get_area_list(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, cls.countryId)
        cls.areaId = areaIds[0]

    def test_school_rank_01(self):
        '''
        测试院校排名接口
        场景1：澳洲国家下的全部院校排名
        '''
        url = "/school/rank/v2.6"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId,
            "countryId": str(self.countryId)
        }

        params = {
            "schoolType": 0,         # 学校类型,0-全部(默认值)，1-中小学,2-大学,3-语言,4-预科
            "areaId": 0,             # 全部地区
            "cooperationType": 0,    # 合作关系,0-全部(默认值)，1-独家,2-合作
            "rankType": 0,           # 排名类型，0-QS(默认),1-US NEWS, 2-TIMES, 3-Maclean
            "rankRange": 2,          # 排名区间，0-全部(默认),1：1到10, 2：11到30, 3：31到50， 4：50到100， 5：100以上
            "startIndex": "0",
            "pageSize": "10"
        }

        res = requests.get(url=self.uri + url, headers=headers, params=params)

        logging.info("请求信息为：{0}{1}{2}".format(self.uri + url, headers, params))
        logging.info("响应信息为：{}".format(res.text))

        # 断言：获取院校排名列表信息
        schoolRankList = res.json()['body']['schoolRankList']
        try:
            if schoolRankList:
                self.assertIsNotNone(schoolRankList)
                logging.info("全部院校排名信息为：")
                for i in schoolRankList:
                    logging.info(i)
            else:
                logging.info("无院校排名信息")
        except Exception as e:
            logging.error(e)

    def test_school_rank_02(self):
        '''
        测试院校排名接口
        场景2：澳洲国家下的中小学院校排名
        '''
        url = "/school/rank/v2.6"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId,
            "countryId": str(self.countryId)
        }

        params = {
            "schoolType": 1,         # 学校类型,0-全部(默认值)，1-中小学,2-大学,3-语言,4-预科
            "areaId": 0,             # 全部地区
            "cooperationType": 0,    # 合作关系,0-全部(默认值)，1-独家,2-合作
            "rankType": 0,           # 排名类型，0-QS(默认),1-US NEWS, 2-TIMES, 3-Maclean
            "rankRange": 2,          # 排名区间，0-全部(默认),1：1到10, 2：11到30, 3：31到50， 4：50到100， 5：100以上
            "startIndex": "0",
            "pageSize": "10"
        }

        res = requests.get(url=self.uri + url, headers=headers, params=params)

        logging.info("请求信息为：{0}{1}{2}".format(self.uri + url, headers, params))
        logging.info("响应信息为：{}".format(res.text))

        # 断言：获取院校排名列表信息
        schoolRankList = res.json()['body']['schoolRankList']
        try:
            if schoolRankList:
                self.assertIsNotNone(schoolRankList)
                logging.info("中小学院校排名信息为：")
                for i in schoolRankList:
                    logging.info(i)
            else:
                logging.info("无院校排名信息")
        except Exception as e:
            logging.error(e)

    def test_school_rank_03(self):
        '''
        测试院校排名接口
        场景3：澳洲国家下的大学院校排名
        '''
        url = "/school/rank/v2.6"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId,
            "countryId": str(self.countryId)
        }

        params = {
            "schoolType": 2,         # 学校类型,0-全部(默认值)，1-中小学,2-大学,3-语言,4-预科
            "areaId": 0,             # 全部地区
            "cooperationType": 0,    # 合作关系,0-全部(默认值)，1-独家,2-合作
            "rankType": 0,           # 排名类型，0-QS(默认),1-US NEWS, 2-TIMES, 3-Maclean
            "rankRange": 2,          # 排名区间，0-全部(默认),1：1到10, 2：11到30, 3：31到50， 4：50到100， 5：100以上
            "startIndex": "0",
            "pageSize": "10"
        }

        res = requests.get(url=self.uri + url, headers=headers, params=params)

        logging.info("请求信息为：{0}{1}{2}".format(self.uri + url, headers, params))
        logging.info("响应信息为：{}".format(res.text))

        # 断言：获取院校排名列表信息
        schoolRankList = res.json()['body']['schoolRankList']
        try:
            if schoolRankList:
                self.assertIsNotNone(schoolRankList)
                logging.info("大学院校排名信息为：")
                for i in schoolRankList:
                    logging.info(i)
            else:
                logging.info("无院校排名信息")
        except Exception as e:
            logging.error(e)

    def test_school_rank_04(self):
        '''
        测试院校排名接口
        场景4：澳洲国家下的语言院校排名
        '''
        url = "/school/rank/v2.6"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId,
            "countryId": str(self.countryId)
        }

        params = {
            "schoolType": 3,         # 学校类型,0-全部(默认值)，1-中小学,2-大学,3-语言,4-预科
            "areaId": 0,             # 全部地区
            "cooperationType": 0,    # 合作关系,0-全部(默认值)，1-独家,2-合作
            "rankType": 0,           # 排名类型，0-QS(默认),1-US NEWS, 2-TIMES, 3-Maclean
            "rankRange": 2,          # 排名区间，0-全部(默认),1：1到10, 2：11到30, 3：31到50， 4：50到100， 5：100以上
            "startIndex": "0",
            "pageSize": "10"
        }

        res = requests.get(url=self.uri + url, headers=headers, params=params)

        logging.info("请求信息为：{0}{1}{2}".format(self.uri + url, headers, params))
        logging.info("响应信息为：{}".format(res.text))

        # 断言：获取院校排名列表信息
        schoolRankList = res.json()['body']['schoolRankList']
        try:
            if schoolRankList:
                self.assertIsNotNone(schoolRankList)
                logging.info("语言院校排名信息为：")
                for i in schoolRankList:
                    logging.info(i)
            else:
                logging.info("无院校排名信息")
        except Exception as e:
            logging.error(e)

    def test_school_rank_05(self):
        '''
        测试院校排名接口
        场景5：澳洲国家下的预科院校排名
        '''
        url = "/school/rank/v2.6"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId,
            "countryId": str(self.countryId)
        }

        params = {
            "schoolType": 4,         # 学校类型,0-全部(默认值)，1-中小学,2-大学,3-语言,4-预科
            "areaId": 0,             # 全部地区
            "cooperationType": 0,    # 合作关系,0-全部(默认值)，1-独家,2-合作
            "rankType": 0,           # 排名类型，0-QS(默认),1-US NEWS, 2-TIMES, 3-Maclean
            "rankRange": 2,          # 排名区间，0-全部(默认),1：1到10, 2：11到30, 3：31到50， 4：50到100， 5：100以上
            "startIndex": "0",
            "pageSize": "10"
        }

        res = requests.get(url=self.uri + url, headers=headers, params=params)

        logging.info("请求信息为：{0}{1}{2}".format(self.uri + url, headers, params))
        logging.info("响应信息为：{}".format(res.text))

        # 断言：获取院校排名列表信息
        schoolRankList = res.json()['body']['schoolRankList']
        try:
            if schoolRankList:
                self.assertIsNotNone(schoolRankList)
                logging.info("预科院校排名信息为：")
                for i in schoolRankList:
                    logging.info(i)
            else:
                logging.info("无院校排名信息")
        except Exception as e:
            logging.error(e)

    def test_school_rank_06(self):
        '''
        测试院校排名接口
        场景6：澳洲国家下的全部院校排名- 独家排名
        '''
        url = "/school/rank/v2.6"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId,
            "countryId": str(self.countryId)
        }

        params = {
            "schoolType": 0,         # 学校类型,0-全部(默认值)，1-中小学,2-大学,3-语言,4-预科
            "areaId": 0,             # 全部地区
            "cooperationType": 1,    # 合作关系,0-全部(默认值)，1-独家,2-合作
            "rankType": 0,           # 排名类型，0-QS(默认),1-US NEWS, 2-TIMES, 3-Maclean
            "rankRange": 2,          # 排名区间，0-全部(默认),1：1到10, 2：11到30, 3：31到50， 4：50到100， 5：100以上
            "startIndex": "0",
            "pageSize": "10"
        }

        res = requests.get(url=self.uri + url, headers=headers, params=params)

        logging.info("请求信息为：{0}{1}{2}".format(self.uri + url, headers, params))
        logging.info("响应信息为：{}".format(res.text))

        # 断言：获取院校排名列表信息
        schoolRankList = res.json()['body']['schoolRankList']
        try:
            if schoolRankList:
                self.assertIsNotNone(schoolRankList)
                logging.info("独家院校排名信息为：")
                for i in schoolRankList:
                    logging.info(i)
            else:
                logging.info("无院校排名信息")
        except Exception as e:
            logging.error(e)

    def test_school_rank_07(self):
        '''
        测试院校排名接口
        场景7：澳洲国家下的全部院校排名 - 合作
        '''
        url = "/school/rank/v2.6"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId,
            "countryId": str(self.countryId)
        }

        params = {
            "schoolType": 0,         # 学校类型,0-全部(默认值)，1-中小学,2-大学,3-语言,4-预科
            "areaId": 0,             # 全部地区
            "cooperationType": 2,    # 合作关系,0-全部(默认值)，1-独家,2-合作
            "rankType": 0,           # 排名类型，0-QS(默认),1-US NEWS, 2-TIMES, 3-Maclean
            "rankRange": 2,          # 排名区间，0-全部(默认),1：1到10, 2：11到30, 3：31到50， 4：50到100， 5：100以上
            "startIndex": "0",
            "pageSize": "10"
        }

        res = requests.get(url=self.uri + url, headers=headers, params=params)

        logging.info("请求信息为：{0}{1}{2}".format(self.uri + url, headers, params))
        logging.info("响应信息为：{}".format(res.text))

        # 断言：获取院校排名列表信息
        schoolRankList = res.json()['body']['schoolRankList']
        try:
            if schoolRankList:
                self.assertIsNotNone(schoolRankList)
                logging.info("合作院校排名信息为：")
                for i in schoolRankList:
                    logging.info(i)
            else:
                logging.info("无院校排名信息")
        except Exception as e:
            logging.error(e)


if __name__ == "__main__":
    unittest.main()










