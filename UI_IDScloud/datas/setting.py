# global waiting time config


WAIT_TIME = 10

BROWSER_NAME = 'Chrome'
BASE_URL='https://bccastle.com/'
OP_URL='https://bccastle.com/op/#/login'
EPS_URL='https://bccastle.com/eps'

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.dirname(os.path.abspath(__file__))

# email
SMTP_server = 'smtp.bamboocloud.cn'
Port = '465'
Sender = 'lina@bamboocloud.cn'
Psw = 'P@ssw0rd1'
Receiver = ['dongchunyi@bamboocloud.cn','shashaxiaoge@163.com']

#database
DB_ip = '192.168.146.27'
DB_instance = 'idscloud'
DB_username = 'root'
DB_password = '123456'

# ;casepakage
CASEPATH = '/testCase'

# OP_user
OP_username='admin'
OP_password='admin'

# ;eps_companyuser
EPS_name='testui'
EPS_pwd='a123456'
EPS_Companyname='testuiregister'
EPS_CompanyNo='TestNo01'
EPS_Imgpath=os.path.join(BASE_DIR,'datas\\busilicense.png')

#isv_company
ISV_Companyname='testuienter'
ISV_CompanyNo='001'
ISV_Industry=1
ISV_Imgpath=os.path.join(BASE_DIR,'datas\\Enterbusilicense.png')
ISV_Openbank='测试银行'
ISV_OpenBname='testuienter'
ISV_OpenNo='11111111111111'

from selenium import webdriver
Options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': DATA_DIR+'\\org_export'}
Options.add_experimental_option('prefs', prefs)
