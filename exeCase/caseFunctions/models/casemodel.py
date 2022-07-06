#encoding=utf8
import pytest
import allure
from exeCase.configPytest import PyConfig
import requests
import jmespath
from app import redis_store
from config import constance
import json
from common.commonFunctions import Common
from allure_commons._allure import Dynamic



@allure.feature("测试模块-模板替换")
class Test:

    # @allure.story('')
    @pytest.mark.parametrize('caseInfo', PyConfig.caseInfos)
    def test_run(self, caseInfo):
        header = caseInfo['header']
        url = caseInfo['route']
        data = caseInfo['case_data']
        param = caseInfo['param']
        expected_results = caseInfo['expected_results']
        method = caseInfo['method']
        dataType = caseInfo['dataType']
        case_id = caseInfo['case_id']
        coordination_id = caseInfo['coordination_id']
        Dynamic.title(caseInfo['explain'])

        # 首先对param、data、exp进行解析
        obj = Common()
        param = obj.parseData(param)
        data = obj.parseData(data)
        # 然后存入redis（断言可能也会用到这些数据）
        redis_store.setex('{}_param'.format(case_id), constance.REDIS_RES_EXPIRE, json.dumps(param, ensure_ascii=False))
        redis_store.setex('{}_data'.format(case_id), constance.REDIS_RES_EXPIRE, json.dumps(data, ensure_ascii=False))

        # with allure.step('接口:{}'.format(url)):
        #     pass
        with allure.step('路径:  {}'.format(url)):
            pass


        with allure.step('请求方法:  {}'.format(method)):
            pass

        with allure.step('param:  {}'.format(param)):
            pass

        with allure.step('入参:  {}'.format(data)):
            pass

        with allure.step('断言:  {}'.format(expected_results)):
            pass

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
            # 返回值存入redis
            redis_store.setex('{}_res'.format(case_id), constance.REDIS_RES_EXPIRE, json.dumps(res.json(), ensure_ascii=False))
            assert res.status_code == 200

            # 解析断言
            expected_results = obj.parseData(expected_results)
            for pat in expected_results:
                exp_value = expected_results[pat]
                try:
                    fact_value = jmespath.search(pat, res.json())
                except:
                    assert False, '断言获取字段失败\n断言表达式:{}\n返回的值:{}'.format(pat, res.text)

                assert exp_value == fact_value, '\n断言失败\n断言表达式::{}\n期望值:{}\n实际结果:{}'.format(pat, exp_value, fact_value)

