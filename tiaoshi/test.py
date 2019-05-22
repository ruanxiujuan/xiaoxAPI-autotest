import requests
import jsonpath
import json

def test_student_list_status_0(s, token,memberId,platform,studentName,uri):  # 查询全部学生列表指定学生信息，并返回资源id
    url = "/counselor/studentsV274"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    data = {
        "studentName": studentName,
        "status": "0",  # 全部列表
        "startIndex": "0",
        "pageSize": "50"
    }
    response = s.post(url=uri + url, headers=headers, data=data)
    result = json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2)

    print("请求信息：", url, headers, data)
    print("响应信息：", result)

    return response