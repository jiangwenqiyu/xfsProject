# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect

from common.libs import UrlManager
from common.models.user import User
from app import app
from common.libs.helper import ops_render
from interceptors.Auth import check_login
from common.models.address import Address
from common.models.pjname import Pjname

index_page = Blueprint( "index_page",__name__ )

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
