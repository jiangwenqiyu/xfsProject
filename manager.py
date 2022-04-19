# coding=utf-8
#启动项
from app import app
from www import *
from flask_script import Server
from app import app,db,manager
#设置命令行启动  python3 manager.py runserver
manager.add_command("runserver",Server(use_debugger=True,use_reloader=True))
def main():
    manager.run()

if __name__ == '__main__':
    #app.run(debug=True)
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()