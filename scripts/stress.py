from locust import HttpUser, between, task
import jmespath
import os

class StressTest(HttpUser):
	wait_time = between(0,0)
	host=""
	@task(1)
	def run0(self):
		url = "http://192.168.0.105:7079/usercenter/webapi/tool/getUserPermissionInfo?jobNumber=10001897"
		with self.client.get("http://192.168.0.105:7079/usercenter/webapi/tool/getUserPermissionInfo?jobNumber=10001897", headers = {}, catch_response=True) as res:
			if res.status_code==200:
				try:
					res.success()
				except:
					res.failure(res.text)
			else:
				res.failure(res.text)
	@task(2)
	def run1(self):
		url = "http://product.t4.xinfangsheng.com/sysback/supplyareaprice/batchCreateSupplyAreaPrice?batchState=prepareing&menuId=239&buttonId=2"
		with self.client.post("http://product.t4.xinfangsheng.com/sysback/supplyareaprice/batchCreateSupplyAreaPrice?batchState=prepareing&menuId=239&buttonId=2", headers = {}, json = {}, catch_response=True) as res:
			if res.status_code==200:
				try:
					res.success()
				except:
					res.failure(res.text)
			else:
				res.failure(res.text)


