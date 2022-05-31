# coding=utf-8
import json
import os
from app import app, db
from . import case_page
from flask import request, redirect, g, jsonify, make_response
from common.libs import helper, UrlManager
from common.models.supplier import Supplier
from common.models.suppliercase import SupplierCase
from common.models.coordination import Coordination
from common.models.coordinationcase import CoordinationCase
from common.models.reportInfo import ReportInfo
from common.models.system_info import SystemInfo
from common.models.func_info import FuncInfo
from common.models.CaseGroup import CaseGroup
from common.models.auth_map import AuthMap
from common.RetJson import RetJson
from common.libs.helper import ops_render
from interceptors.Auth import check_login
from common.libs.requery import requery
from testmain import run
from testmain import runway
from sqlalchemy.sql import and_
from exeCase.configPytest import RunPyTest
import multiprocessing
import requests
import jmespath
import datetime
import time


header = header = {'contenType':'application/json',
                   'cookie':'uc_token=e957c609b1554018ae97fe1dc86e9cf1'}


@case_page.route("/case_list", methods=["GET", "POST"])
def case_list():
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')
    req = request.values
    pjnames = req['pjname'] if 'pjname' in req else ""
    address = req['pjname'] if 'pjname' in req else ""
    querys = Coordination.query
    data_list = querys.all()
    return ops_render('case/case_list.html', {"data": data_list})

@case_page.route("/create_json", methods=["GET", "POST"])
def create_json():
    req = request.values
    apiname = req['apiname'] if 'apiname' in req else ""
    case_data = req['case_data'] if 'case_data' in req else ""

    jsons = runway.runway('post',case_data)
    app.logger.info("jsonify(json)")

    res =  json.dumps(jsons,ensure_ascii=False)
    app.logger.info(json.loads(json.dumps({"data":res},ensure_ascii=False)) )
    app.logger.info("res")
    app.logger.info(res)

    return json.dumps({"data":res},ensure_ascii=False)


# @case_page.route("/addcase", methods=["GET", "POST"])
def addcase():
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')
    req = request.values
    id = int(req['id']) if ('id' in req and req['id']) else 0
    if id < 1:
        return redirect(UrlManager.UrlManager.buildUrl("/case_list"))
    info = Coordination.query.filter_by(id=id).first()
    if not info:
        return redirect(UrlManager.UrlManager.buildUrl("/case_list"))
    param = info.parameter.split(",")
    pjlist = info.remarks.split(",")
    exp_param = info.exp_parameter.split(",")
    print(pjlist)
    return ops_render('case/taddcase.html', {"info": info, "param": param, "exp_param": exp_param, "pjlist": pjlist})


@case_page.route("/addcase", methods=["GET", "POST"])
def addcase():
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')
    req = request.values
    id = int(req['id']) if ('id' in req and req['id']) else 0
    if id < 1:
        return redirect(UrlManager.UrlManager.buildUrl("/case_list"))
    info = Coordination.query.filter_by(id=id).first()
    if not info:
        return redirect(UrlManager.UrlManager.buildUrl("/case_list"))

    pjlist = info.remarks.split(",")
    # param = json.loads(info.param)
    # data = json.loads(info.data)
    param = info.param
    data = info.data
    url = info.route

    return ops_render('case/taddcase.html', {"param": param,'data':data, "pjlist": pjlist, 'info':info, 'url':url, 'id':id})




@case_page.route("/do_add", methods=["GET", "POST"])
def do_add():
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    if request.method == "GET":
        return ops_render("case/case_list")

    req = request.get_json()
    user_id = is_login.user_id
    route = req['route']
    param = json.loads(req['param'])
    data = json.loads(req['data'])
    exp = json.loads(req['exp'])
    explain = req['explain']
    apiname = req['apiname']
    coordinationId = req['coordinationId']


    # pjname = req['pjname'] if 'pjname' in req else ""


    try:
        modle_addcase = CoordinationCase()
        modle_addcase.route = route
        modle_addcase.case_data = data
        modle_addcase.expected_results = exp
        modle_addcase.apiname = apiname
        modle_addcase.explain = explain
        modle_addcase.ispj = '123'
        modle_addcase.user_id = user_id
        modle_addcase.param = param
        modle_addcase.coordination_id = coordinationId
        db.session.add(modle_addcase)
        db.session.commit()
        db.session.close()
    except Exception as e:
        print(e)
        return helper.ops_renderErrJSON(msg="提交失败了我擦")
    else:
        # return jsonify(msg='success')
        return helper.ops_renderJSON(msg="提交成功")
    # return redirect(UrlManager.UrlManager.buildUrl("/case_list"))


# @case_page.route("/mylist", methods=["GET", "POST"])
def mylist():
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    info = CoordinationCase.query.filter_by(user_id=is_login.user_id)
    if not info:
        return redirect(UrlManager.UrlManager.buildUrl("/case_list"))

    return ops_render('case/mylist.html', {"data": info})


@case_page.route("/mylist", methods=["GET", "POST"])
def mylist():
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    # 根据映射表，查询用户的一级模块权限
    info = SystemInfo.query.all()
    if not info:
        return redirect(UrlManager.UrlManager.buildUrl("/case_list"))
    return ops_render('case/my_list_bak.html', {'data':info})

# @case_page.route("/ttt", methods=["GET"])
# def ttt():
#     info = db.session.query(SystemInfo, AuthMap.user_id).join(AuthMap, SystemInfo.id==AuthMap.system_id)
#     print(info, '***************************')
#     for ii in info:
#         print(dir(ii), 'xxxxxxxxxxxxxxxxx000000000000000xxxxxxxxxxxxx')
#
#
#     if not info:
#         return redirect(UrlManager.UrlManager.buildUrl("/case_list"))
#     return ops_render('case/my_list_bak.html', {'data':info})



@case_page.route("/getSecondContent", methods=["POST"])
def getSecondContent():
    # 根据映射表，查询用户的二级模块权限
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    req = request.get_json()
    system_id = req['system_id']

    info = FuncInfo.query.filter_by(system_id=system_id)

    if not info:
        return redirect(UrlManager.UrlManager.buildUrl("/case_list"))

    data = []
    for i in info:
        temp = dict()
        temp['id'] = i.id
        temp['name'] = i.name
        data.append(temp)

    return jsonify(status='0', data=data)

@case_page.route("/getThirdContent", methods=["POST"])
def getThirdContent():
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    req = request.get_json()

    # info = CoordinationCase.query.filter_by(user_id=is_login.user_id, func_id = func_id)
    info = db.session.query(CoordinationCase.case_id,
                            CoordinationCase.user_id,
                            CoordinationCase.apiname,
                            CoordinationCase.case_data,
                            CoordinationCase.expected_results,
                            CoordinationCase.ispj,
                            CoordinationCase.remarks,
                            CoordinationCase.explain,
                            CoordinationCase.route
                            ).join(Coordination, and_(CoordinationCase.coordination_id==Coordination.id,
                                                      CoordinationCase.user_id==is_login.user_id,
                                                      Coordination.func_id == req['func_id']
                                                      )).all()
    if not info:
        return redirect(UrlManager.UrlManager.buildUrl("/case_list"))

    data = []

    for i in info:
        temp = dict()
        temp['case_id'] = i.case_id
        route = i.route
        if route == None or route == '':
            temp['apiname'] = ''
        else:
            temp['apiname'] = i.route.split('/')[-1]

        temp['case_data'] = i.case_data
        temp['expected_results'] = i.expected_results
        # temp['apiname'] = i.apiname
        temp['ispj'] = i.ispj
        temp['remarks'] = i.remarks
        temp['explain'] = i.explain
        data.append(temp)

    return jsonify(status='0', data=data)




@case_page.route("/editcase", methods=["GET", "POST"])
def editcase():
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')
    req = request.values
    case_id = int(req['case_id']) if ('case_id' in req and req['case_id']) else 0
    if case_id < 1:
        return redirect(UrlManager.UrlManager.buildUrl("/case/mylist"))
    info = CoordinationCase.query.filter_by(case_id=case_id).first()
    if not info:
        return redirect(UrlManager.UrlManager.buildUrl("/case/mylist"))

    #  case_data = info.case_data.split(",")
    param = json.dumps(info.param)
    expected_results = json.dumps(info.expected_results)
    case_data = json.dumps(info.case_data)
    explain = info.explain

    pjlist = info.remarks.split(",")
    app.logger.info("pjlist")
    app.logger.info(pjlist)
    # param = info.parameter.split(",")
    # pjlist = info.remarks.split(",")
    # exp_param = info.exp_parameter.split(",")
    app.logger.info("info.case_data")
    app.logger.info(pjlist)
    app.logger.info(case_data)
    return ops_render('case/editcase.html',
                      {"info": info, "explain":explain, "param":param, "case_data": case_data, "expected_results": expected_results, "pjlist": pjlist})


'''
@member_page.route("/reg",methods = ["GET","POST"])
def reg():
    if request.method == "GET":
        return ops_render("member/reg.html")
'''


@case_page.route("/do_edit", methods=["GET", "POST"])
def do_edit():
    if request.method == "GET":
        return ops_render("case/mylist.html")
    req = request.get_json()

    caseid = req['caseid']
    param = req['param']
    data = req['data']
    asser = req['assert']
    explain = req['explain']

    temp = dict()
    temp['case_data'] = json.loads(data)
    temp['param'] = json.loads(param)
    temp['expected_results'] = json.loads(asser)
    temp['explain'] = explain
    db.session.query(CoordinationCase).filter_by(case_id=caseid).update(temp)
    db.session.commit()


    return helper.ops_renderJSON(msg="提交成功")


@case_page.route("/addmodel", methods=["GET", "POST"])
def addmodel():
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')
    return ops_render('case/addmodel.html')


@case_page.route("/do_addmodel", methods=["GET", "POST"])
def do_addmodel():
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')
    req = request.values
    apiname = req['apiname'] if 'apiname' in req else ""
    explain = req['explain'] if 'explain' in req else ""
    route = req['route'] if 'route' in req else ""
    method = req['method'] if 'method' in req else ""
    param = req['param'] if 'param' in req else ""
    data = req['data'] if 'data' in req else ""
    dataType = req['dataType'] if 'dataType' in req else ""
    func_id = req['func_id'] if 'func_id' in req else ""

    if apiname is None or len(apiname) < 1:
        return helper.ops_renderErrJSON(msg="接口名称是必填项")
    if route is None or len(route) < 1:
        return helper.ops_renderErrJSON(msg="路径是必填项")
    if method is None or len(method) < 1:
        return helper.ops_renderErrJSON(msg="请求方法是必填项")
    if explain is None or len(explain) < 1:
        return helper.ops_renderErrJSON(msg="中文解释是必填项")
    if param is None or len(param) < 1:
        return helper.ops_renderErrJSON(msg="param参数是必填项")
    if data is None or len(data) < 1:
        return helper.ops_renderErrJSON(msg="入参是必填项,没有填空")
    if dataType is None or len(dataType) < 1:
        return helper.ops_renderErrJSON(msg="入参类型是必填项,没有入参的话，随便填一个")
    if func_id is None or len(func_id) < 1:
        return helper.ops_renderErrJSON(msg="功能模块id是必填项")

    modle_addmodel= Coordination()
    modle_addmodel.apiname = apiname
    modle_addmodel.explain = explain
    modle_addmodel.route = route
    modle_addmodel.method = method
    modle_addmodel.param = param
    modle_addmodel.data = data
    modle_addmodel.dataType = dataType
    modle_addmodel.func_id = func_id

    db.session.add(modle_addmodel)
    db.session.commit()
    db.session.close()

    return helper.ops_renderJSON(msg="提交成功")




# 执行测试用例
@case_page.route('/exeCases', methods=['POST'])
def exeCases():
    '''
    接收参数：[{"func_id":1,"case":[排序好的用例id]}]
    :return:
    '''


    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    current = datetime.datetime.now()
    # 创建时间
    createTime = current.strftime("%Y-%m-%d %H:%M:%S")
    # 报告后缀，年月日时分秒+13位时间戳后三位
    backContent = current.strftime("%Y%m%d%H%M%S{}".format(str(int(time.time()*1000))[-3:]))
    # 报告名
    reportName = '测试报告_{}'.format(backContent)


    req = request.get_json()

    finalData = dict()
    for obj in req['caseids']:
        caseids = obj['case']   # 已经排好序的
        s = obj['func_id']
        i = FuncInfo.query.filter_by(id=obj['func_id']).first()
        func_name = i.name

        info = db.session.query(CoordinationCase.case_id,
                                CoordinationCase.coordination_id,
                                CoordinationCase.explain,
                                CoordinationCase.route,
                                CoordinationCase.param,
                                CoordinationCase.case_data,
                                CoordinationCase.expected_results,
                                Coordination.method,
                                Coordination.dataType
                                ).join(Coordination, Coordination.id==CoordinationCase.coordination_id).filter(CoordinationCase.case_id.in_(caseids)).all()
        caseDict = dict()
        for i in info:
            temp = dict()
            temp['case_id'] = i.case_id
            temp['coordination_id'] = i.coordination_id
            temp['route'] = i.route
            temp['param'] = i.param
            temp['case_data'] = i.case_data
            temp['expected_results'] = i.expected_results
            temp['method'] = i.method
            temp['dataType'] = i.dataType
            temp['explain'] = i.explain

            caseDict[i.case_id] = temp

        # 把用例进行排序
        caseOrder = list()
        try:
            for caseid in caseids:
                caseOrder.append(caseDict[caseid])
        except:
            return jsonify(msg='id不存在,{}'.format(caseid))
        else:
            # 排序之后存入返回变量 [{"模块名":caseOrder}]
            finalData[func_name] = caseOrder

    # 启动新的线程执行测试用例
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    obj = RunPyTest()
    t = multiprocessing.Process(target=obj.run, args=(is_login.user_id, finalData, path, backContent))
    t.start()

    # 保存测试报告到数据库
    report = ReportInfo()
    report.delflag = 0
    report.createTime = createTime
    report.reportName = reportName
    report.user_id = is_login.user_id
    report.backContent = backContent
    db.session.add(report)
    db.session.commit()


    return jsonify(msg='OK')



# 删除测试用例
@case_page.route('/deletecases', methods=['POST'])
def deleteCases():
    '''
    接收用例id列表，进行删除  {caseId:[]}
    :return:
    '''

    req = request.get_json()
    ids = req.get('caseId')
    if ids == None:
        return  jsonify(msg = '没有获取到入参')

    print(ids,'*************************************')
    db.session.query(CoordinationCase).filter(CoordinationCase.case_id.in_(ids)).delete()
    db.session.commit()
    return jsonify(msg='删除成功')


# 测试测试用例-单独执行
@case_page.route('/dotest', methods=['POST'])
def dotest():
    req = request.get_json()
    caseid = req.get('caseId')
    case = db.session.query(CoordinationCase.param,
                            CoordinationCase.route,
                            CoordinationCase.case_data,
                            Coordination.dataType,
                            Coordination.method,
                            CoordinationCase.expected_results).join(Coordination, Coordination.id==CoordinationCase.coordination_id).filter(CoordinationCase.case_id==caseid).first()
    if case == None:
        return jsonify(msg='没有找到该用例')


    url = case.route
    data = case.case_data
    param = case.param
    dataType = case.dataType
    method = case.method
    expected_results = case.expected_results

    try:
        if method.lower() == 'get':
            res = requests.get(url, headers = header, params=param)
        else:

            if dataType.lower() == 'data':
                res = requests.post(url, headers = header, params=param, data = data)
            else:
                res = requests.post(url, headers = header, params=param, json = data)

            for pat in expected_results:
                exp_value = expected_results[pat]
                try:
                    fact_value = jmespath.search(pat, res.json())
                except:
                    assert False, '断言获取字段失败\n断言表达式:{}\n返回的值:{}'.format(pat, res.text)

                assert exp_value == fact_value, '\n断言失败\n断言表达式::{}\n期望值:{}\n实际结果:{}'.format(pat, exp_value, fact_value)


        return jsonify(msg='测试通过')

    except Exception as e:
        return jsonify(
            msg='测试不通过',
            url = url,
            param=param,
            data = data,
            error=str(e))




# 查看测试报告
@case_page.route('/viewReport', methods=['GET'])
def viewReport():
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    # 从数据库获取测试报告列表
    reports = db.session.query(ReportInfo).filter(and_(ReportInfo.delflag==0, ReportInfo.user_id==is_login.user_id)).all()


    info = {'user_id':is_login.user_id, 'reports':reports}

    resp = make_response()
    resp.status_code = 200
    resp.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    resp.response = ops_render(r'/reports/index.html', info)
    resp.cache_control.public = False

    return resp


# 删除测试报告：逻辑
@case_page.route('/deleteReport', methods=['POST'])
def deleteReport():
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    req = request.get_json()
    repid = req['repid']

    db.session.query(ReportInfo).filter(ReportInfo.id==repid).update({"delflag":1})
    db.session.commit()
    return jsonify(msg='删除成功！')



# 删除测试报告：物理删除
@case_page.route('/deleteReportReal', methods=['POST'])
def deleteReportReal():
    import shutil
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    req = request.get_json()
    repid = req['repid']

    repinfo = db.session.query(ReportInfo).filter(ReportInfo.id==repid)
    backcontent = repinfo.first().backContent
    repinfo.delete()
    db.session.commit()


    # 删除服务器文件
    shutil.rmtree('./static/reports/{}_{}'.format(is_login.user_id, backcontent))

    return jsonify(msg='删除成功！')


''' 2022.5.31  新功能，添加测试用例组  '''
# 新增组
@case_page.route('/saveGroup', methods=['POST'])
def saveGroup():
    '''
    {'desc':'测试组','caseId':['30','31','32']}
    :return:
    '''
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    desc = request.get_json().get('desc')
    caseId = request.get_json().get('caseId')
    if desc == None or caseId == None:
        return jsonify(**RetJson.retContent(RetJson.failCode, None, '用例id或者组描述为空'))

    # 把传入的caseid，转成字符串
    ids = ','.join(caseId)

    group = CaseGroup()
    group.desc = desc
    group.caseids = ids
    group.user_id = is_login.user_id
    db.session.add(group)
    db.session.commit()
    return jsonify(**RetJson.retContent(RetJson.successCode, None, '保存成功'))


# 更新
@case_page.route('/updateGroup', methods=['POST'])
def updateGroup():
    '''
    {'groupid':'2','caseId':['33'], 'desc':'123'}
    :return:
    '''
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    groupid = request.get_json().get('groupid')
    caseId = request.get_json().get('caseId')
    desc = request.get_json().get('desc')
    if groupid == None or caseId == None or desc == None or groupid == '' or caseId == '' or desc == '':
        return jsonify(**RetJson.retContent(RetJson.failCode, None, '用例id或者组id为空'))

    ids = ','.join(caseId)

    obj = {'caseids':ids, 'desc':desc}
    db.session.query(CaseGroup).filter_by(id=groupid).update(obj)
    db.session.commit()
    return jsonify(**RetJson.retContent(RetJson.successCode, None, '用例组更新成功'))


# 删除
@case_page.route('/deleteGroup', methods=['POST'])
def deleteGroup():
    '''
    {'groupid':'2','caseId':['33'], 'desc':'123'}
    :return:
    '''
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    groupId = request.get_json().get('groupid')

    db.session.query(CaseGroup).filter_by(id=groupId).delete()
    db.session.commit()
    return jsonify(**RetJson.retContent(RetJson.successCode, None, '删除成功'))


# 查看用户的组
@case_page.route('/viewGroup', methods=['GET'])
def viewGroup():
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    user_id = is_login.user_id

    groups = db.session.query(CaseGroup.id, CaseGroup.caseids, CaseGroup.desc).filter_by(user_id=user_id)
    ret = []
    for group in groups:
        temp = dict()
        temp['desc'] = group.desc
        temp['caseNum'] = len(group.caseids.split(','))
        temp['groupid'] = group.id
        ret.append(temp)

    return jsonify(**RetJson.retContent(RetJson.successCode, ret))


# 查看组下边的测试用例
@case_page.route('/viewCaseUnderGroup', methods=['POST'])
def viewCaseUnderGroup():
    '''
    {'groupid':'2'}
    :return:
    '''
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')
    user_id = is_login.user_id
    groupid = request.get_json().get('groupid')

    group = db.session.query(CaseGroup).filter_by(id=groupid).first()
    caseids = group.caseids

    caseids_list = caseids.split(',')

    info = db.session.query(CoordinationCase.case_id,
                            CoordinationCase.user_id,
                            CoordinationCase.apiname,
                            CoordinationCase.case_data,
                            CoordinationCase.expected_results,
                            CoordinationCase.ispj,
                            CoordinationCase.remarks,
                            CoordinationCase.explain,
                            CoordinationCase.route
                            ).filter(and_(CoordinationCase.case_id.in_(caseids_list), CoordinationCase.user_id==user_id))
    if not info:
        return redirect(UrlManager.UrlManager.buildUrl("/case_list"))

    data = []

    for i in info:
        temp = dict()
        temp['case_id'] = i.case_id
        route = i.route
        if route == None or route == '':
            temp['apiname'] = ''
        else:
            temp['apiname'] = i.route.split('/')[-1]

        temp['case_data'] = i.case_data
        temp['expected_results'] = i.expected_results
        # temp['apiname'] = i.apiname
        temp['ispj'] = i.ispj
        temp['remarks'] = i.remarks
        temp['explain'] = i.explain
        data.append(temp)

    return jsonify(**RetJson.retContent(RetJson.successCode, data))


# 一键执行组下边的所有用例
@case_page.route('/runCaseUnderGroup', methods=['POST'])
def runCaseUnderGroup():
    '''
    {'groupid':'2'}
    :return:
    '''
    ret = []

    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    groupid = request.get_json().get('groupid')
    user_id = is_login.user_id
    group = db.session.query(CaseGroup).filter_by(id=groupid).first()
    caseids = group.caseids.split(',')

    cases = db.session.query(CoordinationCase.param,
                             CoordinationCase.case_id,
                             CoordinationCase.route,
                             CoordinationCase.case_data,
                             Coordination.dataType,
                             Coordination.method,
                             CoordinationCase.expected_results).join(Coordination, Coordination.id==CoordinationCase.coordination_id).filter(CoordinationCase.case_id.in_(caseids))
    for caseid in caseids:
        for case in cases:
            if caseid == str(case.case_id):
                url = case.route
                data = case.case_data
                param = case.param
                dataType = case.dataType
                method = case.method
                expected_results = case.expected_results

                try:
                    if method.lower() == 'get':
                        res = requests.get(url, headers = header, params=param)
                    else:

                        if dataType.lower() == 'data':
                            res = requests.post(url, headers = header, params=param, data = data)
                        else:
                            res = requests.post(url, headers = header, params=param, json = data)
                except:
                    return jsonify(**RetJson.retContent(RetJson.failCode, None, '用例id:{} 执行时发生错误'.format(case.case_id)))

                temp = dict()
                temp[case.case_id] = res.json()
                ret.append(temp)



    return jsonify(**RetJson.retContent(RetJson.successCode, ret))


