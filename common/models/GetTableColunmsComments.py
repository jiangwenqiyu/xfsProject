# coding: utf-8
from app import app
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:xfs123456@192.168.0.129:3306/xfstestpj"
db = SQLAlchemy(app)
class XfsTableColunmsComment(db.Model):
    __tablename__ = 'xfs_table_colunms_comments'

    id = db.Column(db.Integer, primary_key=True, info='序号')
    table_name = db.Column(db.String(500, 'utf8_general_ci'), nullable=False, info='表名')
    column_name = db.Column(db.Text(collation='utf8_general_ci'), info='列名')
    table_commnet = db.Column(db.String(5000, 'utf8_general_ci'), info='表名')
    column_comment = db.Column(db.Text(collation='utf8_general_ci'), info='列注释')
