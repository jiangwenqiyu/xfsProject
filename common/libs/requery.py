from common.models.coordination import Coordination
from common.models.supplier import Supplier
from app import app



def requery(pjname):
    if pjname == "Supplier":
        query=Supplier.query
        data_list = query.all()
        return data_list

    elif pjname == "Coordination":
        query=Coordination.query
        data_list = query.all()
        return data_list
