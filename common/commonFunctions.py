import re
import json
import jmespath
import random
import time
from app import redis_store


class OfferFunction():
    def __init__(self):
        self.func_map = dict()
        self.func_map['getRanndomInt'] = self.getRanndomInt
        self.func_map['getTimeStamp'] = self.getTimeStamp
        self.func_map['cateName'] = self.cateName


    def getRanndomInt(self):
        return random.randint(0,100000)

    def getTimeStamp(self):
        return int(time.time() * 1000)

    def cateName(self):
        return str(int(time.time() * 1000))[-6:]



class Common(OfferFunction):
    '''
    支持解析param、data、断言
    '''


    # 解析是否需要提取之前接口的数据
    def extractData(self, data):
        d = json.dumps(data, ensure_ascii=False)
        pat = '#(.*?)#'
        result = re.findall(pat, d)
        if len(result) == 0:
            return json.loads(d)

        else:
            for replaceword in result:
                jmes = replaceword.replace('#', '')
                needvalue = jmes.split('_')
                redis_key = '{}_{}'.format(needvalue[0], needvalue[1])
                jmespath_express = needvalue[2]
                redis_value = redis_store.get(redis_key)
                redis_value_json = json.loads(redis_value)
                sub_value = jmespath.search(jmespath_express, redis_value_json)
                d = d.replace('#{}#'.format(replaceword), sub_value)

            return json.loads(d)


    # 解析是否需要执行系统函数
    def offerfunc(self, data):
        d = json.dumps(data, ensure_ascii=False)
        pat = '\$(.*?)\$'
        result = re.findall(pat, d)
        if result == []:
            return json.loads(d)

        else:
            for func in result:
                func_name = func.replace('$', '')
                func_value = self.func_map[func_name]()
                d = d.replace(func, str(func_value))
            return json.loads(d)



    def parseData(self, data):
        d = data
        d = self.extractData(d)
        d = self.offerfunc(d)
        return d







