#-*-coding:utf-8 -*-

from ddt import ddt,data
from selenium import webdriver
from page_objects.op_ordermanage import Op_Ordermanage
from page_objects.market_home import MarketHome
from page_objects.eps_home import EpsHome
from public.get_csv import *
from datas.setting import *
from public.Log import Log
import unittest
from time import sleep
log=Log()
datas=get_data(BASE_DIR+'\\datas\\buy_app.csv')

@ddt
class Buyapp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('===================test_Buyapp==============================')
        cls.ScreenPath = log.get_screenshot_path(__name__)

    def setUp(self):
        self.Mdriver=webdriver.Chrome()
        self.Mdriver.maximize_window()
        self.Mdriver.get(BASE_URL)
        self.Odriver=webdriver.Chrome()
        self.Odriver.maximize_window()
        self.Odriver.get(OP_URL)
        self.opO=Op_Ordermanage(self.Odriver)
        self.eps=EpsHome(self.Mdriver)


    @data(*datas)
    def test_buyapp(self,data):
        Screen = os.path.join(self.ScreenPath, 'test_buyapp_%s_error.png' % data['caseNo'])
        mk=MarketHome(self.Mdriver)
        mk.Login_link(Screen)
        mk.Login(data['username'],data['pwd'],Screen)
        orderNo=mk.Buyapp_page(data['appname'],data['appkind'],data['timelimit'],data['quantity'],Screen)[1]
        self.opO.Login(Screen)
        self.opO.auditorder(orderNo,data['proprotion'],Screen)
        self.eps.eps_click(Screen)
        self.eps.openapp(orderNo,Screen)
        if data['appname'] in self.eps.appnames_Saas(Screen):
            flag=True
            msg='应用 %s 购买成功，并开通' % data['appname']
            self.Mdriver.save_screenshot(os.path.join(self.ScreenPath,'buyapp_%s_pass.png' % data['caseNo']))
        else:
            flag = False
            msg='应用 %s 购买失败' % data['appname']
            self.Mdriver.save_screenshot(os.path.join(self.ScreenPath,'buyapp_%s_fail.png' % data['caseNo']))
        log.info(msg)
        self.assertTrue(flag,msg)

    def tearDown(self):
        Screen = os.path.join(self.ScreenPath, 'test_buyappLogout_error.png')
        self.opO.Logout(Screen)
        self.eps.Logout(Screen)
        self.Mdriver.quit()
        self.Odriver.quit()
    @classmethod
    def tearDownClass(cls):
        log.info('==========================END=================================')


if __name__ == '__main__':
    unittest.main()

