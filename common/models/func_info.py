# coding: utf-8
from app import app
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:xfs123456@192.168.0.129:3306/xfstestpj"
db = SQLAlchemy(app)


class SysInfo(db.Model):
    __tablename__ = 'system_info'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255, 'utf8_general_ci'))
    system_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

