#-*-coding:utf-8 -*-
import time
from ddt import ddt,data
from selenium import webdriver
from page_objects.eps_organization import Epsorg
from public.get_csv import *
from datas.setting import *
from public.Log import Log
import unittest
import pymysql
from random import choice

log=Log()
ScreenPath = log.get_screenshot_path(__name__)
datas=get_data(BASE_DIR+'\\datas\\org_import.csv')

@ddt
class Epsorganization(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('===================test_importorg==============================')
        Screen = os.path.join(ScreenPath, 'test_EpsorganizationLogin_error.png')
        cls.Mdriver=webdriver.Chrome()
        cls.Mdriver.maximize_window()
        cls.Mdriver.get(EPS_URL)
        cls.epsorg=Epsorg(cls.Mdriver)
        cls.epsorg.Login(EPS_name,EPS_pwd,Screen)

    def setUp(self):
        Screen = os.path.join(ScreenPath, 'test_setup_error.png')
        self.Mdriver.refresh()
        self.epsorg.intopage(Screen)

    @data(*datas)
    def test_importorg(self,data):
        Screen = os.path.join(ScreenPath, 'test_importorg_%s_error.png' % data['caseNo'])
        self.epsorg.imbutton_click(Screen)
        filepath = os.path.join(BASE_DIR, os.path.join('datas', data['file']))
        self.epsorg.im_choosefile(filepath,Screen)
        if data['result']=='error':
            try:
                errormsg=self.epsorg.impage_error(Screen)
                if errormsg==data['msg']:
                    flag = True
                    msg='页面报错信息正确：%s' % errormsg
                    self.Mdriver.save_screenshot(os.path.join(ScreenPath,'test_importorg_%s_pass.png' % data['caseNo']))
                else:
                    flag = False
                    msg='页面报错信息错误：%s ；应为：%s' % (errormsg,data['msg'])
                    self.Mdriver.save_screenshot(os.path.join(ScreenPath,'test_importorg_%s_fail.png' % data['caseNo']))
            except Exception as e:
                flag=False
                msg='没有找到页面的报错信息'
                self.Mdriver.save_screenshot(os.path.join(ScreenPath, 'test_importorg_%s_fail.png' % data['caseNo']))

        else:
            self.epsorg.impass(Screen)
            succ,fail=self.epsorg.imresult(Screen)
            dicts = xls_dict(filepath)
            succ_list=[succ for succ in dicts if succ['备注'] == u'成功']
            if int(succ) == len(succ_list) and int(fail) == len(dicts)-len(succ_list):
                flag=True
                msg='导入数据的结果成功与失败的数量与预期相同。'
                if int(fail)>0:
                    msgs = self.epsorg.im_failmsg(Screen)
                    comp = [msg for msg in msgs if msg['commit'] != msg['Msg']]
                    if len(comp) > 0:
                        flag1 = False
                        msg1 = '异常信息报错不对的共 %d 条，详细查看截图;' % len(comp)
                        self.Mdriver.save_screenshot(os.path.join(ScreenPath, 'test_imporg_%s_fail.png' % data['caseNo']))
                    else:
                        flag1 = True
                        msg1 = '异常信息报错均正确;'
                        self.Mdriver.save_screenshot(os.path.join(ScreenPath, 'test_imporg_%s_pass.png' % data['caseNo']))
                    self.epsorg.impass_click(Screen)

                    log.info(msg1)
                    self.assertTrue(flag1,msg1)
                if int(succ)>0:
                    self.epsorg.impass_click(Screen)
                    dict = choice(succ_list)
                    try:
                        self.epsorg.choose_org(dict[u'上级部门'] + '/' + dict[u'部门名称'], Screen)
                        if self.epsorg.editbutton_state(Screen) == None:
                            flag2 = True
                            msg2 = "添加的机构 %s ，添加成功" % (dict[u'上级部门'] + '/' + dict[u'部门名称'])
                            self.Mdriver.save_screenshot(os.path.join(ScreenPath, 'test_imporg_%s_pass.png' % data['caseNo']))
                        else:
                            flag2 = False
                            msg2 = "没有找到添加的机构 %s ，添加失败" % (dict[u'上级部门'] + '/' + dict[u'部门名称'])
                            self.Mdriver.save_screenshot(os.path.join(ScreenPath, 'test_imporg_%s_fail.png' % data['caseNo']))
                    except:
                        flag2 = False
                        msg2 = "没有找到添加的机构 %s ，添加失败" % (dict[u'上级部门'] + '/' + dict[u'部门名称'])
                        self.Mdriver.save_screenshot(os.path.join(ScreenPath, 'test_imporg_%s_fail.png' % data['caseNo']))

                    log.info(msg2)
                    self.assertTrue(flag2,msg2)

            else:
                flag=False
                msg='导入数据的结果与预期结果不同。'
                self.Mdriver.save_screenshot(os.path.join(ScreenPath, 'test_imporg_%s_fail.png' % data['caseNo']))
            self.epsorg.impass_click(Screen)
            log.info(msg)
            self.assertTrue(flag,msg)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        Screen = os.path.join(ScreenPath, 'test_EpsorganizationLogout_error.png')
        cls.epsorg.Logout(Screen)
        cls.Mdriver.quit()
        log.info('==========================END=================================')

if __name__ == '__main__':
    unittest.main()