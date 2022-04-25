import os
import pytest
import shutil

class PyConfig:
    caseInfos = None



class RunPyTest:

    def __init__(self, userid, caseInfos):
        PyConfig.caseInfos = caseInfos
        self.userid = userid


    def run(self):
        # 创建报告目录
        if os.path.exists('./static/reports'):
            pass
        else:
            os.mkdir('./static/reports')



        # 根据用户，创建用户自己的报告目录
        if os.path.exists('./static/reports/{}'.format(self.userid)):
            shutil.rmtree('./static/reports/{}'.format(self.userid))
            os.mkdir('./static/reports/{}'.format(self.userid))
        else:
            os.mkdir('./static/reports/{}'.format(self.userid))

        # 判断用户下是否有临时allure目录
        if os.path.exists('./static/reports/{}/report_temp'.format(self.userid)):
            os.rmdir('./static/reports/{}/report_temp'.format(self.userid))
            os.mkdir('./static/reports/{}/report_temp'.format(self.userid))
        else:
            os.mkdir('./static/reports/{}/report_temp'.format(self.userid))

        if os.path.exists('./static/reports/{}/report'.format(self.userid)):
            os.rmdir('./static/reports/{}/report'.format(self.userid))
            os.mkdir('./static/reports/{}/report'.format(self.userid))
        else:
            os.mkdir('./static/reports/{}/report'.format(self.userid))

        tempdir = './static/reports/{}/report_temp'.format(self.userid)
        reportdir = './static/reports/{}/report'.format(self.userid)

        pytest.main(['-vs', './exeCase/testcases.py', '--alluredir', '{}'.format(tempdir) ])
        os.system('allure generate {} -o {} -c {}'.format(tempdir, reportdir, reportdir))







