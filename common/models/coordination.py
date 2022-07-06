# coding: utf-8
from app import db


class Coordination(db.Model):
    __tablename__ = 'coordination'

    id = db.Column(db.Integer, primary_key=True)
    apiname = db.Column(db.String(255), nullable=False)
    explain = db.Column(db.String(255), nullable=False)
    route = db.Column(db.String(255), nullable=False)
    method = db.Column(db.String(255), nullable=False)
    param = db.Column(db.String(10000))
    data = db.Column(db.String(10000))
    dataType = db.Column(db.String(20))
    remarks = db.Column(db.String(255, 'utf8_general_ci'), server_default=db.FetchedValue())
    func_id = db.Column(db.Integer)
