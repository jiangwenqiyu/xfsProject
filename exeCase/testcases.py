import pytest
import allure
from exeCase.run import PyConfig

@allure.feature("测试模块")
class Test1:

    @pytest.mark.parametrize('caseInfo', PyConfig.caseInfos)
    def test_run(self, caseInfo):
        url = caseInfo['route']
        data = caseInfo['case_data']
        param = caseInfo['param']
        expected_results = caseInfo['expected_results']
        method = caseInfo['method']
        dataType = caseInfo['dataType']

