#变量
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import redis
from datetime import timedelta
from config import constance


app = Flask(__name__)
manager = Manager(app)

app.config.from_pyfile("config/base_setting.py")
# 不设置缓存
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

#数据库链接初始化
app.config['SQLALCHEMY_DATABASE_URI'] = constance.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

# redis连接初始化
redis_store = redis.StrictRedis(host = constance.REDIS_HOST, port = constance.REDIS_PORT)

app.logger.info("================")





