
#-*-coding:utf-8-*-
import unittest
import paramunittest
from common import myHttp
from common.get_csv import *
from common.Log import Log
from common.checkResult import checkResult
from common.ReadConfig import ReadConfig
import os,pymysql

apifile,datapath,casename=get_dataname(os.path.abspath(__file__))
load_csv=get_testdata(datapath)
package=get_package(os.path.abspath(__file__))
@paramunittest.parametrized(*load_csv)

class test_registcompanyUsingPOST(unittest.TestCase):
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

    def test_registcompanyUsingPOST(self):
        u"""eps_企业实名认证"""
        self.re=myHttp.post(self.url,self.params,package)
        checkResult().ck(self.caseId,self.caseName,self.assertKey,self.assertValue,self.params,self.url,self.re)

        self.rc=ReadConfig()
        db = pymysql.connect(self.rc.get_db('ip'), self.rc.get_db('username'), self.rc.get_db('password'),
                             self.rc.get_db('db'))
        cursor = db.cursor()
        cursor.execute('DELETE from ids_consume_company WHERE NAME="testGG" ')
        db.commit()
        db.close()

    def tearDown(self):
        self.log.build_end_line(self.caseId +":"+ self.caseName)

if __name__ == "__main__":
    unittest.main()
            