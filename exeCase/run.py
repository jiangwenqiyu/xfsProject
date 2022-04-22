import os
import pytest

class PyConfig:
    caseInfos = None



class RunPyTest:

    def __init__(self, userid, caseInfos):
        PyConfig.caseInfos = caseInfos
        self.userid = userid


    def run(self):
        # 根据用户，创建用户自己的报告目录
        if os.path.exists('./exeCase/testReport/{}'.format(self.userid)):
            pass
        else:
            os.mkdir('./exeCase/testReport/{}'.format(self.userid))

        # 判断用户下是否有临时allure目录
        if os.path.exists('./exeCase/testReport/{}/report_temp'.format(self.userid)):
            pass
        else:
            os.mkdir('./exeCase/testReport/{}/report_temp'.format(self.userid))

        if os.path.exists('./exeCase/testReport/{}/report'.format(self.userid)):
            pass
        else:
            os.mkdir('./exeCase/testReport/{}/report'.format(self.userid))

        tempdir = './exeCase/testReport/{}/report_temp'.format(self.userid)
        reportdir = './exeCase/testReport/{}/report'.format(self.userid)

        pytest.main(['-vs', './exeCase/testcases.py', '--alluredir', '{}'.format(tempdir) ])
        os.system('allure generate {} -o {} -c {}'.format(tempdir, reportdir, reportdir))







