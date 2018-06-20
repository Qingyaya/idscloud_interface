#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from page_objects.market_home import MarketHome

from public.base_page import BasePage
from public.Log import Log
from datas.setting import *
import time

log=Log()

class EpsHome(BasePage):
    homepage_xpath='//*[@id="app"]/div/div/div[1]/ul/div/div[2]/div[1]/li'

    def eps_click(self,screenshot_path):
        self.element_to_be_click_able_by_xpath('//span[text()="我是企业"]',screenshot_path).click()
        time.sleep(4)
        self.switch_to_lastwin()
        return self

    def homepage(self,screenshot_path):
        if 'ivu-menu-item-active' not in self.find_element_by_xpath(self.homepage_xpath,screenshot_path).get_attribute('class'):
            self.find_element_by_xpath(self.homepage_xpath, screenshot_path).click()

    def Login(self,name,password,screenshot_path):
        mh=MarketHome(self.driver)
        mh.eps_login(name,password,screenshot_path)
        return self

    def Logout(self,screenshot_path):
        if self.get_page_title() != u'企业中心':
            self.switch_to_lastwin()
        icon=self.find_element_by_xpath('//li[contains(@class,"login-sub-menu ivu-menu-submenu")]',screenshot_path)
        webdriver.ActionChains(self.driver).move_to_element(icon).perform()
        time.sleep(2)
        self.find_element_by_xpath('//li[text()="退出"]',screenshot_path).click()
        return self

    def register(self,Companyname,CompanyNo,Imgpath,screenshot_path):
        self.find_elements_by_class_name('ivu-input',screenshot_path)[0].clear()
        self.find_elements_by_class_name('ivu-input', screenshot_path)[0].send_keys(Companyname)
        self.find_elements_by_class_name('ivu-input', screenshot_path)[1].clear()
        self.find_elements_by_class_name('ivu-input', screenshot_path)[1].send_keys(CompanyNo)
        self.find_element_by_xpath('//i[contains(@class,"ivu-icon-ios-plus-empty")]',screenshot_path).click()
        l='%s\\import_busi_license.exe %s'%(BASE_DIR,Imgpath)
        os.system(l)
        time.sleep(3)
        self.find_elements_by_class_name("ivu-checkbox-input",screenshot_path)[0].click()
        self.find_element_by_id('submit',screenshot_path).click()
        time.sleep(3)

    def company_details(self,screenshot_path):
        self.eps_click(screenshot_path)
        if self.get_page_title() != u'企业中心':
            self.switch_to_lastwin()
        msg=self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[3]/div[2]/div/form[1]/div[5]/div/span[2]',screenshot_path).text
        return self,msg

    def finduser(self,username,screenshot_path):
        if self.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/ul/div/div[2]/div[3]/li',screenshot_path).get_attribute('class') != 'ivu-menu-item ivu-menu-item-active ivu-menu-item-selected':
            self.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/ul/div/div[2]/div[3]/li/span', screenshot_path).click()
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[2]/div[1]/div[1]/div/input',screenshot_path).clear()
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[2]/div[1]/div[1]/div/input',screenshot_path).send_keys(username)
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[2]/div[1]/div[3]/button/span',screenshot_path).click()
        time.sleep(2)

    def myorder(self,screenshot_path):
        icon=self.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/ul/div/div[2]/div[5]/li/div[1]',screenshot_path)
        webdriver.ActionChains(self.driver).move_to_element(icon).perform()
        if 'ivu-menu-item-active' not in self.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/ul/div/div[2]/div[5]/li/div[2]/ul/li[1]', screenshot_path).get_attribute('class'):
            self.element_to_be_click_able_by_xpath('//*[@id="app"]/div/div/div[1]/ul/div/div[2]/div[5]/li/div[2]/ul/li[1]',screenshot_path).click()
        time.sleep(3)

    def myorder_search(self,orderno,screenshot_path):
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[2]/div[2]/div[2]/div/input',screenshot_path).clear()
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[2]/div[2]/div[2]/div/input',screenshot_path).send_keys(orderno)
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[2]/div[1]/div[3]/button',screenshot_path).click()
        time.sleep(3)

    def openapp(self,orderno,screenshot_path):
        self.myorder(screenshot_path)
        self.myorder_search(orderno,screenshot_path)
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[3]/div/div[2]/table/tbody/tr/td[11]/div/div/i[2]',screenshot_path).click()
        time.sleep(2)
        self.find_elements_by_class_name('ivu-modal-footer',screenshot_path)[0].find_elements_by_tag_name('button')[0].click()
        time.sleep(5)
        return self

    def appmanage(self,screenshot_path):
        time.sleep(2)
        if self.get_page_title() != u'企业中心':
            self.switch_to_lastwin()

        # '//*[@id="app"]/div/div/div[1]/ul/div/div[2]/div[4]/li'
        if 'ivu-menu-item-active' not in self.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/ul/div/div[2]/div[4]/li', screenshot_path).get_attribute('class'):
            self.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/ul/div/div[2]/div[4]/li/span',screenshot_path).click()
        return self

    def appnames_Saas(self,screenshot_path):
        self.appmanage(screenshot_path)
        names=[]
        eles=self.find_element_by_class_name('SaaSAppList',screenshot_path).find_elements_by_class_name('app-name')
        for i in range(len(eles)):
            names.append(eles[i].text)
        return names

    # def usermanage(self,screenshot_path):
    #     if self.get_page_title() != u'企业中心':
    #         self.switch_to_lastwin()
    #     ele=self.find_element_by_class_name('layout-nav',screenshot_path)
    #     if 'ivu-menu-item-active' not in ele.find_elements_by_tag_name('li')[2].get_attribute('class'):
    #         ele.find_elements_by_tag_name('li')[2].click()
    #     return self
    #
    # def adduser(self, username, usermail, userphone, userNo, orgname, screenshot_path):
    #     self.element_to_be_click_able_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[3]/div[1]/button', screenshot_path).click()
    #     self.find_element_by_xpath("(//input[@type='text'])[6]", screenshot_path).clear()
    #     self.find_element_by_xpath("(//input[@type='text'])[6]", screenshot_path).send_keys(username)
    #     self.find_element_by_xpath("(//input[@type='text'])[7]", screenshot_path).clear()
    #     self.find_element_by_xpath("(//input[@type='text'])[7]", screenshot_path).send_keys(username)
    #     self.find_element_by_xpath("(//input[@type='text'])[8]", screenshot_path).clear()
    #     self.find_element_by_xpath("(//input[@type='text'])[8]", screenshot_path).send_keys(usermail)
    #     self.find_element_by_xpath("(//input[@type='text'])[9]", screenshot_path).clear()
    #     self.find_element_by_xpath("(//input[@type='text'])[9]", screenshot_path).send_keys(userphone)
    #     self.find_element_by_xpath("(//input[@type='text'])[10]", screenshot_path).clear()
    #     self.find_element_by_xpath("(//input[@type='text'])[10]", screenshot_path).send_keys(userNo)
    #     self.find_element_by_xpath("(//input[@type='text'])[11]", screenshot_path).clear()
    #     self.find_element_by_xpath("(//input[@type='text'])[11]", screenshot_path).send_keys(u"员工")
    #     self.find_elements_by_class_name('ivu-radio-group', screenshot_path)[0].find_element_by_class_name('ivu-radio').click()
    #     self.find_element_by_xpath("//input[@type='password']", screenshot_path).clear()
    #     self.find_element_by_xpath("//input[@type='password']", screenshot_path).send_keys("a123456")
    #     self.find_element_by_xpath("(//input[@type='password'])[2]", screenshot_path).clear()
    #     self.find_element_by_xpath("(//input[@type='password'])[2]", screenshot_path).send_keys("a123456")
    #     self.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[2]/div/form/div[10]/div/button",screenshot_path).click()
    #
    #     if self.find_element_by_class_name('ivu-tree-title', screenshot_path).text == orgname:
    #         self.find_element_by_class_name('ivu-tree-title', screenshot_path).click()
    #     else:
    #         lists = self.find_elements_by_class_name('ivu-tree-children', screenshot_path)
    #         for i in range(len(lists)):
    #             if lists[i].find_elements_by_tag_name('span')[1].text == orgname:
    #                 try:
    #                     lists[i].find_elements_by_tag_name('span')[1].click()
    #                 except:
    #                     raise Exception('选择组织机构失败！！！')
    #                 break
    #             else:
    #                 raise Exception('没有找到对应的组织机构')
    #
    #     self.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/button[1]/span',screenshot_path).click()
    #     time.sleep(2)
    #     self.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[2]/div/form/div[11]/div/button[1]/span",screenshot_path).click()
    #     time.sleep(2)
    #
    # def usersearch(self,username,screenshot_path):
    #     self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[2]/div[1]/div[1]/div/input',screenshot_path).clear()
    #     self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[2]/div[1]/div[1]/div/input',screenshot_path).send_keys(username)
    #     self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[2]/div[1]/div[3]/button',screenshot_path).click()
    #     time.sleep(3)
    #
    # def allotappuser(self,appname,screenshot_path):
    #     js='document.getElementsByClassName("ivu-table-column-center")[3].getElementsByTagName("i")[1].click();'
    #     self.driver.execute_script(js)
    #     time.sleep(3)
    #     self.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[2]/div[1]/div/div/input',screenshot_path).clear()
    #     self.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[2]/div[1]/div/div/input',screenshot_path).send_keys(appname)
    #     self.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[2]/div[1]/div/button[1]',screenshot_path).click()
    #     time.sleep(2)
    #     self.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr/td[1]/div/label/span',screenshot_path).click()
    #     self.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[3]/div/button[1]',screenshot_path).click()
    #     time.sleep(1)
    #     self.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[3]/div/button[2]',screenshot_path).click()
    #     time.sleep(3)
    #
    # def orgnamage(self,screenshot_path):
    #     if 'ivu-menu-item-active' not in self.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/ul/div/div[2]/div[2]/li', screenshot_path).get_attribute('class'):
    #         self.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/ul/div/div[2]/div[2]/lispan',screenshot_path).click()
    #     return self
    #
    # def searchorg(self,name,screenshot_path):
    #     self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[2]/form/div/div[1]/div/input',screenshot_path).clear()
    #     self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[2]/form/div/div[1]/div/input',screenshot_path).send_keys(name)
    #     self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[2]/form/div/div[2]/button/span',screenshot_path).click()
    #     time.sleep(3)
    #
    # def orgadd(self,orgName,orgNo,orgType,parentOrg,screenshot_path):
    #     self.searchorg(parentOrg,screenshot_path)
    #     self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div[3]/div[1]/div/ul[1]/li/span[2]/span[2]/button',screenshot_path).click()
    #     self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[1]/form/div[1]/div/div/input',screenshot_path).clear()
    #     self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[1]/form/div[1]/div/div/input',screenshot_path).send_keys(orgName)
    #     self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[1]/form/div[2]/div/div/input',screenshot_path).clear()
    #     self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[1]/form/div[2]/div/div/input',screenshot_path).send_keys(orgNo)
    #     self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[1]/form/div[3]/div/div/input',screenshot_path).clear()
    #     self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[1]/form/div[3]/div/div/input',screenshot_path).send_keys(orgType)
    #     self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[3]/div/button[1]',screenshot_path).click()
    #     time.sleep(2)

    def selfapp_add(self,jointype,appname,logo,url,discript,disable,identfytype,autosubmit,screenshot_path):
        self.find_element_by_xpath("//i[contains(@class,'ivu-icon ivu-icon-ios-plus-empty')]",screenshot_path).click()
        if 'swa' in jointype.lower() :
            self.find_elements_by_class_name('ivu-radio-input',screenshot_path)[0].click()
        elif 'oauth' in jointype.lower():
            self.find_elements_by_class_name('ivu-radio-input',screenshot_path)[1].click()
        self.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/button[1]',screenshot_path).click()
        self.find_element_by_xpath('//button[@class="logo-btn ivu-btn ivu-btn-ghost ivu-btn-long"]',screenshot_path).click()
        l='%s\\import_busi_license.exe %s'%(BASE_DIR,os.path.join(DATA_DIR,logo))
        os.system(l)
        time.sleep(3)
        self.find_elements_by_class_name('ivu-input',screenshot_path)[1].clear()
        self.find_elements_by_class_name('ivu-input',screenshot_path)[1].send_keys(appname)
        self.find_elements_by_class_name('ivu-input',screenshot_path)[2].clear()
        self.find_elements_by_class_name('ivu-input',screenshot_path)[2].send_keys(url)
        self.find_elements_by_class_name('ivu-input',screenshot_path)[3].clear()
        self.find_elements_by_class_name('ivu-input',screenshot_path)[3].send_keys(discript)
        if disable == '0':
            self.find_elements_by_class_name('ivu-radio-input',screenshot_path)[0].click()
        else:
            self.find_elements_by_class_name('ivu-radio-input', screenshot_path)[1].click()
        if identfytype == '0':
            self.find_elements_by_class_name('ivu-radio-input',screenshot_path)[2].click()
        else:
            self.find_elements_by_class_name('ivu-radio-input',screenshot_path)[3].click()
        if autosubmit !='0':
            self.find_elements_by_class_name('ivu-checkbox-input',screenshot_path)[0].click()
        self.find_element_by_xpath('//button[@class="ivu-btn ivu-btn-ghost"]',screenshot_path).click()
        time.sleep(3)

    def appnames_self(self,screenshot_path):
        names=[]
        eles=self.find_element_by_class_name('selfAppList',screenshot_path).find_elements_by_class_name('app-name')
        for i in range(len(eles)):
            names.append(eles[i].text)
        return names

    def regiseter_update(self,screenshot_path):
        self.find_element_by_xpath('(//a[@class="modify"])[4]',screenshot_path).click()
        ele=self.find_element_by_xpath('//a[text()="这里"]',screenshot_path)
        self.click_ele_until_pass(ele)
        time.sleep(2)
        return self

