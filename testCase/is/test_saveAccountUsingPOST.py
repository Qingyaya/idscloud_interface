
#-*-coding:utf-8-*-
import unittest
import paramunittest
import pymysql
from common import myHttp
from common.get_csv import *
from common.Log import Log
from common.checkResult import checkResult
import os
from common.ReadConfig import ReadConfig

apifile,datapath,casename=get_dataname(os.path.abspath(__file__))
load_csv=get_testdata(datapath)
package=get_package(os.path.abspath(__file__))
@paramunittest.parametrized(*load_csv)

class test_saveAccountUsingPOST(unittest.TestCase):
    def setParameters(self,caseId,caseName,assertKey,assertValue,params):
        self.caseId=caseId
        self.caseName=caseName
        self.assertKey=assertKey
        self.assertValue=assertValue
        self.params=eval(params)

    def setUp(self):
        self.url=get_url(apifile,casename)
        self.log=Log()
        self.log.build_start_line(self.caseId+ ":"+ self.caseName)
        self.params['json']= [{"uid":"891b4077-1fbe-4dce-91c8-062ca427b542","EntityID":"1318e07a7cb54a379092577af7fa2bee","account":"180703154801873","sid":0,"status":"","createtime":"","type":0,"avatar":"","SpCode":"","description":"","loginName":"","displayName":"","companyid":"","run":"","appName":"","password":"","isFirstLogin":1,"accountStatus":1}]
        self.rc = ReadConfig()
        db = pymysql.connect(self.rc.get_db('ip'),self.rc.get_db('username'),self.rc.get_db('password'), self.rc.get_db('db'))
        cursor = db.cursor()
        cursor.execute("SELECT usr_id FROM tb_user WHERE mobile = '13212211342' ")
        self.params['json'][0]['uid']=(cursor.fetchone())[0]
        cursor.execute("SELECT login_name FROM tb_user WHERE mobile = '13212211342' ")
        self.params['json'][0]['account'] = (cursor.fetchone())[0]
        self.params['json']=str(self.params['json'])
        db.close()


    def test_saveAccountUsingPOST(self):
        u"""is_Oauth2.0分配账号"""
        self.re=myHttp.post(self.url,self.params,package)
        checkResult().ck(self.caseId,self.caseName,self.assertKey,self.assertValue,self.params,self.url,self.re)

    def tearDown(self):          
        self.log.build_end_line(self.caseId +":"+ self.caseName)

if __name__ == "__main__":
    unittest.main()
            