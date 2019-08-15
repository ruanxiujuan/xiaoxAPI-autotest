import random
import urllib3
import jsonpath
import requests
import json
import time
from common.resource_country import resource_country_list
urllib3.disable_warnings()


    # 我的学生-录学生
def test_student_add_resource(s, uri, token, memberId, platform):
    url = "/counselor/addResource"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform,
        "vcode": "21300"
    }
    data = {
        "resourceType": "1",  # 资源类型(0:名片，1:资源)
        "studentName": "autotest{0}".format(random.randint(1, 100)),
        "tel": "130{0}".format(random.randint(11110001, 11119999)),
        "countryId": resource_country_list(s, uri, token, memberId, platform)[0],
        "remark": "自动化测试脚本添加"
    }
    response = s.post(url=uri + url, headers=headers, data=data)
    studentName = data['studentName']
    return studentName


    # 查询全部学生列表指定学生信息，并返回资源id
def test_student_list_status_0(s, uri, token, memberId, platform):
    url = "/counselor/studentsV274"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    data = {
        "studentName": "",
        "status": "0",  # 全部列表
        "startIndex": "0",
        "pageSize": "10"
    }
    response = s.post(url=uri + url, headers=headers, data=data)
    resourceId = jsonpath.jsonpath(response.json(), "$.body.list[0].resourceId")
    studentName = jsonpath.jsonpath(response.json(), "$.body.list[0].resourceName")
    return resourceId, studentName


    # 查询学生详情页，并返回资源id
def test_student_detail_info_type(s, uri, token, memberId, platform, resourceId):
    url = "/counselor/Student/detailInfo"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    data = {
        "resourceId": resourceId,
        "type": "1"  # 资源类别 1资源阶段，2潜在阶段，3已签约(待定校、待申请、待签证、结案)
    }
    response = s.post(url=uri + url, headers=headers, data=data)
    resourceid = jsonpath.jsonpath(response.json(), "$.body.detail.resourceid")
    return resourceid


def add_visit(s, uri, token, memberId, platform, resourceId, remark, callType, type, stage):
    '''
    添加回访接口
    :return:
    '''
    url = "/counselor/addVisit"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    data = {
        "resourceId": resourceId,
        "remark": remark,
        "callType": callType,
        "type": type,
        "stage": stage,
        "sessionid": "",
        "anserseconds": "",
        "abandonReason": ""   # 1、3天*每天3次电话均无人接听2、客户明确告知没有留学意向3、资源出现错号、空号等情况4、已签约小希平台5、已签约其他公司6、无法提供咨询服务7、其他
    }

    res = s.post(url=uri+url, headers=headers, data=data)

    print("添加回访内容为{0}{1}{2}".format(url, headers, data))
    print("添加结果为{0}".format(res.json()))


def visit_list(s, uri, token, memberId, platform, resourceId, type):
    '''
            回访记录接口
            :return:
            '''
    url = "/counselor/Student/ReturnVisitList"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    data = {
        "resourceId": resourceId,
        "type": type,
        "startIndex": 0,
        "pageSize": 10
    }

    res = s.post(url=uri + url, headers=headers, data=data)

    print("请求内容{0}{1}{2}".format(url, headers, data))
    print("回访列表为{0}".format(res.json()))


def get_student_detail_sms_template_list(s, uri, token, memberId, platform):
    '''
    学生详情页，短信模板接口
    :return: templateCode
    '''
    url = "/message/getStudentDetailSmsTemplateList"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform}

    res = s.post(url=uri+url, headers=headers)

    # print("短信模板请求内容{0}{1}".format(url, headers))
    # print("响应信息为{0}".format(json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2)))

    templateList = res.json()['body']['data']
    templateCode = jsonpath.jsonpath(res.json(), "$.body.data[*].template_code")

    return templateList, templateCode


def send_sms(s, uri, token, memberId, platform, templateCode):
    '''
    发送短信接口
    :return: 响应code,响应信息message
    '''
    url = "/message/sendSms"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    data = {
        "templateCode": templateCode,
        "receiver": "13021117364",
        "paramJson": '{"advisernum": "18514082536", "xxadviser": "小娟"}'
    }
    res = s.post(url=uri+url, headers=headers, data=data)

    print("发送短信请求内容{0}{1}{2}".format(url, headers, data))
    print("响应信息为{0}".format(res.json()))

    code = res.json()['body']['code']
    message = res.json()['body']['message']

    return code, message


def invitation_add(s, uri, token, memberId, platform, resourceId, visitor, receiver):
    '''
    添加邀约来访接口
    :return:返回生成的visitId
    '''
    url = "/counselor/invitationAdd"
    # 获取当前时间
    localtime = time.localtime(time.time())
    invitationTime = time.strftime("%Y/%m/%d %H:%M", localtime)  # 格式化时间格式为：2019/08/09 16:03

    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    data = {
        "resourceId": resourceId,
        "visitor": visitor,
        "receiver": receiver,
        "invitationTime": str(invitationTime),
        "address": "北京市西城区灯市口",
        "tel": 147258369,
        "remark": "自动化测试邀约来访啦啦啦"
    }
    res = s.post(url=uri+url, headers=headers, data=data)

    print("添加邀约来访请求内容{0}{1}{2}".format(url, headers, data))
    print("响应信息为{0}".format(res.json()))

    visitId = res.json()['body']['visitId']

    return visitId


def get_invitations(s, uri, token, memberId, platform, resourceId):
    '''
    邀约来访列表接口
    :return:返回邀约来访列表数据
    '''
    url = "/counselor/getInvitations"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    data = {
        "resourceId": resourceId,
        "startIndex": 0,
        "pageSize": 10
    }
    res = s.post(url=uri+url, headers=headers, data=data)

    print("邀约来访列表请求内容{0}{1}{2}".format(url, headers, data))
    print("响应信息为{0}".format(res.json()))

    list = res.json()['body']['list']

    return list


def test_get_school_by_country_id(s, uri, countryId):
    '''
        留学规划方案——添加选校建议系列接口
        1. 请求资源系统留学国家列表---见第一个方法
        2. 根据国家id选择目标院校接口
        3. 根据院校id选择专业接口
        4. 根据以上三个接口返回的信息生成选校建议
        '''
    url = "/getSchoolByCountryId"
    params = {
        "countryId": str(countryId),
        "type": "1"   # 类型 1-表示资源系统国家id
    }
    response = s.get(url=uri + url, params=params)
    schoolId = jsonpath.jsonpath(response.json(), "$.body.SchoolInfoList[*].id")
    schoolName = jsonpath.jsonpath(response.json(), "$.body.SchoolInfoList[*].name")

    return schoolId, schoolName


def test_get_major_by_school_id(s, uri, token, memberId, platform, schoolId):
    url = "/getMajorBySchoolId"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    data = {
        "schoolId": schoolId
    }
    response = s.post(url=uri + url, headers=headers, data=data)
    majorId = jsonpath.jsonpath(response.json(), "$.body.list[*].id")
    majorName = jsonpath.jsonpath(response.json(), "$.body.list[*].name")

    return majorId, majorName

#
def test_oversea_program_update_school_selection(s, uri, token, memberId, platform, countryId, countryName, schoolId, schoolName, resourceId):
    url = "/overseaProgram/updateSchoolSelection"
    headers = {
        "platform": platform,
        "token": token,
        "memberId": memberId
    }
    data = {
        "chooseId": "0",  # 选校建议编号:新增传0,修改传id值
        "countryId": countryId,
        "countryName": countryName,
        "schoolId": schoolId,
        "schoolName": schoolName,
        # "majorId": self.majorId,
        # "majorName": self.majorName,
        "remark": "the school selection create by autotest!",
        "resourceId": resourceId,
        "schemeId": "0",  # 方案编号:新增传0,修改传id值
    }
    response = s.post(url=uri + url, headers=headers, data=data)
    chooseId = jsonpath.jsonpath(response.json(), "$.body.data_file.chooseid")
    schemeId = jsonpath.jsonpath(response.json(), "$.body.data_file.schemeid")
    return (chooseId, schemeId)


def test_student_update_oversea_program(s, uri, token, memberId, platform, resourceid):
    url = "/overseaProgram/updateOverseaProgramName"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    data = {
        "resourceId": resourceid,
        "schemeId": "0",  # 方案编号:新增传0,修改传id值
        "name": "自动化测试新增{}的留学规划方案".format(resourceid)
    }
    response = s.post(url=uri + url, headers=headers, data=data)
    resourceid = data['resourceId']

    return resourceid


def oversea_program_list(s, uri, token, memberId, platform, resourceId):
    url = "/overseaProgram/list"
    headers = {
        "token": token,
        "memberId": memberId,
        "platform": platform
    }
    data = {
        "resourceId": resourceId,
        "startIndex": "0",
        "pageSize": "10"
    }
    response = s.post(url=uri + url, headers=headers, data=data)
    schemeId = jsonpath.jsonpath(response.json(), "$.body.list[0].id")
    schemeMemberId = jsonpath.jsonpath(response.json(), "$.body.list[0].memberid")

    return resourceId, schemeId, schemeMemberId


def test_oversea_program_detail(s, uri, token, memberid, platform, resourceId, schemeId, schemeMemberId):
    url = "/overseaProgram/detail"
    headers = {
        "token": token,
        "memberId": memberid,
        "platform": platform
    }
    data = {
        "resourceId": resourceId,
        "schemeId": schemeId,
        "schemeMemberId": schemeMemberId
    }
    response = requests.post(url=uri + url, headers=headers, data=data)
    chooseId = jsonpath.jsonpath(response.json(), "$.body.detail.selectionList[0].id")
    r = jsonpath.jsonpath(response.json(), "$.body.detail.r")
    return resourceId, schemeId, r, chooseId
























