# coding=utf-8
import json

from app import app, db
from flask import Blueprint, request, redirect, g, jsonify, render_template
from common.libs import helper, UrlManager
from common.models.supplier import Supplier
from common.models.suppliercase import SupplierCase
from common.models.coordination import Coordination
from common.models.coordinationcase import CoordinationCase
from common.libs.helper import ops_render
from interceptors.Auth import check_login
from common.libs.requery import requery
from testmain import run
from testmain import runway

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

   # res = jsonify(jsons)
    return json.dumps({"data":res},ensure_ascii=False)
   # return render_template('case/taddcase.html', **json)


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


@case_page.route("/do_add", methods=["GET", "POST"])
def do_add():
    if request.method == "GET":
        return ops_render("case/case_list")
    req = request.values
    apiname = req['apiname'] if 'apiname' in req else ""
    param = req['param'] if 'param' in req else ""
    user_id = req['user_id'] if 'user_id' in req else ""
    exp_param = req['expparam'] if 'expparam' in req else ""
    pjname = req['pjname'] if 'pjname' in req else ""
    explain = req['explain'] if 'explain' in req else ""

    try:
        modle_addcase = CoordinationCase()
        modle_addcase.user_id = check_login().user_id
        modle_addcase.apiname = apiname
        modle_addcase.case_data = param
        modle_addcase.expected_results = exp_param
        modle_addcase.ispj = pjname
        modle_addcase.explain = explain
        db.session.add(modle_addcase)
        db.session.commit()
        db.session.close()
    except BaseException:
        print(BaseException)
    else:
        return helper.ops_renderJSON(msg="提交成功")
    # return redirect(UrlManager.UrlManager.buildUrl("/case_list"))


@case_page.route("/mylist", methods=["GET", "POST"])
def mylist():
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    info = CoordinationCase.query.filter_by(user_id=is_login.user_id)
    if not info:
        return redirect(UrlManager.UrlManager.buildUrl("/case_list"))

    return ops_render('case/mylist.html', {"data": info})


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
    expected_results = json.loads(info.expected_results)
    case_data = json.loads(info.case_data)

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
                      {"info": info, "case_data": case_data, "expected_results": expected_results, "pjlist": pjlist})


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
    req = request.values
    apiname = req['apiname'] if 'apiname' in req else ""
    param = req['param'] if 'param' in req else ""
    case_id = req['case_id'] if 'case_id' in req else ""
    exp_param = req['expparam'] if 'expparam' in req else ""
    pjname = req['pjname'] if 'pjname' in req else ""
    explain = req['explain'] if 'explain' in req else ""

    app.logger.info(check_login().user_id)
    app.logger.info("check_login().user_id")

    modle_addcase = CoordinationCase()
    user = modle_addcase.query.filter_by(case_id=case_id).first()
    user.user_id = check_login().user_id
    user.apiname = apiname
    user.case_data = param
    user.expected_results = exp_param
    user.ispj = pjname
    user.explain = explain
    # db.session.add(user)
    db.session.commit()
    # db.session.close()

    return helper.ops_renderJSON(msg="提交成功")
    # return redirect(UrlManager.UrlManager.buildUrl("/case_list"))


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
    route = req['route'] if 'route' in req else ""
    parameter = req['parameter'] if 'parameter' in req else ""
    exp_parameter = req['exp_parameter'] if 'exp_parameter' in req else ""
    method = req['method'] if 'method' in req else ""
    explain = req['explain'] if 'explain' in req else ""

    if apiname is None or len(apiname) < 1:
        return helper.ops_renderErrJSON(msg="接口名称是必填项")
    if route is None or len(route) < 1:
        return helper.ops_renderErrJSON(msg="路径是必填项")
    if method is None or len(method) < 1:
        return helper.ops_renderErrJSON(msg="请求方法是必填项")
    if explain is None or len(explain) < 1:
        return helper.ops_renderErrJSON(msg="中文解释是必填项")

    modle_addmodel= Coordination()
    modle_addmodel.route = route
    modle_addmodel.apiname = apiname
    modle_addmodel.parameter = parameter
    modle_addmodel.exp_parameter = exp_parameter
    modle_addmodel.method = method
    modle_addmodel.explain = explain

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



@case_page.route("/addcase", methods=["GET", "POST"])
def addcase():


    def digui(data, calc, li):

        if isinstance(data, dict):  # 字典
            for key in data:
                tab = ''
                for x in range(calc-1):
                    tab += '\t'
                # print('{}{}-{}'.format(tab, key, type(data[key])))  # 打印键
                li.append('{}--{}'.format(key, calc))

                if isinstance(data[key], dict):  # 判断这个键的值，是否还是字典或列表，是的话继续递归,不是的话，打印当前键，看下一个键
                    digui(data[key], calc, li)
                elif isinstance(data[key], list):
                    digui(data[key], calc, li)
                else:
                    pass


        elif isinstance(data, list):  # 列表
            if len(data) == 0:
                return
            else: # 如果是列表，只取一个元素，继续递归
                digui(data[0], calc+1, li)


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
    param = info.parameter
    li = []
    digui(eval(param),1, li)
    param = li
    print(li)



    pjlist = info.remarks.split(",")
    exp_param = info.exp_parameter.split(",")
    return ops_render('case/taddcase.html', {"info": info, "param": param, "exp_param": exp_param, "pjlist": pjlist})