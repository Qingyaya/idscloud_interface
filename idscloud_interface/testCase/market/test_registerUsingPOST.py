
#-*-coding:utf-8-*-
import unittest
import paramunittest
import pymysql

from common import myHttp
from common.ReadConfig import ReadConfig
from common.get_csv import *
from common.Log import Log
from common.checkResult import checkResult
import os

apifile,datapath,casename=get_dataname(os.path.abspath(__file__))
load_csv=get_testdata(datapath)
package=get_package(os.path.abspath(__file__))
@paramunittest.parametrized(*load_csv)

class test_registerUsingPOST(unittest.TestCase):
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
        self.rc=ReadConfig()
        self.db = pymysql.connect(self.rc.get_db('ip'),self.rc.get_db('username'),self.rc.get_db('password'), self.rc.get_db('db'))
        self.cursor = self.db.cursor()
        self.cursor.execute("DELETE FROM tb_user where mobile='15210925036' ")
        self.db.commit()


    def test_registerUsingPOST(self):
        u"""castle_云超市用户注册"""
        self.re=myHttp.post(self.url,self.params,package)
        checkResult().ck(self.caseId,self.caseName,self.assertKey,self.assertValue,self.params,self.url,self.re)

        self.cursor.execute("DELETE FROM tb_user where mobile='15210925036' ")
        self.db.commit()
        self.db.close()


    def tearDown(self):          
        self.log.build_end_line(self.caseId +":"+ self.caseName)

if __name__ == "__main__":
    unittest.main()
            