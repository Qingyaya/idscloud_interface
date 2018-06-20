# -*-coding:utf-8 -*-

from ddt import data,ddt
from page_objects.eps_home import EpsHome
import unittest
from public.get_csv import *
from datas.setting import *

log=Log()
datas = get_data(BASE_DIR+'\\datas\\add_self_app.csv')
@ddt
class Apppublish(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info('===================test_selfapppublish==============================')
        cls.ScreenPath = log.get_screenshot_path(__name__)

    def setUp(self):
        self.Mdriver=webdriver.Chrome()
        self.Mdriver.maximize_window()
        self.Mdriver.get(BASE_URL)
        self.eps=EpsHome(self.Mdriver)


    @data(*datas)
    def test_publishapp(self,data):
        Screen = os.path.join(self.ScreenPath, 'test_selfappadd_%s_error.png' % data['caseNo'])
        self.eps.Login(EPS_name,EPS_pwd,Screen)
        self.eps.appmanage(Screen)
        self.eps.selfapp_add(data['jointype'],data['appname'],data['logo'],data['url'],data['discript'],data['disable'],data['identfytype'],data['autosubmit'],Screen)
        appnames=self.eps.appnames_self(Screen)
        if data['appname'] in appnames:
            flag = True
            msg = '自建应用 %s 创建成功' % data['appname']
            self.Mdriver.save_screenshot(os.path.join(self.ScreenPath, 'selfappadd_%s_pass.png' % data['caseNo']))
        else:
            flag = False
            msg = '自建应用 %s 创建失败' % data['appname']
            self.Mdriver.save_screenshot(os.path.join(self.ScreenPath, 'selfappadd_%s_fail.png' % data['caseNo']))
        log.info(msg)
        self.assertTrue(flag, msg)

    def tearDown(self):
        Screen = os.path.join(self.ScreenPath, 'test_selfappaddLogout_error.png')
        self.eps.Logout(Screen)
        self.Mdriver.quit()

    @classmethod
    def tearDownClass(cls):
        log.info('==========================END=================================')




