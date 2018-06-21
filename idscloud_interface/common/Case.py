# -*- coding:utf-8 -*-
import os,csv

def datacsv(path,param):
    u"""    创建接口数据文件    """
    with open(path, 'w', newline='') as f:
        wr = csv.writer(f)
        list = [r'caseID', r'caseName', r'assertKey', r'assertValue']
        wr.writerow(list + param)

def caseScript(path,operationId,interfaceName,methond,pk):
    # 创建接口测试文件
    with open(path, 'w', encoding='utf-8') as c:
        ja = r'''
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

class %(classname)s(unittest.TestCase):
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

    def %(classname)s(self):
        u"""%(dis)s"""
        self.re=myHttp.%(methond)s(self.url,self.params,package)
        checkResult().ck(self.caseId,self.caseName,self.assertKey,self.assertValue,self.params,self.url,self.re)

    def tearDown(self):          
        self.log.build_end_line(self.caseId +":"+ self.caseName)

if __name__ == "__main__":
    unittest.main()
            '''
        jas = ja % dict(classname='test_' + operationId,
                        dis=pk+'_' + interfaceName,
                        methond=methond
                        )
        c.write(jas)


if __name__ == '__main__':
    with open('E:\\IDS\\idscloud_interface\\testFile\\isv\\case.csv','r') as f:
        reader=csv.reader(f)
        reads=[read for read in reader]
        for read in reads[1:]:
            operationId=read[0]
            interfaceName=read[1]
            interfaceAddress=read[2]
            methond=read[3]
            param=read[4]
            # caseScript('E:\\IDS\\idscloud_interface\\testCase\\isv\\test_'+ operationId+'.py', operationId, interfaceName, methond, 'isv')
            datacsv('E:\\IDS\\idscloud_interface\\testFile\\isv\\'+interfaceName+'.csv', eval(param))