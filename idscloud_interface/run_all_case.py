import unittest
from common import HTMLTestRunner_params
from common.ReadConfig import ReadConfig
from common.get_csv import *
from common.Log import Log
from common import Data_clean


Prodir =Propath()
log=Log()
rc = ReadConfig()
path=rc.get_casepackage('path')
def runcase():
    log.info('============================TEST START============(all)==================')
    casepath=Prodir + path
    discover = unittest.defaultTestLoader.discover(casepath, pattern ='test_*.py', top_level_dir = None)
    if discover.countTestCases() == 0:
        log.error("没有测试用例，请先添加测试用例脚本。。。")
    else:
        report=log.get_report_path()
        fp=open(report,'wb')
        runner=HTMLTestRunner_params.HTMLTestRunner(stream=fp,
                                             title=u'接口测试报告',
                                             description=u'接口测试的所有用例的执行')
        runner.run(discover)
        fp.close()

    log.info('==============================TEST END=======================================')

if __name__ == '__main__':

    runcase()
    Data_clean







































