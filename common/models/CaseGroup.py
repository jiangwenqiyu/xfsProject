# # coding: utf-8
# from app import app
# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:xfs123456@192.168.0.129:3306/xfstestpj"
# db = SQLAlchemy(app)

from app import db
class CaseGroup(db.Model):
    __tablename__ = 'case_group'

    id = db.Column(db.Integer, primary_key=True)
    caseids = db.Column(db.String(255))
    desc = db.Column(db.String(100))
    user_id = db.Column(db.String(30))
