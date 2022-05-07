# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
# coding: utf-8
from app import app
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:xfs123456@192.168.0.129:3306/xfstestpj"
db = SQLAlchemy(app)


class ReportInfo(db.Model):
    __tablename__ = 'reportInfo'

    id = db.Column(db.Integer, primary_key=True)
    delflag = db.Column(db.Integer)
    createTime = db.Column(db.String(255))
    reportName = db.Column(db.String(255))
    user_id = db.Column(db.String(255))
    backContent = db.Column(db.String(255))
