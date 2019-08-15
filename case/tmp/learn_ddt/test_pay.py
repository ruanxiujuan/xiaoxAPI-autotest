import requests
import json
import jsonpath


host = "http://test-stuapi.xiaoxiedu.com"   # 请求域名
api_version = "2.0"                  # app 接口版本
platform = "2"                       # 登录移动端
phone = "13426475666"                # 手机号/账号
code_type = "1"                      # 登录
login_type = "2"                     # 验证码登录
code = "123456"                      # 验证码

# AppTypeId = "2"                      # 登录移动端
# PayTypeId = "2"                      # 支付方式：1 微信  2 支付宝
# Money = "1"                          # 支付金额（分为单位）
# pay_type = "1"                           # 合同支付为0 订单支付为1


def test_send_code():
    '''
    发送短信接口
    :return:
    '''
    url = "/sendCode"
    headers = {
        "platform": platform,
        "api-version": api_version
    }
    data = {
        "phone": phone,
        "type": code_type
    }

    res = requests.post(url=host+url, headers=headers, data=data)
    # print(res.json())


def test_valid_code():
    '''
    验证短信接口
    :return:
    '''
    url = "/validCode"
    headers = {
        "platform": platform,
        "api-version": api_version
    }
    data = {
        "phone": phone,
        "type": code_type,
        "code": code
    }

    res = requests.post(url=host + url, headers=headers, data=data)
    # print(res.json())


def test_login():
    '''
    登录接口
    :return: memberId, token
    '''
    url = "/login"
    headers = {
        "platform": platform,
        "api-version": api_version
    }
    data = {
        "account": phone,
        "type": login_type,
        "voucher": code
    }

    res = requests.post(url=host + url, headers=headers, data=data)

    # print(res.json())

    userNo = jsonpath.jsonpath(res.json(), "$.body.userNo")  # memberId
    token = jsonpath.jsonpath(res.json(), "$.body.token")    # token

    return userNo, token


def test_order_list(memberId, token):
    '''
    订单列表接口
    :param memberId:
    :param token:
    :return: ordercode
    '''
    url = "/order/list"
    headers = {
        "platform": platform,
        "api-version": api_version,
        "memberId": memberId,
        "token": token
    }
    res = requests.post(url=host+url, headers=headers)

    ordercode = jsonpath.jsonpath(res.json(), "$.body[0].ordercode")
    return ordercode


def test_pay(memberId, token, ordercode, AppTypeId, PayTypeId, Money, pay_type):
    '''
    支付接口
    :param memberId:
    :param token:
    :param ordercode:
    :return: 返回接口响应信息
    '''
    url = "/payV2"
    headers = {
        "platform": platform,
        "api-version": api_version,
        "memberId": memberId,
        "token": token
    }
    data = {
        "OrderId": ordercode,
        "AppTypeId": AppTypeId,
        "PayTypeId": PayTypeId,
        "Money": Money,
        "type": pay_type

    }

    res = requests.post(url=host+url, headers=headers, data=data)
    print(json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2))



# 方法调用
test_send_code()
test_valid_code()
test_login()
