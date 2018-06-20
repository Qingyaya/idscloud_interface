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
datas=get_data(BASE_DIR+'\\datas\\org_delet.csv')
@ddt
class Epsorganization_delete(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('===================test_orgdelete==============================')
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
    def test_orgdelete(self,data):
        Screen = os.path.join(ScreenPath, 'test_orgdelet_%s_error.png'% data['caseNo'])
        if data['orgparent']!='':
            self.epsorg.choose_org(data['orgparent'],Screen)
            if data['orgname']!='':
                self.epsorg.choose_childorg(data['orgname'],Screen)
            else:
                self.epsorg.choose_allchildorg(Screen)
            self.epsorg.delebutton(Screen)
            self.epsorg.deleok(Screen)
        msg=self.epsorg.delemsg(Screen)
        if msg==data['msg']:
            flag=True
            msg='机构：%s 删除成功' %(data['orgparent']+'/' +data['orgname'])
            self.Mdriver.save_screenshot(os.path.join(ScreenPath,'test_deletorg_%s_pass.png' % data['caseNo']))
        else:
            flag = False
            msg='机构：%s 删除失败' %(data['orgparent']+'/' +data['orgname'])
            self.Mdriver.save_screenshot(os.path.join(ScreenPath,'test_deletorg_%s_fail.png' % data['caseNo']))

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