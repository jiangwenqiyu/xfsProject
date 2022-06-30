# coding: utf-8
from app import db


class ReportInfo(db.Model):
    __tablename__ = 'reportInfo'

    id = db.Column(db.Integer, primary_key=True)
    delflag = db.Column(db.Integer)
    createTime = db.Column(db.String(255))
    reportName = db.Column(db.String(255))
    user_id = db.Column(db.String(255))
    backContent = db.Column(db.String(255))
    exeState = db.Column(db.Integer, server_default=db.FetchedValue())
