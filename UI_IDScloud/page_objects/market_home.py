#-*-coding:utf-8-*-

from public.base_page import BasePage
from selenium import webdriver
from datas.setting import *
from public.Log import Log
from selenium.webdriver.common.keys import Keys
from time import sleep
log=Log()

class MarketHome(BasePage):

    def Register(self,screenshot_path):
        self.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/ul/li[9]/button/span',screenshot_path).click()
        self.find_element_by_xpath("//input[@type='text']",screenshot_path).clear()
        self.find_element_by_xpath("//input[@type='text']",screenshot_path).send_keys(EPS_name)
        self.find_element_by_xpath("//input[@type='password']",screenshot_path).clear()
        self.find_element_by_xpath("//input[@type='password']",screenshot_path).send_keys(EPS_pwd)
        self.find_element_by_xpath("(//input[@type='password'])[2]",screenshot_path).clear()
        self.find_element_by_xpath("(//input[@type='password'])[2]",screenshot_path).send_keys(EPS_pwd)
        self.find_element_by_xpath("(//input[@type='text'])[2]",screenshot_path).clear()
        self.find_element_by_xpath("(//input[@type='text'])[2]",screenshot_path).send_keys("15210925036")
        self.find_element_by_xpath("(//input[@type='text'])[3]",screenshot_path).clear()
        self.find_element_by_xpath("(//input[@type='text'])[3]",screenshot_path).send_keys("491219")
        self.find_elements_by_class_name("ivu-checkbox-input",screenshot_path)[0].click()
        self.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/div/div/div/form/div[7]/div/button",screenshot_path).click()
        return self

    def Login_link(self,screenshot_path):
        self.element_to_be_click_able_by_xpath('/html/body/div/div[1]/div/div/div[2]/ul/li[10]',screenshot_path).click()
        return self

    def Login(self,name,password,screenshot_path):
        self.find_element_by_id("j_username",screenshot_path).clear()
        self.find_element_by_id("j_username",screenshot_path).send_keys(name)
        self.find_element_by_id("j_password",screenshot_path).clear()
        self.find_element_by_id("j_password",screenshot_path).send_keys(password)
        self.find_element_by_id("loginBtn",screenshot_path).send_keys(Keys.ENTER)
        return self

    def eps_login(self,username,password,screenshot_path):
        self.Login_link(screenshot_path)
        self.Login(username,password,screenshot_path)
        self.element_to_be_click_able_by_xpath('/html/body/div/div[1]/div/div/div[2]/ul/li[7]/span',screenshot_path).click()
        sleep(5)
        self.switch_to_lastwin()
        return self

    def isv_click(self,screenshot_path):
        self.element_to_be_click_able_by_xpath('/html/body/div/div[1]/div/div/div[2]/ul/li[8]/span',screenshot_path).click()
        self.switch_to_lastwin()
        return self

    def isv_login(self,username,password,screenshot_path):
        self.Login_link(screenshot_path)
        self.Login(username,password,screenshot_path)
        self.isv_click(screenshot_path)
        return self

    def Logout(self,screenshot_path):
        icon = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/ul/li[9]/div[1]/span')
        webdriver.ActionChains(self.driver).move_to_element(icon).perform()
        self.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/ul/li[9]/div[2]/ul/li[1]',screenshot_path).click()
        return self

    def Buyapp_page(self,appname,appkind,timelimit,quantity,screenshot_path):
        self.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]',screenshot_path).find_element_by_xpath('./ul/li[4]').click()
        self.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/input',screenshot_path).send_keys(appname)
        self.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/div/div/div[3]/button/span',screenshot_path).click()
        self.find_element_by_class_name('appLogo',screenshot_path).click()
        self.switch_to_lastwin()
        app=self.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div',screenshot_path)
        app_kinds=app.find_elements_by_tag_name('label')
        for i in range(len(app_kinds)):
            if app_kinds[i].text == appkind:
                app_kinds[i].click()
                break
        if self.is_exist_element_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div'):
            apptimes=self.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div',screenshot_path)
            apptimes_kinds=apptimes.find_elements_by_tag_name('label')
            for i in range(len(apptimes_kinds)):
                if apptimes_kinds[i].text == timelimit:
                    apptimes_kinds[i].click()
                    break
        if self.is_exist_element_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div/input'):
            self.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div/input',screenshot_path).clear()
            self.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div/input',screenshot_path).send_keys(quantity)
        self.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div/div[1]/div[2]/div/button",screenshot_path).click()
        self.find_elements_by_class_name("ivu-checkbox-input",screenshot_path)[0].click()
        self.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[2]/button[2]",screenshot_path).click()
        self.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/p[1]/a',screenshot_path).click()
        orderNo=self.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/ul[1]/li[1]/span[2]',screenshot_path).text
        log.info('订单编号：'+orderNo)
        return self,orderNo


