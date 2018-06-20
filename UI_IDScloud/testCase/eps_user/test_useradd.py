#-*-coding:utf-8 -*-
import time
from ddt import ddt,data
from selenium import webdriver
from page_objects.eps_user import Epsuser
from public.get_csv import *
from datas.setting import *
from public.Log import Log
import unittest
import pymysql
from random import choice

log=Log()
ScreenPath = log.get_screenshot_path(__name__)
datas=get_data(BASE_DIR+'\\datas\\add_user.csv')

@ddt
class EpsUseradd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('===================test_org==============================')
        Screen = os.path.join(ScreenPath, 'test_EpsuserLogin_error.png')
        cls.Mdriver=webdriver.Chrome()
        cls.Mdriver.maximize_window()
        cls.Mdriver.get(EPS_URL)
        cls.epsuser=Epsuser(cls.Mdriver)
        cls.epsuser.Login(EPS_name,EPS_pwd,Screen)

    def setUp(self):
        Screen = os.path.join(ScreenPath, 'test_setup_error.png')
        self.Mdriver.refresh()
        self.epsuser.intopage(Screen)

    @data(*datas)
    def test_adduser(self,data):
        Screen = os.path.join(ScreenPath, 'test_adduser_%s_error.png' % data['caseNo'])
        self.epsuser.adduser_click(Screen)
        self.epsuser.addpage_username(data['username'],Screen)
        self.epsuser.addpage_mobile(data['mobile'],Screen)
        self.epsuser.addpage_password(data['password'],Screen)
        self.epsuser.addpage_sex(data['sex'],Screen)
        self.epsuser.addpage_mail(data['mail'],Screen)
        self.epsuser.addpage_choose_click(Screen)
        self.epsuser.org_choose(data['org'],Screen)
        self.epsuser.addpage_workerid(data['workerno'],Screen)
        self.epsuser.addpage_job(data['job'],Screen)
        self.epsuser.addpage_save(Screen)



    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        Screen = os.path.join(ScreenPath, 'test_EpsuserLogout_error.png')
        cls.epsuser.Logout(Screen)
        cls.Mdriver.quit()
        log.info('==========================END=================================')


if __name__ == '__main__':
    unittest.main()