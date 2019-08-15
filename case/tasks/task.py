import requests
import json
import jsonpath


def test_task_type(s, uri, token, memberid, platform):
    '''
    测试任务类型接口，返回任务类型id，任务类型name
    '''
    url = "/task/type"
    headers = {
        "platform": platform,
        "token": token,
        "memberId": memberid
    }
    res = s.post(url=uri + url, headers=headers)

    print("请求信息：{0}{1}".format(uri+url, headers))
    print("响应信息：{0}".format(res.json()))

    type_list = json.dumps(res.json()['body']['list'], ensure_ascii=False, sort_keys=True, indent=2)
    print("任务类型：", type_list)

    type_id = jsonpath.jsonpath(res.json(), "$.body.list[*].id")
    type_name = jsonpath.jsonpath(res.json(), "$.body.list[*].name")

    return type_id, type_name


def test_task_list(s, uri, token, memberid, platform, countryId, taskType, taskStatus, endType):
    url = "/task/list"
    headers = {
        "platform": platform,
        "token": token,
        "memberId": memberid,
        "countryId": countryId
    }
    data = {
        "taskType": taskType,
        "taskStatus": taskStatus,
        "name": "",
        "endType": endType,
        "startIndex": 0,
        "pageSize": 10
    }
    res = requests.post(url=uri + url, headers=headers, data=data)
    # print(res.json())

    print("请求信息：{0}{1}{2}".format(uri+url, headers, data))
    print("响应信息：{0}".format(res.json()))

    task_list = res.json()['body']['list']
    try:
        if task_list and task_list is not None:
            print("任务列表为：", json.dumps(task_list, ensure_ascii=False, sort_keys=True, indent=2))
        else:
            print("无相关任务")
    except Exception as e:
        print(e)








