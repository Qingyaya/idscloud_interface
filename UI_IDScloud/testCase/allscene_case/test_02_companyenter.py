# -*-coding:utf-8 -*-
from page_objects.market_home import MarketHome
from page_objects.isv_home import IsvHome
from page_objects.op_home import OpHome
from selenium import webdriver
import unittest,os
from public.Log import Log
from datas.setting import *
from time import sleep
log=Log()
class Companyenter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Screenshot = log.get_screenshot_path(__name__)
        log.info('===================test_Companyenter==============================')
        cls.Mdriver=webdriver.Chrome()
        cls.Mdriver.maximize_window()
        cls.Mdriver.get(BASE_URL)
        cls.Odriver=webdriver.Chrome()
        cls.Odriver.maximize_window()
        cls.mk=MarketHome(cls.Mdriver)
        cls.isv=IsvHome(cls.Mdriver)


    def test_companyenter(self):
        Screen = os.path.join(self.Screenshot, 'test_companyenter_error.png')
        self.mk.isv_login(EPS_name,EPS_pwd,Screen)
        self.isv.companyenter(Screen)
        self.Odriver.get(OP_URL)
        op=OpHome(self.Odriver)
        op.isv_audit(Screen)
        op.Logout(Screen)
        self.mk.isv_click(Screen)
        sleep(2)
        if self.isv.company_details(Screen)== ISV_Companyname:
            flag=True
            msg='服务商已成功入驻'
            self.Mdriver.save_screenshot(os.path.join(self.Screenshot,'companycheck_pass.png'))
        else:
            flag=False
            msg='服务商入驻失败'
            self.Mdriver.save_screenshot(os.path.join(self.Screenshot,'companycheck_fail.png'))
        log.info(msg)
        self.assertTrue(flag,msg)
        self.isv.Logout(Screen)

    @classmethod
    def tearDownClass(cls):
        cls.Mdriver.quit()
        cls.Odriver.quit()
        log.info('================================END==================================')




