#-*-coding:utf-8-*-

import time

from selenium.webdriver.common.keys import Keys

from public.base_page import BasePage
from datas.setting import *
from public.get_csv import *

from selenium import webdriver
from page_objects.market_home import MarketHome

class Apppublish_page(BasePage):
    slections_class='ivu-select-selection'
    slecttypes_class='ivu-select-dropdown-list'
    radio_class='ivu-radio-inner'
    checkbox_class='ivu-checkbox-input'
    input_class='ivu-input'
    pagelink_xpath='//*[@id="app"]/div/div/div[1]/div/ul/li[2]/span'
    sassbutton_xpath='//*[@id="sass"]/span'
    appname_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/ul/li[2]/div[3]/div[1]/form/div[1]/div/div[1]/input'
    apptypek_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/ul/li[2]/div[3]/div[1]/form/div[2]/div/div/div[1]'
    apptype_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/ul/li[2]/div[3]/div[1]/form/div[2]/div/div/div[2]/ul[2]'
    appvision_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/ul/li[2]/div[3]/div[1]/form/div[3]/div/div/input'
    appostypek_classid=1
    appusers_classid=2
    appamornot_classid=1
    appamtype_classid=3
    appaddress_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/ul/li[2]/div[3]/div[1]/form/div[8]/div/div/input'
    applogo_xpath='//*[@id="logoup"]/div/div'
    appdetail_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/ul/li[3]/div[3]/div/form/div/div[1]/div/div/div/div/div[2]'
    appdetail_detail_xpath='//*[@id="app1"]/div/textarea'
    appdetail_trait_xpath='//*[@id="app2"]/div/div[2]/div[1]'
    appdetail_guide_xpath='//*[@id="app3"]/div/div[2]/div[1]'
    appsuport_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/ul/li[3]/div[3]/div/form/div/div[1]/div/div/div/div/div[3]'
    appsuport_doc_tag='textarea'
    appsuport_file_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/ul/li[3]/div[3]/div/form/div/div[2]/div[2]/div[3]/div/button/span'
    appcase_xpath='//div[contains(text(),"成功案例")]'
    appcase_doc_xpath='//div[@id="appsuccess"]/div/div[2]/div[1]'
    appaddspec_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/ul/li[3]/div[3]/div/form/div/div[1]/div/div/div/div/div[5]'
    appaddspec_model_classid=3
    appaddspec_license_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/ul/li[3]/div[3]/div/form/div/div[2]/div[4]/div[1]/label/span'
    appspecs_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/ul/li[3]/div[3]/div/form/div/div[2]/div[4]/div[2]/div[%(num)s]'
    appspecs_times_modelname_xpath='./div[1]/div[1]/div/div/input'
    appspecs_timeprice_xpath='./div[1]/div[4]/div/div[1]/input'
    appspecs_times_licensemin_xpath='./div[1]/div[3]/div[1]/div/div/div/input'
    appspecs_times_licensemax_xpath='./div[1]/div[3]/div[2]/div/div/div/input'
    appspecs_modelname_xpath='./div[2]/div[1]/div/div/input'
    appspecs_onemonth_classid=0
    appspecs_onemonth_price_xpath='./div[2]/div[5]/div[1]/div/div/div/input'
    appspecs_oneyear_classid=1
    appspecs_oneyear_price_xpath='./div[2]/div[5]/div[2]/div/div/div/input'
    appspecs_threemonth_classid=2
    appspecs_threemonth_price_xpath='./div[2]/div[6]/div[1]/div/div/div/input'
    appspecs_twoyear_classid=3
    appspecs_twoyear_price_xpath='./div[2]/div[6]/div[2]/div/div/div/input'
    appspecs_sixmonth_classid=4
    appspecs_sixmonth_price_xpath='./div[2]/div[7]/div[1]/div/div/div/input'
    appspecs_threeyear_classid=5
    appspecs_threeyear_price_xpath='./div[2]/div[7]/div[2]/div/div/div/input'
    appspecs_licensemin_xpath='./div[2]/div[3]/div[1]/div/div/div/input'
    appspecs_licensemax_xpath='./div[2]/div[3]/div[2]/div/div/div[1]/input'
    appspecs_add_xpath= './div/div/div'
    appspecs_commit_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/ul/li[3]/div[3]/div/form/div/div[2]/div[4]/div[2]/button[1]/span'
    appspecs_cancel_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/ul/li[3]/div[3]/div/form/div/div[2]/div[4]/div[2]/button[2]/span'

    appspecs_negotiable_modelname_xpath='//*[@id="app"]/div/div/div[2]/div[2]/div/div/section/div/ul/li[3]/div[3]/div/form/div/div[2]/div[4]/div[2]/div/div/div/div/div/input'

    msg_xpath='/html/body/div[2]/div[2]'
    msg_button_class='ivu-modal-footer'
    msg_confirm_classid=1
    msg_cancel_classid=0
    # 进入  产品发布  页面
    def page_link(self,screenshot_path):
        wins = self.driver.window_handles
        self.driver.switch_to.window(wins[-1])
        time.sleep(1)
        self.find_element_by_xpath(self.pagelink_xpath,screenshot_path).click()
        return self

    def sassapp(self,screenshot_path):
        self.element_to_be_click_able_by_xpath(self.sassbutton_xpath,screenshot_path).click()
        return  self

    def appname(self,name,screenshot_path):
        self.find_element_by_xpath(self.appname_xpath,screenshot_path).send_keys(name)
        return  self

    def apptype(self,typename,screenshot_path):
        self.find_element_by_xpath(self.apptypek_xpath,screenshot_path).click()
        ele=self.element_to_be_click_able_by_xpath(self.apptype_xpath,screenshot_path)
        #
        list=ele.find_elements_by_tag_name('li')
        for i in range(len(list)):
            if list[i].text == typename:
                flag = True
                try:
                    list[i].click()
                    break
                except:
                    raise Exception('选择产品类型失败')
            else:
                flag=False
        if not flag:
            raise Exception('没有所要选的产品类型')
        return self

    def appvision(self,vision,screenshot_path):
        self.find_element_by_xpath(self.appvision_xpath,screenshot_path).send_keys(vision)
        return self

    def appostype(self,os,screenshot_path):
        self.find_elements_by_class_name(self.slections_class,screenshot_path)[self.appostypek_classid].click()

        stypes=self.find_elements_by_class_name(self.slecttypes_class,screenshot_path)[self.appostypek_classid].find_elements_by_tag_name('li')

        for i in range(len(stypes)):
            if stypes[i].text == os:
                flag = True
                try:
                    stypes[i].click()
                    break
                except:
                    raise Exception('选择产品操作类型失败')
            else:
                flag=False
        if not flag:
            raise Exception('没有要选的操作类型')
        self.find_elements_by_class_name(self.slections_class,screenshot_path)[self.appostypek_classid].click()
        time.sleep(1)
        return self

    def appusers(self,users,screenshot_path):
        self.find_elements_by_class_name(self.slections_class,screenshot_path)[self.appusers_classid].click()
        stypes=self.find_elements_by_class_name(self.slecttypes_class,screenshot_path)[self.appusers_classid].find_elements_by_tag_name('li')

        for i in range(len(stypes)):
            if stypes[i].text == users:
                flag = True
                try:
                    stypes[i].click()
                    break
                except:
                    raise Exception('选择产品用户群体失败')
            else:
                flag=False
        if not flag:
            raise Exception('没有要选的用户群体')
        self.find_elements_by_class_name(self.slections_class,screenshot_path)[self.appusers_classid].click()

        return self

    def appAmornot(self,amornot,screenshot_path):
        if amornot=='0':
            ele=self.find_elements_by_class_name(self.radio_class,screenshot_path)[self.appamornot_classid]
            time.sleep(5)
            webdriver.ActionChains(self.driver).click(ele).perform()
        return self

    def appAmtype(self,amtype,screenshot_path):
        if amtype=='0':
            ele=self.find_elements_by_class_name(self.radio_class,screenshot_path)[self.appamtype_classid]
            time.sleep(2)
            webdriver.ActionChains(self.driver).click(ele).perform()
        return self

    def appaddress(self,address,screenshot_path):
        self.find_element_by_xpath(self.appaddress_xpath,screenshot_path).send_keys(address)
        return self

    def applogo(self,imgpath,screenshot_path):
        path=os.path.join(BASE_DIR,os.path.join('datas',imgpath))
        self.find_element_by_xpath(self.applogo_xpath,screenshot_path).click()
        l='%s\\import_busi_license.exe %s'%(BASE_DIR,path)
        os.system(l)
        time.sleep(3)
        return self

    def appdetail(self,detail,trait,guide,screenshot_path):
        classes=self.find_element_by_xpath(self.appdetail_xpath,screenshot_path)
        if 'ivu-tabs-tab-active' not in classes.get_attribute('class'):
            self.click_ele_xpath_until_pass(self.appdetail_xpath)
        self.find_element_by_xpath(self.appdetail_detail_xpath,screenshot_path).send_keys(detail)
        self.find_element_by_xpath(self.appdetail_trait_xpath,screenshot_path).send_keys(trait)
        self.find_element_by_xpath(self.appdetail_guide_xpath,screenshot_path).send_keys(guide)

    def appsuportservice(self,suportdetail,filepath,screenshot_path):
        classes=self.find_element_by_xpath(self.appsuport_xpath,screenshot_path)
        if 'ivu-tabs-tab-active' not in classes.get_attribute('class'):
            self.click_ele_xpath_until_pass(self.appsuport_xpath)
        self.find_elements_by_tag_name(self.appsuport_doc_tag,screenshot_path)[1
        ].send_keys(suportdetail)
        if filepath != '':
            self.find_element_by_xpath(self.appsuport_file_xpath,screenshot_path).click()
            l = '%s\\import_busi_license.exe %s' % (BASE_DIR, filepath)
            os.system(l)
            time.sleep(3)
        return self

    def appcase(self,passcase,screenshot_path):
        classes=self.find_element_by_xpath(self.appcase_xpath,screenshot_path)
        if 'ivu-tabs-tab-active' not in classes.get_attribute('class'):
            self.click_ele_xpath_until_pass(self.appcase_xpath)
        self.find_element_by_xpath(self.appcase_doc_xpath,screenshot_path).send_keys(passcase)
        return self

    def appaddspec_model(self,model,screenshot_path):

        classes=self.find_element_by_xpath(self.appaddspec_xpath,screenshot_path)
        if 'ivu-tabs-tab-active' not in classes.get_attribute('class'):
            self.click_ele_xpath_until_pass(self.appaddspec_xpath)
        time.sleep(1)
        self.find_elements_by_class_name(self.slections_class,screenshot_path)[self.appaddspec_model_classid].click()
        eles=self.find_elements_by_class_name(self.slecttypes_class,screenshot_path)[self.appaddspec_model_classid].find_elements_by_tag_name('li')
        for i in range(len(eles)):
            if eles[i].text == model:
                flag=True
                try:
                    eles[i].click()
                    break
                except:
                    raise Exception('选择产品规格模式失败')
            else:
                flag = False
        if not flag:
            raise Exception('没有要选的规格模式')
        self.msg_pass(screenshot_path)
        time.sleep(1)
        return self

    def appaddspec_license(self,licenseornot,screenshot_path):
        if licenseornot!='0':
            self.find_element_by_xpath(self.appaddspec_license_xpath,screenshot_path).click()
        return self

    def appadd_modelname(self,modelnum,name,screenshot_path):
        model=self.find_element_by_xpath(self.appspecs_xpath % dict (num = modelnum),screenshot_path)
        model.find_element_by_xpath(self.appspecs_modelname_xpath).send_keys(name)
        return self

    def appadd_modelprice(self,modelnum,limit,price,screenshot_path):
        time.sleep(2)
        model=self.find_element_by_xpath(self.appspecs_xpath % dict (num = modelnum),screenshot_path)
        if limit==u'1月':
            model.find_elements_by_class_name(self.checkbox_class)[self.appspecs_onemonth_classid].click()
            model.find_elements_by_class_name(self.input_class)[3].send_keys(price)
        elif limit == u'1年':
            model.find_elements_by_class_name(self.checkbox_class)[self.appspecs_oneyear_classid].click()
            model.find_elements_by_class_name(self.input_class)[4].send_keys(price)
        elif limit == u'3月':
            model.find_elements_by_class_name(self.checkbox_class)[self.appspecs_threemonth_classid].click()
            model.find_elements_by_class_name(self.input_class)[5].send_keys(price)
        elif limit == u'2年':
            model.find_elements_by_class_name(self.checkbox_class)[self.appspecs_twoyear_classid].click()
            model.find_elements_by_class_name(self.input_class)[6].send_keys(price)
        elif limit == u'6月':
            model.find_elements_by_class_name(self.checkbox_class)[self.appspecs_sixmonth_classid].click()
            model.find_elements_by_class_name(self.input_class)[7].send_keys(price)
        elif limit ==u'3年':
            model.find_elements_by_class_name(self.checkbox_class)[self.appspecs_threeyear_classid].click()
            model.find_elements_by_class_name(self.input_class)[8].send_keys(price)
        else:
            raise Exception('没有可选期限！')
        return self

    def appaddspec_licensemin(self,modelnum,minnum,screenshot_path):
        model=self.find_element_by_xpath(self.appspecs_xpath % dict (num = modelnum),screenshot_path)
        model.find_element_by_xpath(self.appspecs_licensemin_xpath).send_keys(minnum)
        return self

    def appaddspec_licensemax(self,modelnum,maxnum,screenshot_path):
        model=self.find_element_by_xpath(self.appspecs_xpath % dict (num = modelnum),screenshot_path)
        model.find_element_by_xpath(self.appspecs_licensemax_xpath).send_keys(maxnum)
        return self

    def appadd_times_modelname(self,modelnum,name,screenshot_path):
        model=self.find_element_by_xpath(self.appspecs_xpath % dict (num = modelnum),screenshot_path)
        model.find_element_by_xpath(self.appspecs_times_modelname_xpath).send_keys(name)
        return self

    def appadd_times_modelprice(self,modelnum,price,screenshot_path):
        model=self.find_element_by_xpath(self.appspecs_xpath % dict (num = modelnum),screenshot_path)
        model.find_element_by_xpath(self.appspecs_timeprice_xpath).send_keys(price)
        return self

    def appaddspec_times_licensemin(self,modelnum,minnum,screenshot_path):
        model=self.find_element_by_xpath(self.appspecs_xpath % dict (num = modelnum),screenshot_path)
        model.find_element_by_xpath(self.appspecs_times_licensemin_xpath).send_keys(minnum)
        return self

    def appaddspec_times_licensemax(self,modelnum,maxnum,screenshot_path):
        model=self.find_element_by_xpath(self.appspecs_xpath % dict (num = modelnum),screenshot_path)
        model.find_element_by_xpath(self.appspecs_times_licensemax_xpath).send_keys(maxnum)
        return self

    def appaddspec_negotiable(self,name,screenshot_path):
        self.find_element_by_xpath(self.appspecs_negotiable_modelname_xpath,screenshot_path).send_keys(name)
        return self

    def appaddspec_add(self,num,screenshot_path):
        self.find_element_by_xpath(self.appspecs_xpath % dict (num=num),screenshot_path).find_element_by_xpath(self.appspecs_add_xpath).click()
        return self

    def appadd_commit(self,screenshot_path):
        self.find_element_by_xpath(self.appspecs_commit_xpath,screenshot_path).click()
        return self

    def appadd_cancle(self,screenshot_path):
        self.find_element_by_xpath(self.appspecs_cancel_xpath,screenshot_path).click()
        return self

    def msg_pass(self,screenshot_path):
        if 'ivu-modal-hidden' not in self.driver.find_element_by_xpath(self.msg_xpath).get_attribute('class'):
            self.find_element_by_class_name(self.msg_button_class,screenshot_path).find_elements_by_tag_name('button')[self.msg_confirm_classid].click()
        return self

    #发布一个APP
    def appadd(self,data,screenshot_path):
        self.page_link(screenshot_path)
        self.appname(data['appname'],screenshot_path)
        self.apptype(data['typename'],screenshot_path)
        self.appvision(data['vision'],screenshot_path)
        self.appostype(data['os'],screenshot_path)
        time.sleep(2)
        self.appusers(data['users'],screenshot_path)
        self.appAmornot(data['amornot'],screenshot_path)
        if data['amornot']=='1':
            self.appAmtype(data['amtype'],screenshot_path)
        self.appaddress(data['address'],screenshot_path)
        self.applogo(data['logoimgpath'],screenshot_path)
        self.appdetail(data['appdetail'],data['trait'],data['guide'],screenshot_path)
        self.appsuportservice(data['suportdetail'],data['filepath'],screenshot_path)
        self.appcase(data['passcase'],screenshot_path)
        self.appaddspec_model(data['model'],screenshot_path)
        if data['model'] !=u'面议':
            self.appaddspec_license(data['licenseornot'],screenshot_path)
            if data['model']==u'按租期':
                for i in range(int(data['modelnums'])):
                    self.appadd_modelname(data['modelnum%s' % str(i+1)],data['modelname%s' % str(i+1)],screenshot_path)
                    pricetypes=data['limit%s' % str(i+1)].split('/')
                    prices=data['price%s' % str(i+1)].split('/')
                    for j in range(len(pricetypes)):
                        self.appadd_modelprice(data['modelnum%s' % str(i+1)],pricetypes[j],prices[j],screenshot_path)
                    if data['licenseornot'] !='0':
                        self.appaddspec_licensemin(data['modelnum%s' % str(i+1)],data['minnum%s' % str(i+1)],screenshot_path)
                        self.appaddspec_licensemax(data['modelnum%s' % str(i+1)],data['maxnum%s' % str(i+1)],screenshot_path)

                    if i<int(data['modelnums'])-1:
                        self.appaddspec_add(i+2,screenshot_path)
            elif data['model']==u'按次':
                for i in range(int(data['modelnums'])):
                    self.appadd_times_modelname(data['modelnum%s' % str(i+1)],data['modelname%s' % str(i+1)],screenshot_path)
                    self.appadd_times_modelprice(data['modelnum%s' % str(i+1)],data['price%s' % str(i+1)],screenshot_path)
                    if data['licenseornot'] !='0':
                        self.appaddspec_times_licensemin(data['modelnum%s' % str(i+1)],data['minnum%s' % str(i+1)],screenshot_path)
                        self.appaddspec_times_licensemax(data['modelnum%s' % str(i+1)],data['maxnum%s' % str(i+1)],screenshot_path)
                    if i<int(data['modelnums'])-1:
                        self.appaddspec_add(i+2,screenshot_path)
            else:
                raise Exception('检查数据中的规格模式是否正确！')
        else:
            self.appaddspec_negotiable(data['modelname1'],screenshot_path)

        self.appadd_commit(screenshot_path)
        time.sleep(2)
        return self


if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get('https://bccastle.com/')
    driver.maximize_window()
    mk=MarketHome(driver)
    mk.isv_login('testui','a123456','test.png')
    time.sleep(2)
    ad=Apppublish_page(driver)
    data = get_data(BASE_DIR+'\\datas\\add_app.csv')[0]
    ad.appadd(data,'1.png')








