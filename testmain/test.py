# coding=utf-8
import json

import requests
from testmain.Util import findkv
from testmain import run
'''
url = "http://192.168.0.121:8050/cmps/srm/Supplier/querySupplierInfo"

data = {'supplierNos':[12085,12085]}
#test = run.runmain("post",url,data)
#response = requests.post(url=url,params={'supplierNos':12085})
req = run.baseRequests()
res = req.run_main('post',"http://192.168.0.121:8050/cmps/srm/Supplier/querySupplierInfo",data)

print(res)
'''
data = {'supplierNos':["12085"]}
print(type(json.dumps(data)))
req = run.baseRequests()
print(data)
res = req.run_main('post', "http://192.168.0.121:8050/cmps/srm/Supplier/querySupplierInfo", json.dumps(data))
print(res)


