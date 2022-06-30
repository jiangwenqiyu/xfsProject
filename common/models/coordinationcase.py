# # coding: utf-8
# from flask_sqlalchemy import SQLAlchemy
# # coding: utf-8
# from app import app
# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:xfs123456@192.168.0.129:3306/xfstestpj"
# db = SQLAlchemy(app)

from app import db
class CoordinationCase(db.Model):
    __tablename__ = 'coordination_case'

    case_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255, 'utf8_general_ci'), nullable=False)
    route = db.Column(db.String(255, 'utf8_general_ci'))
    case_data = db.Column(db.JSON)
    results = db.Column(db.String(10000, 'utf8_general_ci'))
    expected_results = db.Column(db.JSON)
    rely_key = db.Column(db.Integer)
    apiname = db.Column(db.String(255, 'utf8_general_ci'), nullable=False)
    ispj = db.Column(db.String(255), nullable=False)
    explain = db.Column(db.String(255))
    remarks = db.Column(db.String(255, 'utf8_general_ci'), server_default=db.FetchedValue())
    param = db.Column(db.JSON)
    coordination_id = db.Column(db.Integer)
