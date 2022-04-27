import os
import pytest
import shutil
import requests


class PyConfig:
    caseInfos = []



class RunPyTest:

    def __init__(self):
        self.userid = None


    def run(self, userid, caseInfos, path):
        self.userid = userid
        PyConfig.caseInfos = caseInfos

        # 创建报告目录
        if os.path.exists('{}/static/reports'.format(path)):
            pass
        else:
            os.mkdir('{}/static/reports'.format(path))

        # 根据用户，创建用户自己的报告目录.如果有历史数据，先删除历史数据
        if os.path.exists('{}/static/reports/{}'.format(path, self.userid)):
            shutil.rmtree('{}/static/reports/{}'.format(path, self.userid))
            os.mkdir('{}/static/reports/{}'.format(path, self.userid))
        else:
            os.mkdir('{}/static/reports/{}'.format(path, self.userid))

        # 判断用户下是否有临时allure目录
        if os.path.exists('{}/static/reports/{}/report_temp'.format(path, self.userid)):
            shutil.rmtree('{}/static/reports/{}/report_temp'.format(path, self.userid))
            os.mkdir('{}/static/reports/{}/report_temp'.format(path, self.userid))
        else:
            os.mkdir('{}/static/reports/{}/report_temp'.format(path, self.userid))

        if os.path.exists('{}/static/reports/{}/report'.format(path, self.userid)):
            shutil.rmtree('{}/static/reports/{}/report'.format(path, self.userid))
            os.mkdir('{}/static/reports/{}/report'.format(path, self.userid))
        else:
            os.mkdir('{}/static/reports/{}/report'.format(path, self.userid))

        tempdir = '{}/static/reports/{}/report_temp'.format(path, self.userid)
        reportdir = '{}/static/reports/{}/report'.format(path, self.userid)
        pytest.main(['-vs',  '{}/exeCase/testcases.py'.format(path), '--alluredir', '{}'.format(tempdir) ])
        # os.system('allure generate {} -o {} -c {}'.format(tempdir, reportdir, reportdir))

        # 执行完之后，请求内部接口，生成测试报告
        url = 'http://192.168.0.129:7890/case/generateReport'
        # url = 'http://127.0.0.1:5000/case/generateReport'
        data = {'user_id': self.userid}
        res = requests.post(url, json=data).json()
        print(res)









