# -*- coding: utf-8 -*-
from flask import request
from common.libs.helper import ops_render
from interceptors.Auth import check_login
from common.models.address import Address
from common.models.pjname import Pjname
from controllers import index_page


@index_page.route("/")
def index():
    req = request.values
    is_login = check_login()
    if is_login == False:
        return ops_render('member/login.html')

    address_query = Address.query
    address = address_query.all()

    pjname_query = Pjname.query
    pjname = pjname_query.all()


    #app.logger.info( session['uid'] )

    return ops_render( "index.html",{"address":address,"pjname":pjname} )
