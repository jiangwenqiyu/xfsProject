# coding=utf-8
#路由注册
from controllers.index import index_page
from controllers.member import member_page
from controllers.case import case_page
from controllers.stressTest import api_stress
from app import app
from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension(app)
from interceptors.Auth import *
from interceptors.errorHandler import *
#注册蓝图，首层路径设置
app.register_blueprint(member_page,url_prefix="/member")
app.register_blueprint(index_page, url_prefix="/")
app.register_blueprint(case_page,url_prefix="/case")
app.register_blueprint(api_stress,url_prefix="/stress")

from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildUrl,"buildUrl")
app.add_template_global(UrlManager.buildStaticUrl,"buildStaticUrl")