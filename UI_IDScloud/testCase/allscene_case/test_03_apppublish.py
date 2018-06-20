# -*-coding:utf-8 -*-
from ddt import data,ddt
from page_objects.market_home import MarketHome
from page_objects.apppublish import Apppublish_page
from page_objects.op_home import OpHome
from page_objects.isv_home import IsvHome
from page_objects.op_appmanage import Op_Appmagage
from selenium import webdriver
import unittest
from public.get_csv import *
from datas.setting import *

log=Log()
datas = get_data(BASE_DIR+'\\datas\\add_app.csv')
@ddt
class Apppublish(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info('===================test_apppublish==============================')
        cls.ScreenPath = log.get_screenshot_path(__name__)

    def setUp(self):
        self.Mdriver=webdriver.Chrome()
        self.Mdriver.maximize_window()
        self.Mdriver.get(BASE_URL)
        self.mk=MarketHome(self.Mdriver)
        self.isv=IsvHome(self.Mdriver)
        self.Odriver=webdriver.Chrome()
        self.Odriver.maximize_window()
        self.Odriver.get(OP_URL)
        self.op=OpHome(self.Odriver)

    @data(*datas)
    def test_publishapp(self,data):
        Screen = os.path.join(self.ScreenPath, 'test_publish_%s_error.png'% data['caseNo'])
        self.mk.isv_login(EPS_name,EPS_pwd,Screen)
        self.op.Login(Screen)
        capp=Apppublish_page(self.Mdriver)
        capp.appadd(data,Screen)
        self.isv.switch_to_lastwin()
        self.isv.appmamage(Screen)
        opM=Op_Appmagage(self.Odriver)
        opM.appmanage(Screen)
        if data['amornot']!='0':
            self.isv.apply(data['appname'],Screen)
        opM.app_audit(data['appname'],Screen)
        state=self.isv.appstatecurrent(data['appname'],Screen)
        if state=='已上架':
            flag=True
            msg='%s产品上架成功' % data['appname']
            self.Mdriver.save_screenshot(os.path.join(self.ScreenPath,'publishapp_%s_pass.png' % data['caseNo']))
        else:
            flag=False
            msg='%s产品上架失败' % data['appname']
            self.Mdriver.save_screenshot(os.path.join(self.ScreenPath,'publishapp_%s_fail.png' % data['caseNo']))
        log.info(msg)
        self.assertTrue(flag,msg)

    def tearDown(self):
        Screen = os.path.join(self.ScreenPath, 'test_publishLogout_error.png')
        self.isv.Logout(Screen)
        self.Mdriver.quit()
        self.op.Logout(Screen)
        self.Odriver.quit()

    @classmethod
    def tearDownClass(cls):
        log.info('==========================END=================================')








