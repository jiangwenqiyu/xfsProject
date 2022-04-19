# coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
import requests
import json
class baseRequests():
    def send_get(self,url,data):
        response = requests.get(url=url,params=data)
        res = response.text
        return res
    def send_post(self,url,data):
      #  print(type(data))
      #  print(data)
        print("here---------------")
    #supplierNos
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        #    "Content-Type": "application/json;charset=UTF-8"
        }

        response = requests.post(url=url,data=data,headers=headers)
        res = response.text
        return res
    def run_main(self,method,url,data):
        if method == 'get':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
      #  try:
            res = json.loads(res)
      #  except:
       #     print("not json")
        #print("--->", res)
        return res