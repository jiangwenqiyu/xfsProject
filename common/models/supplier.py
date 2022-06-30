# # coding: utf-8
# from app import app
# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:xfs123456@192.168.0.129:3306/xfstestpj"
# db = SQLAlchemy(app)

from app import db

class Supplier(db.Model):
    __tablename__ = 'supplier'

    id = db.Column(db.Integer, primary_key=True)
    apiname = db.Column(db.String(255), nullable=False, info='接口名称')
    route = db.Column(db.String(255), nullable=False, info='路径')
    parameter = db.Column(db.String(10000, 'utf8_general_ci'), info='请求参数')
    exp_parameter = db.Column(db.String(10000, 'utf8_general_ci'), info='返回参数')
    method = db.Column(db.String(255), nullable=False, info='请求方法')
    remarks = db.Column(db.String(255, 'utf8_general_ci'), info='备注')