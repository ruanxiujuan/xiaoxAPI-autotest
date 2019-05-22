import json
import requests


baseUrl = "http://test-xiaoxapi.aoji.cn"

def login():
    url = baseUrl + "/login/newLogin"

    data = {"type": 2,
            "acount": "13426475666",
            "password": "123456"}
    headers = {
        'platform': "3",
        'uuid': "11"
    }

    response = requests.post(url=baseUrl+url, data=data, headers=headers)
    print(json.dumps(response.json(), ensure_ascii=False, sort_keys=False, indent=2))


login()
