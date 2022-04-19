import pymysql

class recursor:
    def Recursor(self):
     #   db = pymysql.connect('192.168.0.129','root','xfs123456','xfstestpj')
        db =pymysql.connect(host='192.168.0.129',
                     user='root',
                     password='xfs123456',
                     database='xfstestpj')
        c = db.cursor()
        return c
