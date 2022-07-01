# coding: utf-8
from app import db


class Scene(db.Model):
    __tablename__ = 'scene'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    userid = db.Column(db.String(20), nullable=False)
    caseids = db.Column(db.String(500), server_default=db.FetchedValue())
    createTime = db.Column(db.DateTime, server_default=db.FetchedValue())
    updateTime = db.Column(db.DateTime, server_default=db.FetchedValue())
