import requests
import random


def login(s, host, platform, uuid, type, acount, password):
    url = "/login/newLogin"
    header = {
        "platform": platform[2],
        "uuid": uuid
    }
    data = {
        "type": type[1],
        "acount": acount,
        "password": password
    }

    res = s.post(url=host+url, header=header, data=data)
    print(res.json())


host = "http://test-xiaoxapi.aoji.cn"
platform = [1, 2, 3, 4]               # 平台，1-web,2-android,3-IOS,4-dingtalk
uuid = random.randint(1, 999)
type = [1, 2, 3, 4]                   # 登录类型1-手机验证码登录，2-手机密码登录，3-邮箱密码登录，4-集团帐号登录
acount = "13426475666"
password = "123456"
s = requests.session()

print(uuid)
login(s, host, platform, uuid, type, acount, password)