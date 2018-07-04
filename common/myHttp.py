# -*- coding:utf-8 -*-

import requests
from common.Log import Log
from common.ReadConfig import *

rc=ReadConfig()
log=Log()
headkey=rc.get_headers('key')

def get(url,params,Authonvalue=''):
    if Authonvalue=='':
        header={}
    else:
        if Authonvalue != 'om':
            headvalue = rc.get_headers('market')
        else:
            headvalue = rc.get_headers('om')
        header={headkey:headvalue}
    """
    get请求
    :return:
    """
    try:
        # 当headers传的cookies时，要把键值对id改成cookies
        response = requests.get(url, params=params,headers=header,timeout=10)
        return response
    except Exception as e:
        log.error(e)

def post(url,data,Authonvalue=''):
    if Authonvalue=='':
        header={}
    else:
        if Authonvalue != 'om':
            headvalue = rc.get_headers('market')
        else:
            headvalue = rc.get_headers('om')
        header={headkey:headvalue}
    """
    post请求
    :return:
    """
    try:
        # 当headers传的cookies时，要把键值对id改成cookies
        response = requests.post(url, data=data,timeout=10,headers=header)
        return response
    except Exception as e:
        log.error(e)

if __name__ == '__main__':
    res = get('','')
