# coding=utf-8
# 查找单个键

def find(target, dictData, notFound='没找到'):
    queue = [dictData]
    while len(queue) > 0:
        data = queue.pop()
        for key, value in data.items():
            if key == target:
                return value
            elif type(value) == dict:
                queue.append(value)
    return notFound


# 有多个同名键在字典里时，可以用这个方法
def findAll(target, dictData, notFound=[]):
    queue = [dictData]
    result = []
    while len(queue) > 0:
        data = queue.pop()
        for key, value in data.items():
            if key == target:
                result.append(value)
            elif type(value) == dict:
                queue.append(value)
    if not result: result = notFound
    return result


def find_disc(will_find_dist, find_keys):
    value_found = []
    if isinstance(will_find_dist, list):  # 含有列表的值处理
        if len(will_find_dist) > 0:
            for now_dist in will_find_dist:
                found = find_disc(now_dist, find_keys)
                if found:
                    value_found.extend(found)
            return value_found
        if not isinstance(will_find_dist, dict):  # 没有字典类型的了
            return 0

        else:  # 查找下一层
            dict_key = will_find_dist.keys()
            # print (dict_key)
            for i in dict_key:
                if i == find_keys:
                    value_found.append(will_find_dist[i])
                found = find_disc(will_find_dist[i], find_keys)
                if found:
                    value_found.extend(found)

        return value_found

    # ! /usr/bin/python
    # coding:utf-8
    """ 
    @author:Bingo.he 
    @file: get_target_value.py 
    @time: 2017/12/22 
    """


def get_target_value(key, dic, tmp_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """

    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '
    if key in dic.keys():
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
    for value in dic.values():  # 传入数据不符合则对其value值进行遍历
        if isinstance(value, dict):
            get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
        elif isinstance(value, (list, tuple)):
            _get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
        return tmp_list


def _get_value(key, val, tmp_list):
    for val_ in val:
        if isinstance(val_, dict):
            get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, tmp_list)  # 传入数据的value值是列表或者元组，则调用自身


def list_all_dict(dict_a):
    if isinstance(dict_a, dict):  # 使用isinstance检测数据类型

        for x in range(len(dict_a)):
            temp_key = dict_a.keys()[x]

            temp_value = dict_a[temp_key]

            print ("%s : %s" % (temp_key, temp_value))

            list_all_dict(temp_value)  # 自我调用实现无限遍历

def gen_dict_location_extract(key, value, path=None):
    if path is None:
        path = []

    if hasattr(value, "items"):
        for k, v in value.items():
            if k == key:  # recursive exit point
                if len(path) > 0:
                    yield (v, path)
                else:   # handling root keys
                    yield (v, None)

            if isinstance(v, dict):
                path_copy = path.copy()
                # it is important to do a copy of the path for recursive calls
                # so every iteration has its own path object
                path_copy.append(k)
                yield from gen_dict_location_extract(key, v, path_copy)
            elif isinstance(v, list):
                yield from gen_dict_location_extract(key, v, path)


def call_gen_dict_location_extract(key, enumerable):
    results = []
    for result in gen_dict_location_extract(key, enumerable):
        results.append(result)
    return results