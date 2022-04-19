from testmain.run import baseRequests
from app import app
import json
def runway(method,data):
    data = json.loads(data)
    req = baseRequests()
    url = "http://192.168.0.121:8050/cmps/srm/Supplier/querySupplierInfo"

    val = data['supplierNos'].split(",")
    data['supplierNos'] = val


    res = req.run_main(method,url,json.dumps(data))

    return res