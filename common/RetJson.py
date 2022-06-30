class RetJson:
    successCode = 0
    failCode = 1


    @staticmethod
    def retContent(code, data, msg=''):

        ret = {'msg':msg,'code':code, 'data':data}
        return ret