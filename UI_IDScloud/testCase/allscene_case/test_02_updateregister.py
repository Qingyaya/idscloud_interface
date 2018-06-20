# -*-coding:utf-8 -*-
from page_objects.market_home import MarketHome
from page_objects.op_home import OpHome
from page_objects.eps_home import EpsHome
import unittest
from ddt import data,ddt
from public.get_csv import *
from datas.setting import *

log = Log()
ScreenPath = log.get_screenshot_path(__name__)
datas=get_data(DATA_DIR+'\\registerupdate.csv')

@ddt
class UpdateRegiste(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info('===================test_updateregistercompany==============================')

    def setUp(self):
        self.Mdriver = webdriver.Chrome()
        self.Mdriver.maximize_window()
        self.Odriver = webdriver.Chrome()
        self.Odriver.maximize_window()
        self.Mdriver.get(BASE_URL)
        self.mk = MarketHome(self.Mdriver)
        self.eps = EpsHome(self.Mdriver)
        self.Odriver.get(OP_URL)
        self.op = OpHome(self.Odriver)

    @data(*datas)
    def test_updateregister(self,data):
        Screen = os.path.join(ScreenPath, 'test_updateregister_%s_error.png' % data['caseNo'])
        self.mk.eps_login(EPS_name, EPS_pwd, Screen)
        self.eps.homepage(Screen)
        self.eps.regiseter_update(Screen)
        self.eps.register(data['Name'],data['No'],data['Img'],Screen)
        self.op.Login(Screen)
        self.op.eps_find(data['Name'],'待审批',Screen)
        self.op.eps_audit(Screen)
        self.op.eps_find(data['Name'], '已通过', Screen)
        text = self.eps.company_details(Screen)[1]
        if u'已认证成为企业用户' in text:
            flag = True
            msg = '企业认证成功'
            self.Mdriver.save_screenshot(os.path.join(ScreenPath, 'updateregister_pass.png'))
        else:
            flag = False
            msg = '企业认证失败'
            self.Mdriver.save_screenshot(os.path.join(ScreenPath, 'updateregister_fail.png'))
        log.info(msg)
        self.assertTrue(flag, msg)

    def tearDown(self):
        Screen = os.path.join(ScreenPath, 'test_logout_error.png')
        self.eps.Logout(Screen)
        self.op.Logout(Screen)
        self.Mdriver.quit()
        self.Odriver.quit()

    @classmethod
    def tearDownClass(cls):
        log.info('==========================END=================================')

    if __name__ == "__main__":
        unittest.main()