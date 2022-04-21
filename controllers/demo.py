# class test:
#     def test(self):
#         test = {"a" : 123,"b" : "aaa"}
#         print(test['b'])
#         return
#
#
# if __name__ == "__main__":
#     t = test()
#     t.test()


li = []
def digui(data, calc, li):

    if isinstance(data, dict):  # 字典
        for key in data:
            tab = ''
            for x in range(calc-1):
                tab += '\t'
            print('{}--{}'.format( key, calc-1))  # 打印键
            li.append('{}{}-{}'.format(tab, key, type(data[key])))

            if isinstance(data[key], dict):  # 判断这个键的值，是否还是字典或列表，是的话继续递归,不是的话，打印当前键，看下一个键
                digui(data[key], calc + 1, li)
            elif isinstance(data[key], list):
                digui(data[key], calc, li)
            else:
                pass


    elif isinstance(data, list):  # 列表
        if len(data) == 0:
            return
        else: # 如果是列表，只取一个元素，继续递归
            digui(data[0], calc+1, li)


a = {
    "disCentre": "",
    "centralBuyState": "2",
    "brandUuid": "2100003319",
    "brandName": "测试品牌",
    "productName": "wqexcz",
    "productNameType": "1",
    "helpCode": "csppwqexcz",
    "addPriceType": "2",
    "subtitle": "cs",
    "isSaleMultiUnit": "2",
    "isPurchaseMultiUnit": "2",
    "mainUnit": "maps2",
    "mainUnitDecimalsStr": 1,
    "mainUnitUuid": "2100003112",
    "tagList": [],
    "addPriceTypeStr": "比例",
    "productType": "01",
    "productTypeStr": "经销商品",
    "categoryUuid": "17063",
    "templateUuid": "2100003037",
    "specList": [[{
        "valueUuid": "2100003089",
        "valueName": "脚本属性值2",
        "position": 0,
        "valueImageKey": None,
        "officialFlag": "Y",
        "selected": True,
        "helpCode": "jbsxz2",
        "duoyinIndexs": [0,
                         2],
        "attributeUuid": "2100003057",
        "attributeName": "脚本规格属性"
    }]],
    "a": [],
    "b": "比例",
    "v": "01",
    "c": "经销商品",
    "d": "17063",
    "e": "2100003037",
    'f':{'xa':123, 'xb':{'fuck':789}}
}

# digui(a, 1, li)
#
# print(li)

a = [1,2,3,4,5,6]
print(a[0:1])








