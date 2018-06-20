#-*-coding:utf-8-*-
from selenium.webdriver.common.keys import Keys

from public.base_page import BasePage
from selenium import webdriver
from datas.setting import *
from public.Log import Log
from time import sleep

log=Log()

class OpHome(BasePage):
    def Login(self,screenpath):
        self.find_element_by_name("uname",screenpath).clear()
        self.find_element_by_name("uname",screenpath).send_keys('admin')
        self.find_element_by_name("upass",screenpath).clear()
        self.find_element_by_name("upass",screenpath).send_keys('admin')
        self.find_element_by_xpath("//form[@id='loginform']/div/div[4]/div/div/button/span",screenpath).click()

    def Logout(self,screenpath):
        icon = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div/div/div/ul/div[2]/li/div[1]')
        webdriver.ActionChains(self.driver).move_to_element(icon).perform()
        sleep(1)
        self.element_to_be_click_able_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div/div/div/ul/div[2]/li/div[2]/ul/li',screenpath).click()
        return self

    def isv_find(self,companyname,state,screenpath):
        self.element_to_be_click_able_by_xpath('//*[@id="app"]/div/div/div[1]/div/ul[3]/li/span',screenpath).click()
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/div/div[1]/div/input',screenpath).clear()
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/div/div[1]/div/input',screenpath).send_keys(companyname)
        self.find_element_by_xpath('//i[contains(@class,"ivu-icon-ios-search")]',screenpath).click()
        sleep(1)
        li=self.driver.find_element_by_class_name('ivu-select-dropdown-list').find_elements_by_tag_name('li')
        for i in range(len(li)):
            if li[i].text==state:
                li[i].click()
                break
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/div/div[3]/button', screenpath).click()
        return self

    def isv_audit(self,screenpath):
        self.Login(screenpath)
        self.isv_find(ISV_Companyname,'待审批',screenpath)
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[4]/div/div[2]/table/tbody/tr/td[8]/div/div/i[3]',screenpath)
        self.click_ele_xpath_until_pass('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[4]/div/div[2]/table/tbody/tr/td[8]/div/div/i[3]')
        self.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[2]/div/div/textarea',screenpath).send_keys(u'通过')
        self.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[3]/div/button[1]/span',screenpath).click()
        return self

    def eps_audit(self,screenpath):

        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[4]/div/div[2]/table/tbody/tr/td[8]/div/div/i[2]',screenpath)
        self.click_ele_xpath_until_pass('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[4]/div/div[2]/table/tbody/tr/td[8]/div/div/i[2]')
        self.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[2]/div/div/textarea',screenpath).send_keys(u'通过')
        self.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[3]/div/button[1]/span',screenpath).click()
        sleep(2)


    def eps_find(self,companyname,state,screenpath):
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/div/div[1]/div/input',screenpath).clear()
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/div/div[1]/div/input',screenpath).send_keys(companyname)
        self.find_element_by_xpath('//i[contains(@class,"ivu-icon-ios-search")]',screenpath).click()
        sleep(1)
        li=self.driver.find_element_by_class_name('ivu-select-dropdown-list').find_elements_by_tag_name('li')
        for i in range(len(li)):
            if li[i].text==state:
                li[i].click()
                break
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/div/div[3]/button',screenpath).click()




