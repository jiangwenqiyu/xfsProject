# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Supplier(db.Model):
    __tablename__ = 'supplier'

    id = db.Column(db.Integer, primary_key=True)
    apiname = db.Column(db.String(255), nullable=False, info='接口名称')
    route = db.Column(db.String(255), nullable=False, info='路径')
    parameter = db.Column(db.String(10000, 'utf8_general_ci'), info='请求参数')
    exp_parameter = db.Column(db.String(10000, 'utf8_general_ci'), info='返回参数')
    method = db.Column(db.String(255), nullable=False, info='请求方法')
