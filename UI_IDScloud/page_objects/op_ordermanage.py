# -*-coding:utf-8 -*-

from public.base_page import BasePage
from page_objects.op_home import OpHome
import time

class Op_Ordermanage(BasePage):
    selectk_class='ivu-select-placeholder'
    selectlist_class='ivu-select-dropdown-list'
    ordermanage_link_xpath='//*[@id="app"]/div/div/div[1]/div/ul[6]/li'
    apptypek_classid=0
    apptype_classid=0
    createtime_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/form/div[1]/div[2]/div/div[1]/div/input'
    servicepro_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/form/div[1]/div[3]/div/input'

    orderstatek_classid=1
    orderstate_classid=1
    orderno_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/form/div[2]/div[2]/div/input'
    search_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/form/div[1]/div[4]/button'
    addorder_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[3]/div/button'
    updateorder_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[4]/div/div[2]/table/tbody/tr[1]/td[13]/div/div/i[2]'
    orderstate_class='ivu-select-selected-value'
    updatestate_xpath='/html/body/div[3]/ul[2]/li[1]'
    proprotion_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/div/div[3]/div/span[2]/div/input'
    updatesubmit_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/div[2]/div/div[5]/form/div/div/button[1]'
    def Login(self,screenpath):
        op=OpHome(self.driver)
        op.Login(screenpath)
    def Logout(self,screenpath):
        op=OpHome(self.driver)
        op.Logout(screenpath)

    def ordermanage_link(self,screenpath):
        self.element_to_be_click_able_by_xpath(self.ordermanage_link_xpath,screenpath).click()
        return self

    def apptype_selet(self,name,screenpath):
        self.find_elements_by_class_name(self.selectk_class,screenpath)[self.apptype_classid].click()
        ele=self.find_elements_by_class_name(self.selectlist_class,screenpath)[self.apptype_classid].find_elements_by_tag_name('li')
        for i in range(len(ele)):
            if ele[i]==name:
                flag = True
                try:
                    ele[i].click()
                    break
                except:
                    raise Exception('选择应用类型失败')
            else:
                flag = False
        if not flag:
                raise Exception('没有要选的应用类型')

    def appcreatetime_input(self,date,screenpath):
        self.find_element_by_xpath(self.createtime_xpath,screenpath).send_keys(date)
        return self

    def appservicepro_input(self,name,screenpath):
        self.find_element_by_xpath(self.servicepro_xpath,screenpath).send_keys(name)
        return self

    def apporderstate_selet(self,state,screenpath):
        self.find_elements_by_class_name(self.selectk_class,screenpath)[self.orderstatek_classid].click()
        ele=self.find_elements_by_class_name(self.selectlist_class,screenpath)[self.orderstate_classid].find_elements_by_tag_name('li')
        for i in range(len(ele)):
            if ele[i]==state:
                flag = True
                try:
                    ele[i].click()
                    break
                except:
                    raise Exception('选择支付状态失败')
            else:
                flag = False
        if not flag:
                raise Exception('没有要选的支付状态')
        return self

    def apporderno_input(self,number,screenpath):
        self.find_element_by_xpath(self.orderno_xpath,screenpath).send_keys(number)
        return self

    def appsearch(self,screenpath):
        self.find_element_by_xpath(self.search_xpath,screenpath).click()
        time.sleep(3)
        return self

    def addorder_button(self,screenpath):
        self.find_element_by_xpath(self.addorder_xpath,screenpath).click()
        return self


    def auditorder(self,orderno,proprotion,screenpath):
        self.ordermanage_link(screenpath)
        self.apporderno_input(orderno,screenpath)
        self.appsearch(screenpath)
        js='document.getElementsByClassName("ivu-table-column-center")[1].getElementsByTagName("i")[1].click();'
        self.driver.execute_script(js)
        self.find_element_by_class_name(self.orderstate_class,screenpath).click()
        self.find_element_by_xpath(self.updatestate_xpath,screenpath).click()
        self.find_element_by_xpath(self.proprotion_xpath,screenpath).clear()
        self.find_element_by_xpath(self.proprotion_xpath,screenpath).send_keys(proprotion)
        self.find_element_by_xpath(self.updatesubmit_xpath,screenpath).click()
        time.sleep(3)










