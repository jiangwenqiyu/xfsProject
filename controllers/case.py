# coding=utf-8
import json

from app import app, db
from flask import Blueprint, request, redirect, g, jsonify, render_template
from common.libs import helper, UrlManager
from common.models.supplier import Supplier
from common.models.suppliercase import SupplierCase
from common.models.coordination import Coordination
from common.models.coordinationcase import CoordinationCase
from common.models.system_info import SystemInfo
from common.models.func_info import FuncInfo
from common.models.auth_map import AuthMap
from common.libs.helper import ops_render
from interceptors.Auth import check_login
from common.libs.requery import requery
from testmain import run
from testmain import runway
from sqlalchemy.sql import and_


case_page = Blueprint("case", __name__)


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

    return ops_render('case/taddcase.html', {"param": param,'data':data, "pjlist": pjlist, 'info':info, 'url':url})




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
    func_id = req['func_id']


    # pjname = req['pjname'] if 'pjname' in req else ""


    try:
        modle_addcase = CoordinationCase()
        modle_addcase.route = route
        modle_addcase.case_data = data
        modle_addcase.expected_results = exp
        modle_addcase.apiname = apiname
        modle_addcase.explain = explain
        modle_addcase.func_id = func_id
        modle_addcase.ispj = '123'
        modle_addcase.user_id = user_id
        modle_addcase.param = param
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
    func_id = req['func_id']

    info = CoordinationCase.query.filter_by(user_id=is_login.user_id, func_id = func_id)
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

    if apiname is None or len(apiname) < 1:
        return helper.ops_renderErrJSON(msg="接口名称是必填项")
    if route is None or len(route) < 1:
        return helper.ops_renderErrJSON(msg="路径是必填项")
    if method is None or len(method) < 1:
        return helper.ops_renderErrJSON(msg="请求方法是必填项")
    if explain is None or len(explain) < 1:
        return helper.ops_renderErrJSON(msg="中文解释是必填项")

    modle_addmodel= Coordination()
    modle_addmodel.apiname = apiname
    modle_addmodel.explain = explain
    modle_addmodel.route = route
    modle_addmodel.method = method
    modle_addmodel.param = param
    modle_addmodel.data = data
    modle_addmodel.dataType = dataType

    print(req)
    print(apiname)
    print(explain)
    print(route)
    print(method)
    print(param)
    print(data)
    print(dataType)

    db.session.add(modle_addmodel)
    db.session.commit()
    db.session.close()

    return helper.ops_renderJSON(msg="提交成功")


@case_page.route("/parseData", methods=["GET", "POST"])
def parseData():
    def getInfo(obj, temp):
        if isinstance(obj, dict):
            for k in obj:
                if isinstance(obj[k], dict):
                    t = dict()
                    tt = list()
                    tt = getInfo(obj[k], tt)
                    t[k] = tt
                    temp.append(t)
                elif isinstance(obj[k], list) and len(obj[k]) != 0 and isinstance(obj[k][0], dict):
                    t = dict()
                    tt = list()
                    tt = getInfo(obj[k][0], tt)
                    t[k] = tt
                    temp.append(t)

                else:
                    temp.append(k)

            return temp

        elif isinstance(obj, list) and len(obj) != 0 and isinstance(obj[0], dict):
            for k in obj[0]:
                if isinstance(obj[0][k], dict):
                    t = dict()
                    tt = list()
                    tt = getInfo(obj[0][k], tt)
                    t[k] = tt
                    temp.append(t)
                elif isinstance(obj[0][k], list) and len(obj[0][k]) != 0 and isinstance(obj[0][k][0], dict):
                    t = dict()
                    tt = list()
                    tt = getInfo(obj[0][k][0], tt)
                    t[k] = tt
                    temp.append(t)

                else:
                    temp.append(k)

            return temp

    c = Coordination.query.all()
    p = eval(c[4].parameter)
    a = getInfo(p, [])
    for i in a:
        print(i)
    return jsonify(sta = a)



# @case_page.route("/addcase", methods=["GET", "POST"])
# def addcase():
#
#
#     def digui(data, calc, li):
#
#         if isinstance(data, dict):  # 字典
#             for key in data:
#                 tab = ''
#                 for x in range(calc-1):
#                     tab += '\t'
#                 # print('{}{}-{}'.format(tab, key, type(data[key])))  # 打印键
#                 li.append('{}-{}--{}'.format(key, str(type(data[key])).replace('<class ', '').replace('>', ''), calc))
#
#                 if isinstance(data[key], dict):  # 判断这个键的值，是否还是字典或列表，是的话继续递归,不是的话，打印当前键，看下一个键
#                     digui(data[key], calc + 1, li)
#                 elif isinstance(data[key], list):
#                     digui(data[key], calc, li)
#                 else:
#                     pass
#
#
#         elif isinstance(data, list):  # 列表
#             if len(data) == 0:
#                 return
#             else: # 如果是列表，只取一个元素，继续递归
#                 digui(data[0], calc+1, li)
#
#
#     is_login = check_login()
#     if is_login == False:
#         return ops_render('member/login.html')
#     req = request.values
#     id = int(req['id']) if ('id' in req and req['id']) else 0
#     if id < 1:
#         return redirect(UrlManager.UrlManager.buildUrl("/case_list"))
#     info = Coordination.query.filter_by(id=id).first()
#     if not info:
#         return redirect(UrlManager.UrlManager.buildUrl("/case_list"))
#     param = info.parameter
#     li = []
#     digui(eval(param),1, li)
#     param = li
#     # print(li, '**************************')
#
#     li = []
#     real_li = []
#     for i in param:
#         # 先把字段存入li
#         li.append(i)
#         # 深拷贝li，反转
#         temp = copy.deepcopy(li)
#         temp.reverse()
#         # 判断是否是1级，是的话直接存入real
#         if i.split('--')[1] == '1':
#             real_li.append(i.split('--')[0])
#         # 否则取深拷贝层级，与当前层级最近的dict，为父字段   （父） 当前字段
#         else:
#             for x in temp:
#                 # if 'dict' in x and x.split('--')[1] != i.split('--')[1]:
#                 if x.split('--')[1] != i.split('--')[1]:
#                     real_li.append('<strong style="color: red">({})</strong> {}'.format(x.split('--')[0], i.split('--')[0]))
#                     break
#     param = real_li
#
#
#
#
#
#     pjlist = info.remarks.split(",")
#     exp_param = info.exp_parameter.split(",")
#     return ops_render('case/taddcase.html', {"info": info, "param": param, "exp_param": exp_param, "pjlist": pjlist})

