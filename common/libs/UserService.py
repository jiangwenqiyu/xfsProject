import random
import string,hashlib,base64


class UserService:

    @staticmethod
    def geneAuthCode(user_info = None):
        m = hashlib.md5()
        str = "%s-%s-%s-%s"%(user_info.id,user_info.user_id,user_info.state,user_info.password)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    #返回md5加密密码
    @staticmethod
    def genePwd(pwd,salt):
        m = hashlib.md5()
        str = "%s-%s"%(base64.encodebytes(pwd.encode("utf-8")),salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    #返回密码key
    @staticmethod
    def getsalt(length = 16):
        keylist = [random.choice(string.ascii_letters+string.digits) for i in range(length)]
        return ("".join(keylist))