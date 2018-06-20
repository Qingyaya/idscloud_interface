import time,re

from selenium.webdriver.common.keys import Keys

from public.base_page import BasePage
from datas.setting import *
from page_objects.market_home import MarketHome
from selenium import webdriver
class Epsuser(BasePage):

    add_user_button_xpath='//span[text()="添加员工"]'
    addpage_edit_class='ivu-input'
    username=1
    mobile=2
    password=3
    mail=4
    workerid=6
    job=7
    org_find_id =8
    sex_class="ivu-radio-input"
    boy=0
    girl=1
    addpage_button_tag='button'
    addpage_return_id=0
    addpage_savecontinue_id=1
    addpage_save_id=2
    addpage_cancel_id=3
    addpage_orgchoice='//i[contains(@class,"ivu-icon-arrow-down-b")]'
    org_find_xpath='//i[contains(@class,"ivu-icon-ios-search-strong")]'




    def Login(self,name,password,screenshot_path):
        mk=MarketHome(self.driver)
        mk.Login(name,password,screenshot_path)
        time.sleep(5)
        return self

    def Logout(self,screenshot_path):
        if self.get_page_title() != u'企业中心':
            self.switch_to_lastwin()
        icon=self.find_element_by_xpath('//li[@class="login-sub-menu ivu-menu-submenu"]',screenshot_path)
        webdriver.ActionChains(self.driver).move_to_element(icon).perform()
        time.sleep(2)
        self.find_element_by_xpath('//li[text()="退出"]',screenshot_path).click()
        return self

    def intopage(self,screenshot_path):
        if self.get_page_title()!=u"企业中心":
            self.switch_to_lastwin()
        ele=self.find_element_by_class_name('layout-nav',screenshot_path)
        time.sleep(2)
        ele=ele.find_elements_by_tag_name('li')[2]
        if 'ivu-menu-item-active' not in ele.get_attribute('class'):
            ele.click()
        return self

    def adduser_click(self,screenshot_path):
        self.find_element_by_xpath(self.add_user_button_xpath,screenshot_path).click()
        time.sleep(2)
        return self

    def addpage_username(self,username,screenshot_path):
        self.find_elements_by_class_name(self.addpage_edit_class,screenshot_path)[self.username].clear()
        self.find_elements_by_class_name(self.addpage_edit_class,screenshot_path)[self.username].send_keys(username)
        return self
    def addpage_mobile(self,mobile,screenshot_path):
        self.find_elements_by_class_name(self.addpage_edit_class,screenshot_path)[self.mobile].clear()
        self.find_elements_by_class_name(self.addpage_edit_class,screenshot_path)[self.mobile].send_keys(mobile)
        return self
    def addpage_password(self,password,screenshot_path):
        self.find_elements_by_class_name(self.addpage_edit_class,screenshot_path)[self.password].clear()
        self.find_elements_by_class_name(self.addpage_edit_class,screenshot_path)[self.password].send_keys(password)
        return self
    def addpage_mail(self,mail,screenshot_path):
        self.find_elements_by_class_name(self.addpage_edit_class,screenshot_path)[self.mail].clear()
        self.find_elements_by_class_name(self.addpage_edit_class,screenshot_path)[self.mail].send_keys(mail)
        return self
    def addpage_workerid(self,workerid,screenshot_path):
        self.find_elements_by_class_name(self.addpage_edit_class,screenshot_path)[self.workerid].clear()
        self.find_elements_by_class_name(self.addpage_edit_class,screenshot_path)[self.workerid].send_keys(workerid)
        return self
    def addpage_job(self,job,screenshot_path):
        self.find_elements_by_class_name(self.addpage_edit_class,screenshot_path)[self.job].clear()
        self.find_elements_by_class_name(self.addpage_edit_class,screenshot_path)[self.job].send_keys(job)
        return self

    def addpage_sex(self,sex,screenshot_path):
        if sex=='0':
            self.find_elements_by_class_name(self.sex_class,screenshot_path)[self.boy].click()
        elif sex =='1':
            self.find_elements_by_class_name(self.sex_class, screenshot_path)[self.girl].click()
        else:
            raise ('检查测试数据中的性别，男：0，女：1')
        return self

    def addpage_back(self,screenshot_path):
        self.find_elements_by_tag_name(self.addpage_button_tag,screenshot_path)[self.addpage_return_id].click()
        return self

    def addpage_savecontinue(self,screenshot_path):
        self.find_elements_by_tag_name(self.addpage_button_tag,screenshot_path)[self.addpage_savecontinue_id].click()
        return self

    def addpage_save(self,screenshot_path):
        self.find_elements_by_tag_name(self.addpage_button_tag,screenshot_path)[self.addpage_save_id].click()
        return self

    def addpage_cancel(self,screenshot_path):
        self.find_elements_by_tag_name(self.addpage_button_tag,screenshot_path)[self.addpage_cancel_id].click()
        return self

    def addpage_choose_click(self,screenshot_path):
        self.find_element_by_xpath(self.addpage_orgchoice,screenshot_path).click()
        return self

    def org_find(self,org,screenshot_path):
        self.find_elements_by_class_name(self.addpage_edit_class)[self.org_find_id].clear()
        self.find_elements_by_class_name(self.addpage_edit_class)[self.org_find_id].send_keys(org)
        self.find_element_by_xpath(self.org_find_xpath,screenshot_path)[self.org_find_xpath].click()
        return self

    def org_choose(self,orgpath,screenshot_path):
        orgs=orgpath.split('/')
        eles=self.find_elements_by_class_name('ivu-tree-children',screenshot_path)
        for org in orgs[1:len(orgs)-1]:
            for ele in eles:
                if ele.find_elements_by_tag_name('span')[1].text==org:
                    eles=ele.find_elements_by_tag_name('li')
                    break
        for ele in eles:
            if ele.find_elements_by_tag_name('span')[1].text == orgs[-1]:
                ele.find_elements_by_tag_name('span')[1].click()
                break
        self.find_element_by_class_name('ivu-modal-footer',screenshot_path).find_element_by_xpath('//span[text()="确定"]').click()

        return self




