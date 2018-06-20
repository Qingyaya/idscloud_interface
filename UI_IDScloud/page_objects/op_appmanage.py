# -*-coding:utf-8 -*-
from selenium.webdriver.common.keys import Keys

from public.base_page import BasePage
import time

class Op_Appmagage(BasePage):
    appmanage_xpath='//*[@id="app"]/div/div/div[1]/div/ul[5]/li'
    selectlist_class='ivu-select-dropdown-list'
    appname_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/form/div[1]/div[1]/div/input'
    appstatek_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/form/div[1]/div[2]/div/div[1]'
    appstate_classid=0
    appcreatetime_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/form/div[1]/div[3]/div/div[1]/div/input'
    apptypek_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/form/div[2]/div[1]/div/div[1]/span[1]'
    apptype_classid=1
    appcompany_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/form/div[2]/div[2]/div/input'
    appsearch_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/form/div[1]/div[4]/button'
    appcancel_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/form/div[2]/div[3]/button'
    appdelete_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[3]/div[1]/button'
    appimport_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[3]/div[2]/div/div/div/button'
    appaudit_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[4]/div/div[2]/table/tbody/tr[1]/td[9]/div/div/i[3]'
    appauditpass_xpath='/html/body/div[5]/div[2]/div/div/div[3]/div/button[2]/span'
    appaudit_class='ivu-table-column-left'
    appauditpass_classid=2

    appauditmsg_class='ivu-modal-footer'
    appauditmsg_classid=1
    appauditpass_tag='button'
    appauditpass_tagid=2

    def appmanage(self,screenshot_path):
        ele=self.find_element_by_xpath(self.appmanage_xpath,screenshot_path)
        if 'ivu-menu-item-active' not in ele.get_attribute('class'):
            ele.click()
        return self

    def appname(self,name,screenshot_path):
        self.find_element_by_xpath(self.appname_xpath,screenshot_path).send_keys(name)
        return self

    def appstate(self,state,screenshot_path):
        self.find_element_by_xpath(self.appstatek_xpath,screenshot_path).click()
        lists=self.find_elements_by_class_name(self.selectlist_class,screenshot_path)[self.appstate_classid].find_elements_by_tag_name('li')
        for i in range(len(lists)):
            if lists[i].text==state:
                try:
                    lists[i].click()
                    break
                except:
                    raise Exception('选择应用状态失败')
            else:
                flag = False
        if not flag:
            raise Exception('没有要选的应用状态')
        return self

    def appcreatetime(self,date,screenshot_path):
        self.find_element_by_xpath(self.appcreatetime_xpath,screenshot_path).send_keys(date)
        return self

    def apptype(self,type,screenshot_path):
        self.find_element_by_xpath(self.apptypek_xpath,screenshot_path).click()
        lists=self.find_elements_by_class_name(self.selectlist_class,screenshot_path)[self.apptype_classid].find_elements_by_tag_name('li')
        for i in range(len(lists)):
            if lists[i].text==type:
                try:
                    lists[i].click()
                    break
                except:
                    raise Exception('选择应用类型失败')
            else:
                flag = False
        if not flag:
            raise Exception('没有要选的应用类型')
        return self

    def appcompany(self,name,screenshot_path):
        self.find_element_by_xpath(self.appcompany_xpath,screenshot_path).send_keys(name)
        return self

    def appsearch(self,screenshot_path):
        self.find_element_by_xpath(self.appsearch_xpath,screenshot_path).click()
        return self

    def appcancel(self,screenshot_path):
        self.find_element_by_xpath(self.appcancel_xpath,screenshot_path).click()
        return self

    def appdelete(self,screenshot_path):
        self.find_element_by_xpath(self.appcancel_xpath,screenshot_path).click()
        return self

    def appimport(self,screenshot_path):
        self.find_element_by_xpath(self.appimport_xpath,screenshot_path).click()
        return self

    def app_audit(self,appname,screenshot_path):
        self.appname(appname,screenshot_path)
        self.appsearch(screenshot_path)
        time.sleep(5)
        js='document.getElementsByClassName("%s")[1].getElementsByTagName("i")[%s].click();' % (self.appaudit_class,self.appauditpass_classid)
        self.driver.execute_script(js)
        self.find_elements_by_tag_name('textarea',screenshot_path)[1].send_keys('通过')
        self.find_elements_by_class_name(self.appauditmsg_class,screenshot_path)[self.appauditmsg_classid].find_elements_by_tag_name(self.appauditpass_tag)[self.appauditpass_tagid].click()
        time.sleep(3)



