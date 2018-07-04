
#-*-coding:utf-8-*-
import unittest
import paramunittest
from common import myHttp
from common.get_csv import *
from common.Log import Log
from common.checkResult import checkResult
import os

apifile,datapath,casename=get_dataname(os.path.abspath(__file__))
load_csv=get_testdata(datapath)
package=get_package(os.path.abspath(__file__))
@paramunittest.parametrized(*load_csv)

class test_updateSorgSequenceUsingPOST(unittest.TestCase):
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
        self.params['json']='{"95bdb194-e84b-4b66-b04d-55a562560cfc":86,"03715d2e-6a03-4d46-857c-59be511e9b26":83}'

    def test_updateSorgSequenceUsingPOST(self):
        u"""is_修改序列号"""
        self.re=myHttp.post(self.url,self.params,package)
        checkResult().ck(self.caseId,self.caseName,self.assertKey,self.assertValue,self.params,self.url,self.re)

    def tearDown(self):          
        self.log.build_end_line(self.caseId +":"+ self.caseName)

if __name__ == "__main__":
    unittest.main()
            