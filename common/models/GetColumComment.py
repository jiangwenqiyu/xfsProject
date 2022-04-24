# coding: utf-8
from app import app
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:xfs123456@192.168.0.129:3306/xfstestpj"
db = SQLAlchemy(app)
class XfsColumnComment(db.Model):
    __tablename__ = 'xfs_column_comment'

    table_name = db.Column(db.String(100, 'utf8_general_ci'), info='表名')
    column_name = db.Column(db.String(100, 'utf8_general_ci'), info='列名')
    column_comment = db.Column(db.String(1000, 'utf8_general_ci'), info='列名注释')
    id = db.Column(db.Integer, primary_key=True, info='id')
