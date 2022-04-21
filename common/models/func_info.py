# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
# coding: utf-8
from app import app
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:xfs123456@192.168.0.129:3306/xfstestpj"
db = SQLAlchemy(app)


class FuncInfo(db.Model):
    __tablename__ = 'func_info'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    system_id = db.Column(db.Integer)
