#-*- coding:utf-8 -*-
import csv,os,re
from common.Log import Log
log=Log()
def get_url(file,api_name):
    with open(file,"rt") as f:
        reader = csv.reader(f, delimiter=',')
        fieldnames = next(reader)
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=',')
        for row in reader:
            if row['接口名称']== api_name or row['接口标识'] == api_name :
                url=row['接口地址']
                return url

def get_apiname(file,apiID):
    with open(file,"rt") as f:
        reader = csv.reader(f, delimiter=',')
        fieldnames = next(reader)
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=',')
        for row in reader:
            if row['接口标识'] == apiID :
                apiname=row['接口名称']
                return apiname

def get_testdata(file):
    data=[]

    with open(file) as fb:
        reader=csv.reader(fb)
        columns=[[read[0],read[1],read[2],read[3],read[4:]] for read in reader]
        for column in columns[1:]:
            column[4]=[eval(word) if re.findall(r'(^int[(].+[)]$)|(^bool[(].+[)]$)',word) else word for word in column[4]]
            data.append([column[0],column[1],column[2],column[3],str(dict(zip(columns[0][4],column[4])))])
        if len(data) != 0:
            return data

def get_dataname(path):
    datapath=path.replace('testCase','testFile')
    datapath=os.path.split((os.path.splitext(datapath))[0])
    name=os.path.split(datapath[0])[-1]
    apifile=os.path.join(datapath[0],name+'.csv')
    casename=re.sub(r'test_\d*_*','',datapath[1])
    # print(casename)
    # casename=datapath[1].replace('test_','')
    casename=get_apiname(apifile,casename)
    try:
        casedatapath=os.path.join(datapath[0],casename+'.csv')
    except Exception as e:
        log.error('接口文件中不存在此接口！！！')
        return None,None,None
    if os.path.exists(casedatapath):
        return apifile,casedatapath,casename
    else:
        log.error('用例：'+casename +'的数据文件不存在！')

def Propath():
    path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path

def get_package(path):
    package=os.path.basename(os.path.split(path)[0])
    return package




if __name__ == '__main__':
    print(get_testdata('E:/IDS/idscloud_interface/testFile/is/查看资源权限信息.csv'))