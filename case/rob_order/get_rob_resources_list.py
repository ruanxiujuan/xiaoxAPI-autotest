import requests
import json
from lib.login import *

# 抢单列表
def get_rob_resources_list(s, uri, token, memberid, platform):
    url = "/rob/getRobResources"

    headers = {
        "platform": platform,
        "token": token,
        "memberId": memberid
    }
    response = s.post(url=uri + url, headers=headers)
    result = response.json()
    return result







