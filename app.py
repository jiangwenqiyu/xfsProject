#变量
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

manager = Manager(app)

app.config.from_pyfile("config/base_setting.py")

#数据库链接初始化
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:xfs123456@192.168.0.129:3306/xfstestpj"
db = SQLAlchemy(app)

app.logger.info("================")



