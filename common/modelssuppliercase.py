# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class SupplierCase(db.Model):
    __tablename__ = 'supplier_case'

    case_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(255, 'utf8_general_ci'), nullable=False)
    case_data = db.Column(db.String(255, 'utf8_general_ci'))
    results = db.Column(db.String(10000, 'utf8_general_ci'))
    expected_results = db.Column(db.String(10000, 'utf8_general_ci'))
    rely_key = db.Column(db.Integer)
