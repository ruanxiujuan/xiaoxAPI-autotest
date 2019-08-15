import unittest
from common.login import *
from data_file import default_data
import logging
from common.resource_country import resource_country_list
from school import *


class TestSchoolTrainList(unittest.TestCase):

    s = requests.session()     # 创建请求会话对象
    uri = default_data.baseUrl
    platform = default_data.platform
    vcode = default_data.vcode

    @classmethod
    def setUpClass(cls):
        cls.a = login(cls.s)  # 实例化登录对象
        aa = cls.a.outside_consultants_login(cls.uri)  # 调用外部顾问登录方法并返回用户数据
        cls.token = aa['body']['token']
        cls.memberId = aa['body']['memberid']

        # 调用国家列表接口获取国家id
        countryInfo = resource_country_list(cls.s, cls.uri, cls.token, cls.memberId, cls.platform)
        countryIds = countryInfo[0]
        countryId = countryIds[1]  # 澳洲

        # 调用用户保存国家接口获取国家id
        cls.countryId = member_save_country(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, countryId)

        # 调用热门院校接口获取院校id
        schoolIds = school_rank(cls.s, cls.uri, cls.token, cls.memberId, cls.platform, countryId)
        cls.schoolId = schoolIds[0]


    def test_school_train_list(self):
        '''
        测试热门院校接口
        '''
        url = "/school/train"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberId,
            "countryId": str(self.countryId)
        }

        params = {
            "schoolId": self.schoolId,
            "startIndex": 0,
            "pageSize": 10,
            "category": 1     # 视频分类，1-院校培训，2-个人视频 不传则系统默认为1
        }

        res = requests.get(url=self.uri+url, headers=headers, params=params)

        logging.info("请求信息为：{0}{1}{2}".format(self.uri + url, headers, params))
        logging.info("响应信息为：{}".format(res.json()))

        # 断言：获取院校培训列表信息并判断是否存在，存在则打印
        try:
            trainList = res.json()['body']['trainList']
            if list:
                logging.info("院校详情院校培训列表信息~")
                logging.info(json.dumps(trainList, ensure_ascii=False, sort_keys=True, indent=2))
            else:
                logging.info("无院校院校培训列表信息~")
        except Exception as e:
            logging.error(e)


if __name__ == "__main__":
    unittest.main()










