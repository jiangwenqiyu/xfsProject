import os
import psutil
import time
import wmi
from app import redis_store
from common import commonFunctions

data = {'taxList': [{'attrUuid': 'tax_classify', 'valueInfo': '21858'}, {'attrUuid': 'tax_code', 'valueInfo': '1060507020000000000'}, {'attrUuid': 'tax_rate', 'valueInfo': '0.13'}], 'manageList': [{'attrUuid': 'manage_area', 'valueInfo': '1001'}, {'attrUuid': 'manage_stock_period', 'valueInfo': None}, {'attrUuid': 'manage_soldout_period', 'valueInfo': None}, {'attrUuid': 'manage_cooperation', 'valueInfo': 'manage_cooperation_distribution'}, {'attrUuid': 'manage_dealmode', 'valueInfo': 'manage_dealmode_mainsellproduct'}, {'attrUuid': 'manage_sellmanageperiod', 'valueInfo': 'manage_sellmanageperiod_year'}, {'attrUuid': 'manage_outpos', 'valueInfo': 'manage_outpos_high'}, {'attrUuid': 'manage_inpos', 'valueInfo': 'manage_inpos_high'}, {'attrUuid': 'manage_season_product', 'valueInfo': 'manage_season_product_no'}], 'productUuid': '#56_res_retData.productUuid#', 'logisticsList': [{'attrUuid': 'logistics_pack', 'valueInfo': ''}, {'attrUuid': 'logistics_transport', 'valueInfo': ''}, {'attrUuid': 'logistics_restrict', 'valueInfo': ''}, {'attrUuid': 'logistics_store', 'valueInfo': ''}], 'marketingList': [{'attrUuid': 'marketing_saleplat', 'valueInfo': 'marketing_saleplat_signed,marketing_saleplat_swan'}]}
data = commonFunctions.Common().parseData(data)
print(data['productUuid'])








