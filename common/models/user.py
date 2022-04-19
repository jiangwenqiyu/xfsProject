# coding: utf-8
from app import app
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:xfs123456@192.168.0.129:3306/xfstestpj"
db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), nullable=False)
    group = db.Column(db.Integer)
    name = db.Column(db.String(255, 'utf8_general_ci'))
    state = db.Column(db.Integer)
    password = db.Column(db.String(255, 'utf8_general_ci'), nullable=False)
    login_salt = db.Column(db.String(255), nullable=False)
