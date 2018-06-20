import unittest
from public import HTMLTestRunner
from public import sendMail
from public.Log import Log
from datas.setting import *
from public import data_parse

Prodir =BASE_DIR
log=Log()

def runcase():
    log.info('==============================TEST START====================================')
    casepath=Prodir + CASEPATH
    discover = unittest.defaultTestLoader.discover(casepath, pattern ='test_*.py', top_level_dir = None)
    if discover.countTestCases() == 0:
        log.error("没有测试用例，请先添加测试用例脚本。。。")
    else:
        report=log.get_report_path()
        fp=open(report,'wb')

        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                             title=u'竹云城堡业务流程测试报告',
                                             description=u'竹云城堡主要业务流程覆盖测试')
        runner.run(discover)
        fp.close()

        # sendMail.send_mail(report)

    log.info('==============================TEST END=======================================')

if __name__ == '__main__':
    data_parse.parse()
    runcase()
    # clear_company()
