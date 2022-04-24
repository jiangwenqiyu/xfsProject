from app import db
from common.models.GetTableColunmsComments import XfsTableColunmsComment
from common.models.GetColumComment import XfsColumnComment

def GetTableData():
    tableObj = XfsTableColunmsComment()
    tableName = tableObj.query.all()
    # for i in tableName:
    #     print(i.table_name,i.table_commnet)
    return tableName

def GetColumnData():
    colObj = XfsColumnComment()
    colComment = colObj.query.all()
    # for i in colComment:
    #     print(i.column_name, i.column_comment)
    return colComment

def AccordingToTableNameGetData(tableName):
    TbName = tableName
    tabObj = XfsColumnComment()
    tableData = tabObj.query.filter_by(table_name=TbName).all()
    # for i in tableData:
    #     print(i.column_name, i.column_comment)
    return tableData

if __name__ == '__main__':
    # GetColumnData()
    # GetTableData()
    AccordingToTableNameGetData('check_standard_detail')
