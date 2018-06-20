#-*-coding:utf-8-*-
from selenium import webdriver
from public.base_page import BasePage
from public.Log import Log
from datas.setting import *
from time import sleep
import time
log=Log()
class IsvHome(BasePage):

    def Logout(self,screenshot_path):
        icon = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div/div/div[2]/ul/li/div[1]')
        webdriver.ActionChains(self.driver).move_to_element(icon).perform()
        self.element_to_be_click_able_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div/div/div[2]/ul/li/div[2]/ul/li',screenshot_path).click()
        return self

    def companyenter(self,screenshot_path):
        self.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/form/div[1]/div/div/input',screenshot_path).send_keys(ISV_Companyname)
        self.element_to_be_click_able_by_xpath('//span[@class="ivu-select-placeholder"]',screenshot_path).click()
        self.visib_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/form/div[2]/div/div/div[2]/ul[2]',screenshot_path)
        inds = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/form/div[2]/div/div/div[2]/ul[2]')
        inds.find_elements_by_tag_name('li')[ISV_Industry].click()
        self.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/form/div[3]/div/div/input',screenshot_path).send_keys(ISV_CompanyNo)
        self.element_to_be_click_able_by_xpath('//*[@id="upload"]/div/div',screenshot_path).click()
        l='%s\\import_busi_license.exe %s'%(BASE_DIR,ISV_Imgpath)
        os.system(l)
        sleep(3)

        self.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/form/div[5]/div/div/input',screenshot_path).send_keys(ISV_Openbank)
        self.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/form/div[6]/div/div/input',screenshot_path).send_keys(ISV_OpenBname)
        self.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/form/div[7]/div/div/input',screenshot_path).send_keys(ISV_OpenNo)
        self.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/form/div[8]/div/button',screenshot_path).click()


    def company_details(self,screenshot_path):
        self.switch_to_lastwin()
        time.sleep(5)
        name=self.visib_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[1]/div[2]',screenshot_path).text
        return name

    def appmamage(self,screenshot_path):
        ele=self.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/ul/li[3]',screenshot_path)
        if 'ivu-menu-item-active' not in ele.get_attribute('class'):
            ele.click()
        return self

    def appmanage_search(self,appname,screenshot_path):
        self.refresh()
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/form/div/div[1]/div/input',screenshot_path).clear()
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/form/div/div[1]/div/input',screenshot_path).send_keys(appname)
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/form/div/div[3]/button',screenshot_path).click()
        sleep(5)
        return self

    def apply(self,appname,screenshot_path):
        sleep(3)
        self.appmanage_search(appname,screenshot_path)
        self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[3]/div/div[2]/table/tbody/tr/td[10]/div/div/i[3]',screenshot_path)
        self.click_ele_xpath_until_pass('//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[3]/div/div[2]/table/tbody/tr/td[10]/div/div/i[3]')
        self.find_elements_by_tag_name('textarea',screenshot_path)[1].send_keys('提交申请')
        self.find_element_by_class_name('ivu-modal-footer',screenshot_path).find_elements_by_tag_name('button')[0].click()
        time.sleep(3)

    def appstatecurrent(self,appname,screenshot_path):
        self.appmanage_search(appname,screenshot_path)
        table=self.find_element_by_class_name('ivu-table-row',screenshot_path)
        state=table.find_elements_by_tag_name('td')[7].text
        return state






