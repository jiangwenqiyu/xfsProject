from flask import Blueprint, request, jsonify
from common.libs.helper import ops_render
from interceptors.Auth import check_login
from flask import session
import os


api_stress = Blueprint('stress', __name__)



@api_stress.route('/stress', methods=['GET'])
def stress():
    print(session.keys(), '****************************')
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')



    return ops_render('stress/stressTest.html')





@api_stress.route('/generateScript', methods = ['POST'])
def test():
    '''
    接收：data:[]
    :return:
    '''
    data = request.get_json()
    urls = data['data']
    print(urls)
    try:
        generate(urls)
    except Exception as e:
        return jsonify(status = '1', msg=str(e))

    return jsonify(status = '0', msg='生成脚本成功')


@api_stress.route('/exeScript', methods = ['POST'])
def test1():
    # 重启locust服务
    os.system('sudo systemctl restart locust.service')

    return jsonify(status = '0', msg='服务重启成功！')


# urls = [('http://127.0.0.1:5000/stress', 'post', 'data', '{1}', '{2}', {'int_a':789, 'int_abc':111}), ('http://192.168.0.105:7079/usercenter/webapi/tool/getUserPermissionInfo?jobNumber=10001897', 'post', 'json', '{3}', '{3}', {'string_ret.status':'2'})]

def generate(urls):

    word = ''
    word += 'from locust import HttpUser, between, task\n'
    word += 'import jmespath\n'
    word += 'import os\n\n'
    word += 'class StressTest(HttpUser):\n\twait_time = between(0,0)\n\thost=""\n'
    for i in range(len(urls)):
        word += '\t@task({})\n'.format(urls[i][6])
        word += '\tdef run{}(self):\n'.format(i)
        word += '\t\turl = "{}"\n'.format(urls[i][0])
        if urls[i][1].lower() == 'post':
            if urls[i][2].lower() == 'data':
                word += '\t\twith self.client.post("{}", headers = {}, data = {}, catch_response=True) as res:\n'.format(urls[i][0], urls[i][3], urls[i][4])
            else:
                word += '\t\twith self.client.post("{}", headers = {}, json = {}, catch_response=True) as res:\n'.format(urls[i][0], urls[i][3], urls[i][4])
        else:
            word += '\t\twith self.client.get("{}", headers = {}, catch_response=True) as res:\n'.format(urls[i][0], urls[i][3])

        word += '\t\t\tif res.status_code==200:\n'

        if urls[i][5] != '{}':

            word += '\t\t\t\ttry:\n'
            for key in urls[i][5]:
                __key = key.split('_')
                print(key, '***************************')
                if __key [0] == 'int':
                    word += '\t\t\t\t\tassert jmespath.search("{}", res.json()) == {}\n'.format(__key[1], urls[i][5][key])
                else:
                    word += '\t\t\t\t\tassert jmespath.search("{}", res.json()) == "{}"\n'.format(__key[1], urls[i][5][key])
            word += '\t\t\t\t\tres.success()\n'
            word += '\t\t\t\texcept:\n'
            word += '\t\t\t\t\tres.failure(res.text)\n'
        else:
            word += '\t\t\t\tres.success()\n'
        word += '\t\t\telse:\n'
        word += '\t\t\t\tres.failure(res.text)\n'
    word += '\n\n'

    print(word)

    with open('./scripts/stress.py', 'w') as f:
        f.write(word)








