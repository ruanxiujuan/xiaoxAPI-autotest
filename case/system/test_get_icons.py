from common.login import *
from data_file import default_data
import unittest
import json
import jsonpath


class TestGetIcons(unittest.TestCase):
    s = requests.session()
    uri = default_data.baseUrl
    platform = default_data.platform
    vcode = default_data.vcode

    @classmethod
    def setUpClass(cls):
        # 初始化会话对象
        cls.a = login(cls.s)
        # 登录用户
        aa = cls.a.outside_consultants_login(cls.uri)
        cls.token = aa['body']['token']
        cls.memberid = aa['body']['memberid']

    def test_get_icons(self):
        '''
        加载首页模块图片：
        模块包括：院校通知、院校速查、智能选校、成功案例、最近通话、推荐资源、优惠券
        2.16.0版本开始，首页不显示”优惠券“模块
        '''
        url = "/system/getIcons"
        headers = {
            "platform": self.platform,
            "token": self.token,
            "memberId": self.memberid,
            "vcode": self.vcode
        }

        # 发送请求及接收响应
        res = requests.post(url=self.uri+url, headers=headers)

        # 获取模块名称+图片URL
        list = res.json()['body']['list']
        name = jsonpath.jsonpath(res.json(), '$.body.list[*].name')
        url = jsonpath.jsonpath(res.json(), '$.body.list[*].url')


        # 断言：判断模块名称、图片不为空，打印当前模块+图片个数并遍历模块
        expect_modle = ['院校通知', '院校速查', '智能选校', '成功案例', '最近通话', '推荐资源']
        try:
            if list is not None:
                print("接口返回模块数为："+str(len(list)))
                if name is not None:
                    print("接口返回模块名称数："+str(len(name)))
                    for expect_modle in name:
                        self.assertIn(expect_modle, name)
                    if len(url) >= 6:
                        print("接口返回图片数：" + str(len(url)))
                        print("首页模块内容为："+json.dumps(res.json()['body']['list'], ensure_ascii=False, sort_keys=True, indent=2))
                else:
                    print("首页模块数据返回不符")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()




