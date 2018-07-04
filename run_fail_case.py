from common import HTMLTestRunner_params
from common.ReadConfig import ReadConfig
from common import sendMail
from common.Log import Log
from common.get_csv import *
import unittest
import csv
log=Log()
Prodir =Propath()
def case_list(file):
    caselist=[]
    with open(file)as fb:
        reader=csv.reader(fb)
        caselists=[ read for read in reader]
        for word in caselists:
            if len(word) != 0:
                caselist.append(word[0])
    return caselist

def make_suite(caselist):
    test_suite = unittest.TestSuite()
    suite_module=[]
    casepath = Prodir + '/testCase/'
    for casename in caselist:
        discover = unittest.defaultTestLoader.discover(casepath, pattern=casename+'.py', top_level_dir=None)
        suite_module.append(discover)
    if len(suite_module) > 0:
        for suite in suite_module:
            for test_name in suite:
                test_suite.addTest(test_name)
    else:
        return None
    return test_suite

def runfailcase(file):
    caselist=case_list(file)
    suite=make_suite(caselist)
    log.info('============================TEST START============(Failcase)==================')
    report=log.get_report_path()
    fp=open(report,'wb')
    runner=HTMLTestRunner_params.HTMLTestRunner(stream=fp,
                                         title=u'接口测试报告',
                                         description=u'接口测试的所有用例的执行')
    runner.run(suite)
    fp.close()

    # sendMail.send_mail(report)
    log.info('==============================TEST END=======================================')

if __name__ == '__main__':
    failcasepath='failcaselist.csv'
    runfailcase(failcasepath)

