import pytest
import allure
from exeCase.configPytest import PyConfig
import requests
import jmespath


@allure.feature("测试模块")
class Test1:

    @pytest.mark.parametrize('caseInfo', PyConfig.caseInfos)
    def test_run(self, caseInfo):
        # print(id(PyConfig.caseInfos), '****', PyConfig.caseInfos)
        # return 0
        header = {}
        url = caseInfo['route']
        data = caseInfo['case_data']
        param = caseInfo['param']
        expected_results = caseInfo['expected_results']
        method = caseInfo['method']
        dataType = caseInfo['dataType']

        try:
            if method.lower() == 'get':
                res = requests.get(url, headers = header, params=param)
            else:

                if dataType.lower() == 'data':
                    res = requests.post(url, headers = header, params=param, data = data)
                else:
                    res = requests.post(url, headers = header, params=param, json = data)

        except Exception as e:
            assert False, '\n请求失败\nurl:{}\ndata:{}\nException:{}'.format(url, data, e)

        else:

            assert res.status_code == 200

            for pat in expected_results:
                exp_value = expected_results[pat]
                fact_value = jmespath.search(pat, res.json())

                assert exp_value == fact_value, '\n断言失败\n断言表达式::{}\n期望值:{}\n实际结果:{}'.format(pat, exp_value, fact_value)

