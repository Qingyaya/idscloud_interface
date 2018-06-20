#-*- coding:utf-8 -*-
import csv,os
from public.Log import Log
import xlrd

log=Log()

def Propath():
    path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path

def get_package(path):
    package=os.path.basename(os.path.split(path)[0])
    return package

def get_data(path):
    with open(path,'r') as f:
        reader=csv.DictReader(f)
        columns=[dict(read) for read in reader]
        return columns
def xls_dict(path):
    xls=xlrd.open_workbook(path)
    table=xls.sheet_by_index(0)
    culumns=[dict(zip(table.row_values(1),table.row_values(i))) for i in range(2,table.nrows)]
    return culumns

def xls_row_len(path):
    xls=xlrd.open_workbook(path)
    row_len=xls.sheet_by_index(0).nrows
    return row_len




if __name__ == '__main__':
    print(xls_dict('E:\\UI_IDScloud\\datas\\org_importfile\\testuiregister-正常.xls'))