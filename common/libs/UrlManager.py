from app import app
from common.libs.datahelper import getCurrentTime
import os
class UrlManager(object):
    @staticmethod
    def buildUrl(path):
        config_domain = app.config['DOMAIN']
        return "%s%s"%(config_domain['www'],path)

    @staticmethod
    def buildStaticUrl(path):
        path = "/static" + path+"?ver="+UrlManager.getReleaseVersion()
        return UrlManager.buildUrl(path)

#如果找到RELEASE_PATH所在版本文件，则不在进行js版本更新，显示版本文件内版本号,用于版本发布管理，开发环境使用时间戳进行js更新
    @staticmethod
    def getReleaseVersion():

        ver = "%s" % (getCurrentTime("%Y%m%d%H%M%S%f"))

        release_path = app.config.get('RELEASE_PATH')
        if release_path and os.path.exists(release_path):
            with open(release_path,'r') as f:
                ver=f.readline()

        return ver