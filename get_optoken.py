from selenium.webdriver.common.keys import Keys
import paramiko
from common.ReadConfig import ReadConfig
from common.get_csv import *
from common.myHttp import post
from selenium import webdriver
rc=ReadConfig()
path=Propath()
def get_optoken():
    url = get_url(path+'\\testFile\\om\\om.csv','login')
    data={'uname':'admin','upass':'admin'}
    re=post(url,data)
    token=re.json()['date']['token']
    return token

def get_markettoken():
    driver=webdriver.Chrome()
    driver.get('https://bccastle.com/eps/')
    driver.maximize_window()
    driver.find_element_by_id("j_username").clear()
    driver.find_element_by_id("j_username").send_keys('yulin')
    driver.find_element_by_id("j_password").clear()
    driver.find_element_by_id("j_password").send_keys('a123456')
    driver.find_element_by_id("loginBtn").send_keys(Keys.ENTER)
    trans = paramiko.Transport(('192.168.146.27', 22))
    trans.connect(username='root', password='abcd1234')
    res = paramiko.SSHClient()
    res._transport = trans
    stdin, stdout, stderr = res.exec_command('tail -n -20 /var/log/is.log')
    tokens = str(stdout.read()).split('\\n')
    tokens = [token for token in tokens if 'token' in token]
    token = tokens[-1].split('=')[-1]
    return token

if __name__ == '__main__':
    rc=ReadConfig()
    om=get_optoken()
    market=get_markettoken()
    rc.set_headers('om',om)
    rc.set_headers('market',market)
    log.info('optoken:%s,markettoken:%s' %(om,market))


