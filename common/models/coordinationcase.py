# coding: utf-8
from app import app
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:xfs123456@192.168.0.129:3306/xfstestpj"
db = SQLAlchemy(app)
class CoordinationCase(db.Model):
    __tablename__ = 'coordination_case'

    case_id = db.Column(db.Integer, primary_key=True, info='用例id')
    user_id = db.Column(db.String(255, 'utf8_general_ci'), nullable=False, info='用户id')
    route = db.Column(db.String(255, 'utf8_general_ci'), info='路径')
    case_data = db.Column(db.String(255, 'utf8_general_ci'), info='用例请求值')
    results = db.Column(db.String(10000, 'utf8_general_ci'), info='返回值')
    expected_results = db.Column(db.String(10000, 'utf8_general_ci'), info='预期返回值')
    rely_key = db.Column(db.Integer, info='依赖caseid')
    apiname = db.Column(db.String(255, 'utf8_general_ci'), nullable=False, info='接口名')
    ispj = db.Column(db.String(255), nullable=False, info='所属项目')
    explain = db.Column(db.String(255), info='说明')
    remarks = db.Column(db.String(255, 'utf8_general_ci'), server_default=db.FetchedValue(), info='相关联系统列表')
