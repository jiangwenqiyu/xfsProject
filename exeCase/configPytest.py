import os
import pytest
import shutil
import requests
import json

class PyConfig:
    caseInfos = []



class RunPyTest:

    def __init__(self):
        self.userid = None
        self.path = None
        self.caseInfos = None
        self.reportbackContent = None


    def diyReport(self):
        # 改title
        with open('{}/static/reports/{}_{}/report/index.html'.format(self.path, self.userid, self.reportbackContent), 'r') as f1:
            file = f1.read()
            file = file.replace('Allure Report', '鑫方盛测试平台-测试报告')

            with open('{}/static/reports/{}_{}/report/index.html'.format(self.path, self.userid, self.reportbackContent), 'w', encoding='utf8') as f2:
                f2.write(file)

        # 改主页标题
        with open('{}/static/reports/{}_{}/report/widgets/summary.json'.format(self.path, self.userid, self.reportbackContent), 'r') as f1:
            file = json.loads(f1.read())
            file['reportName'] = '鑫方盛测试中心'
            with open('{}/static/reports/{}_{}/report/widgets/summary.json'.format(self.path, self.userid, self.reportbackContent), 'w', encoding='utf8') as f2:
                f2.write(json.dumps(file))

        # 改标题栏
        with open('{}/static/reports/{}_{}/report/app.js'.format(self.path, self.userid, self.reportbackContent), 'r', encoding='utf8') as f1:
            file = f1.read()
            file = file.replace('测试套', '方法路径')
            with open('{}/static/reports/{}_{}/report/app.js'.format(self.path, self.userid, self.reportbackContent), 'w', encoding='utf8') as f2:
                f2.write(file)

        with open('{}/static/reports/{}_{}/report/plugins/behaviors/index.js'.format(self.path, self.userid, self.reportbackContent), 'r', encoding='utf8') as f1:
            file = f1.read()
            file = file.replace('功能', '模块用例结果')
            with open('{}/static/reports/{}_{}/report/plugins/behaviors/index.js'.format(self.path, self.userid, self.reportbackContent), 'w', encoding='utf8') as f2:
                f2.write(file)

        with open('{}/static/reports/{}_{}/report/plugins/behaviors/index.js'.format(self.path, self.userid, self.reportbackContent), 'r', encoding='utf8') as f1:
            file = f1.read()
            file = file.replace('包', '用例总览')
            with open('{}/static/reports/{}_{}/report/plugins/behaviors/index.js'.format(self.path, self.userid, self.reportbackContent), 'w', encoding='utf8') as f2:
                f2.write(file)




    def run(self, userid, caseInfos, path, reportbackContent):
        self.userid = userid
        self.path = path
        self.caseInfos = caseInfos
        self.reportbackContent = reportbackContent
        PyConfig.caseInfos = caseInfos


        # 创建报告目录
        if os.path.exists('{}/static/reports'.format(path)):
            pass
        else:
            os.mkdir('{}/static/reports'.format(path))

        # 根据用户，创建用户自己的报告目录.如果有历史数据，先删除历史数据
        os.mkdir('{}/static/reports/{}_{}'.format(path, self.userid, reportbackContent))
        # if os.path.exists('{}/static/reports/{}'.format(path, self.userid)):
        #     shutil.rmtree('{}/static/reports/{}'.format(path, self.userid))
        #     os.mkdir('{}/static/reports/{}'.format(path, self.userid))
        # else:
        #     os.mkdir('{}/static/reports/{}'.format(path, self.userid))

        # 判断用户下是否有临时allure目录
        os.mkdir('{}/static/reports/{}_{}/report_temp'.format(path, self.userid, reportbackContent))
        # if os.path.exists('{}/static/reports/{}/report_temp'.format(path, self.userid)):
        #     shutil.rmtree('{}/static/reports/{}/report_temp'.format(path, self.userid))
        #     os.mkdir('{}/static/reports/{}/report_temp'.format(path, self.userid))
        # else:
        #     os.mkdir('{}/static/reports/{}/report_temp'.format(path, self.userid))

        os.mkdir('{}/static/reports/{}_{}/report'.format(path, self.userid, reportbackContent))
        # if os.path.exists('{}/static/reports/{}/report'.format(path, self.userid)):
        #     shutil.rmtree('{}/static/reports/{}/report'.format(path, self.userid))
        #     os.mkdir('{}/static/reports/{}/report'.format(path, self.userid))
        # else:
        #     os.mkdir('{}/static/reports/{}/report'.format(path, self.userid))

        tempdir = '{}/static/reports/{}_{}/report_temp'.format(path, self.userid, reportbackContent)
        reportdir = '{}/static/reports/{}_{}/report'.format(path, self.userid, reportbackContent)

        # 根据用户生成对应的执行测试用例文件
        if os.path.exists('{}/exeCase/caseFunctions'.format(path)):
            pass
        else:
            os.mkdir('{}/exeCase/caseFunctions'.format(path))

        if os.path.exists('{}/exeCase/caseFunctions/{}'.format(path, self.userid)):
            pass
        else:
            os.mkdir('{}/exeCase/caseFunctions/{}'.format(path, self.userid))

        # 生成对应的文件
        with open('{}/exeCase/caseFunctions/models/casemodel.py'.format(path), 'r', encoding='utf8') as f:
            head = f.readlines()[0:12]
        head_final = ''
        for h in head:
            head_final += h

        with open('{}/exeCase/caseFunctions/models/casemodel.py'.format(path), 'r', encoding='utf8') as f:
            body = f.readlines()[14:]

        content = ''
        calc = 1
        for name in caseInfos:
            for i in body:
                if "测试模块-模板替换" in i:
                    content += i.replace('@allure.feature("测试模块-模板替换")', '@allure.feature("{}")'.format(name))
                elif "PyConfig.caseInfos" in i:
                    content += i.replace("@pytest.mark.parametrize('caseInfo', PyConfig.caseInfos)", "@pytest.mark.parametrize('caseInfo', PyConfig.caseInfos{})".format('["{}"]'.format(name)))
                elif 'class Test' in i:
                    content += i.replace('class Test:', 'class Test{}:'.format(calc))

                else:
                    content += i
            content += '\n\n'
            calc += 1

        with open('{}/exeCase/caseFunctions/{}/testcases.py'.format(path, self.userid), 'w', encoding='utf8') as f:
            f.write(head_final + '\n\n' + content)


        #执行pytest
        pytest.main(['-vs',  '{}/exeCase/caseFunctions/{}/testcases.py'.format(path, self.userid), '--alluredir', '{}'.format(tempdir) ])
        # 生成报告
        os.system('allure generate {} -o {} -c {}'.format(tempdir, reportdir, reportdir))
        print('allure generate {} -o {} -c {}'.format(tempdir, reportdir, reportdir))

        # 生成报告后，改下基础信息
        self.diyReport()











