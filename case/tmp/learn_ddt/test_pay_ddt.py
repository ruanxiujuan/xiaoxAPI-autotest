import unittest
from ddt import ddt, data, unpack
from tmp.learn_ddt.test_pay import *


@ddt
class TestPay(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        test_send_code()                     # 发送短信
        test_valid_code()                    # 验证短信验证码
        loging_info = test_login()           # 验证码登录

        usrId = loging_info[0]            # memberId
        cls.memberId = usrId[0]
        Token = loging_info[1]           # token
        cls.token = Token[0]

        cls.ordercode = test_order_list(cls.memberId, cls.token)

    '''
    支付信息：
     AppTypeId = "2"                      # 登录移动端：1 安卓 2 IOS
     PayTypeId = "2"                      # 支付方式：1 微信  2 支付宝
     Money = "1"                          # 支付金额（分为单位）订单剩余金额为1000元
     pay_type = "1"                       # 合同支付为0 订单支付为1
    '''

# 场景1：支付宝支付-订单类型  --- 有效
    @data(
          (1, 2, 1, 1),     # 安卓登录-支付宝支付-1分钱-订单类型
          (2, 2, 1, 1)      # IOS登录-支付宝支付-1分钱-订单类型
          )
    @unpack
    def test_payV2_by_zhifubao_dingdan(self, AppTypeId, PayTypeId, Money, pay_type):
        test_pay(self.memberId, self.token, self.ordercode, AppTypeId, PayTypeId, Money, pay_type)

# 场景2：支付宝支付-合同    ---  无效（订单类型不匹配）
    @data(
          (1, 2, 1, 0),     # 安卓登录-支付宝支付-1分钱-合同类型
          (2, 2, 1, 0)      # IOS登录-支付宝支付-1分钱-合同类型
          )
    @unpack
    def test_payV2_by_zhifubao_hetong(self, AppTypeId, PayTypeId, Money, pay_type):
        test_pay(self.memberId, self.token, self.ordercode, AppTypeId, PayTypeId, Money, pay_type)

# 场景3：微信支付-订单类型    --- 无效（不支持微信支付）
    @data(
          (1, 1, 1, 1),     # 安卓登录-微信支付-1分钱-订单类型
          (2, 1, 1, 1)      # IOS登录-微信支付-1分钱-订单类型
          )
    @unpack
    def test_payV2_by_wechat_dingdan(self, AppTypeId, PayTypeId, Money, pay_type):
        test_pay(self.memberId, self.token, self.ordercode, AppTypeId, PayTypeId, Money, pay_type)

# 场景4：微信支付-合同类型   --- 无效 （不支持微信支付）
    @data(
          (1, 1, 1, 0),     # 安卓登录-微信支付-1分钱-合同类型
          (2, 1, 1, 0)      # IOS登录-微信支付-1分钱-合同类型
          )
    @unpack
    def test_payV2_by_wechat_hetong(self, AppTypeId, PayTypeId, Money, pay_type):
        test_pay(self.memberId, self.token, self.ordercode, AppTypeId, PayTypeId, Money, pay_type)

# 场景5：支付宝-订单-支付全部/重复支付
    @data((1, 2, 100000, 1),
          (1, 2, 100000, 1))
    @unpack
    def test_payV2_by_wechat_daer(self, AppTypeId, PayTypeId, Money, pay_type):
        test_pay(self.memberId, self.token, self.ordercode, AppTypeId, PayTypeId, Money, pay_type)


if __name__ == "__main__":
    unittest.main()




