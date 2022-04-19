# conding=utf-8
import configparser
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)


def readini(paramheader, parambody):
    base_path = os.path.abspath(os.path.dirname(os.getcwd()))
    sys.path.append(base_path)
    file_path = "../../config/conf.ini"
    r = configparser.ConfigParser()
    r.read(file_path)
    f = r.get(paramheader, parambody)
    return f

#if __name__ == "__main__":
 #   print(readini('url','SUPPLIER_url'))