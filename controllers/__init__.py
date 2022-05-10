from flask import Blueprint

# 存放所有蓝图

case_page = Blueprint("case", __name__)  # 用例相关的接口
index_page = Blueprint( "index_page",__name__ )  # 起始页接口
member_page = Blueprint("member_page",__name__)  # 用户相关
api_stress = Blueprint('stress', __name__)   # 压测

from controllers import case
from controllers import index
from controllers import member
from controllers import stressTest