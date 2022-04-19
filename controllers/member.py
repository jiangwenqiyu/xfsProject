# coding=utf-8
from app import app,db
from flask import Blueprint,request,make_response,redirect
from common.libs import helper, UrlManager
from common.models.user import User
from common.libs import UserService
from common.libs.helper import ops_render
from flask import session

member_page = Blueprint("member_page",__name__)
@member_page.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return ops_render('member/login.html')

    req = request.values
    login_name = req["login_name"] if "login_name" in req else ""
    userpwd = req["userpwd"] if "userpwd" in req else ""
    if login_name == None or len(login_name) < 1 :
        return helper.ops_renderErrJSON("请输入正确的用户名或密码")
    if userpwd == None or len(userpwd) < 6 :
        return helper.ops_renderErrJSON("请输入正确的用户名或密码")

    user_info = User.query.filter_by(user_id = login_name).first()
    if not user_info:
        return helper.ops_renderErrJSON("请输入正确的用户名或密码")

    if user_info.password != UserService.UserService.genePwd(userpwd,user_info.login_salt):
        return helper.ops_renderErrJSON("请输入正确的用户名或密码")

    if user_info.state != 1:
        return helper.ops_renderErrJSON("账户已被禁用")

    response = make_response(helper.ops_renderJSON(msg="登陆成功"))
    response.set_cookie(app.config["AUTH_COOKIE_NAME"],"%s#%s"%(UserService.UserService.geneAuthCode(user_info),user_info.id),60*60*7)
    return response

    #return helper.ops_renderJSON(msg = "登陆成功")

@member_page.route("/reg",methods = ["GET","POST"])
def reg():
    if request.method == "GET":
        return ops_render("member/reg.html")
    reg = request.values
    login_name = reg['login_name'] if 'login_name' in reg else ""
    userpwd = reg['userpwd'] if 'userpwd' in reg else ""
    userpwd1 = reg['userpwd1'] if 'userpwd1' in reg else ""

    if login_name is None or len(login_name) < 1:
        return helper.ops_renderErrJSON(msg="用户名不能为空")

    if userpwd is None or len(userpwd) < 6:
        return helper.ops_renderErrJSON(msg="用户名不能为空")

    if userpwd1 != userpwd:
        return helper.ops_renderErrJSON(msg="两次密码不也一样，再试试")

    user_info = User.query.filter_by(user_id = login_name).first()
    if user_info:
        return helper.ops_renderErrJSON(msg="注册的用户名已经有了，换一个吧。")

    modle_user = User()
    modle_user.user_id = login_name
    modle_user.login_salt = UserService.UserService.getsalt(8)
    modle_user.password = UserService.UserService.genePwd(userpwd,modle_user.login_salt)
    modle_user.state = 1
    db.session.add(modle_user)
    db.session.commit()
    return helper.ops_renderJSON("注册成功")

@member_page.route("/logout")
def logOut():
    response = make_response( redirect( UrlManager.UrlManager.buildUrl("/member/login") ) )
    response.delete_cookie(  app.config['AUTH_COOKIE_NAME'] )
    return response




