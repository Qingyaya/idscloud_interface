# -*- coding: utf-8 -*-
from datas.setting import *
from page_objects.market_home import MarketHome
import unittest
from public.Log import Log
from selenium import webdriver

log = Log()


class Register(unittest.TestCase):
    def setUp(self):
        self.Screenshot = log.get_screenshot_path(__name__)
        log.info('===================test_register==============================')
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)

    def test_register(self):
        self.mk=MarketHome(self.driver)
        Screen=os.path.join(self.Screenshot,'test_redister_error.png')
        self.mk.Register(Screen)
        #登录验证
        self.mk.Login( EPS_name,EPS_pwd,Screen)
        if  self.mk.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/ul/li[9]/div[1]/span/span',Screen).text == EPS_name:
            flag=True
            self.driver.save_screenshot(os.path.join(self.Screenshot,'test_register_pass.png'))
            msg='注册成功，并登陆成功'
        else:
            flag = False
            self.driver.save_screenshot(os.path.join(self.Screenshot,'test_register_fail.png'))
            msg='注册失败'
        log.info(msg)
        self.assertTrue(flag,msg)

    def tearDown(self):
        self.mk.Logout(os.path.join(self.Screenshot,'logout_error.png'))
        self.driver.quit()
        log.info('==========================END=================================')


if __name__ == "__main__":
    unittest.main()

