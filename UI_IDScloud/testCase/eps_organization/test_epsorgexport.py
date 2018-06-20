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
class Epsorganization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info('===================test_export==============================')
        Screen = os.path.join(ScreenPath, 'test_EpsorganizationLogin_error.png')
        cls.Mdriver=webdriver.Chrome(chrome_options=Options)
        cls.Mdriver.maximize_window()
        cls.Mdriver.get(EPS_URL)
        cls.epsorg=Epsorg(cls.Mdriver)
        cls.epsorg.Login(EPS_name,EPS_pwd,Screen)

    def setUp(self):
        Screen = os.path.join(ScreenPath, 'test_setup_error.png')
        self.Mdriver.refresh()
        self.epsorg.intopage(Screen)

    def test_export(self):
        Screen = os.path.join(ScreenPath, 'test_export_error.png')
        self.epsorg.exbutton_click(Screen)
        db = pymysql.connect('192.168.146.27', 'root', '123456', 'idscloud')
        cursor = db.cursor()
        sql = 'select count(*) from sorg where companyid=(SELECT company_id from ids_consume_company where name="%s") and SORG_FULLNAME <> "%s"' % (
        EPS_Companyname, EPS_Companyname)
        cursor.execute(sql)
        count = cursor.fetchone()[0]
        db.close()
        path = DATA_DIR + '\\org_export\\' + EPS_Companyname + '组织架构.xls'
        if os.path.exists(path):
            len = xls_row_len(path) - 2
            if len == count:
                flag = True
                msg = '下载文件成功，数据总数与数据库相等,数据共%d 条' % len
            else:
                flag = False
                msg = '下载文件与数据库不对应'
        else:
            flag = False
            msg = '下载文件失败'
        log.info(msg)
        self.assertTrue(flag, msg)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        Screen = os.path.join(ScreenPath, 'test_EpsorganizationLogout_error.png')
        cls.epsorg.Logout(Screen)
        cls.Mdriver.quit()
        log.info('==========================END=================================')

