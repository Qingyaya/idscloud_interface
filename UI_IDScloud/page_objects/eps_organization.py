import time,re

from selenium.webdriver.common.keys import Keys

from public.base_page import BasePage
from datas.setting import *
from page_objects.market_home import MarketHome
from selenium import webdriver
class Epsorg(BasePage):
    search_xpath='//input[@placeholder="搜索部门"]'
    tree_class='ivu-tree-children'
    edit_delete_state_xpath='//button[@class= "short-btn ivu-btn ivu-btn-ghost"]'
    edit_delete_button_xpath='//button[@class= "short-btn ivu-btn ivu-btn-ghost"]//span'
    editbutton_id=0
    upprocedue_id=1
    delebutton_id=2
    addbutton_xpath='//span[text()="添加子部门"]'
    childorg_head_class='ivu-table-header'
    childall_check='ivu-checkbox-input'
    childorgrows_class='ivu-table-row'
    org_edit_class='ivu-modal-body'
    org_edit_xpath='//form[contains(@class,"editDepForm")]'
    addorg_edit=0
    edit_org_tag='input'
    edit_org_no=0
    edit_org_name=1
    edit_org_comment_tag='textarea'
    edit_ord_submit_class='ivu-modal-footer'
    addorg_submit=0
    edit_org_submit_tag='button'
    addorg_ok=0
    editorg_ok=1
    addorg_cancle=2
    addorg_error_class='ivu-form-item-error-tip'
    dele_ok_xpath='(//button[@class="short-btn ivu-btn ivu-btn-ghost ivu-btn-large"])[1]'
    dele_cancle_xpath='(//button[@class="short-btn ivu-btn ivu-btn-ghost ivu-btn-large"])[2]'
    dele_msg_class='ivu-message-notice'
    imex_button_class='ivu-dropdown-rel'
    im_ex_class='ivu-dropdown-item'
    import_button=0
    export_button=1
    im_choosefile_xpath='//div[@class="ivu-upload ivu-upload-select"]'
    imperr_class="ivu-message-notice"
    succ_fail_num_class='ivu-alert-desc'
    succ_num=0
    fail_num=1
    failmsg_table_class='ivu-table-tbody'
    impass_xpath='//button[@class="ivu-btn ivu-btn-primary"]'

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
        ele=ele.find_elements_by_tag_name('li')[1]
        if 'ivu-menu-item-active' not in ele.get_attribute('class'):
            ele.click()
        return self

    def search(self,keys,screenshot_path):
        self.find_element_by_xpath(self.search_xpath,screenshot_path).clear()
        self.find_element_by_xpath(self.search_xpath,screenshot_path).send_keys(keys)
        self.find_element_by_xpath(self.search_xpath, screenshot_path).send_keys(Keys.ENTER)

    def choose_org(self,namepath,screenshot_path):
        names=namepath.split('/')
        eles = self.find_elements_by_class_name(self.tree_class,screenshot_path)
        if len(names)>1:
            for i in range(1,len(names)-1):
                for ele in eles:
                    if ele.find_elements_by_tag_name('span')[1].text==names[i]:
                        ele.find_elements_by_tag_name('span')[0].click()
                        time.sleep(3)
                        elem=ele
                        break
                eles=elem.find_elements_by_tag_name('li')
        for ele in eles:
            if ele.find_elements_by_tag_name('span')[1].text == names[-1]:
                ele.find_elements_by_tag_name('span')[1].click()
                time.sleep(3)
                break

    def choose_childorg(self,name,screenshot_path):
        rows=self.find_elements_by_class_name(self.childorgrows_class,screenshot_path)
        for row in rows:
            if row.find_elements_by_tag_name('td')[2].find_element_by_tag_name('span').text == name:
                row.find_elements_by_tag_name('td')[0].find_element_by_class_name('ivu-checkbox-input').click()
                break
        time.sleep(1)
        return self

    def choose_allchildorg(self,screenshot_path):
        self.find_element_by_class_name(self.childorg_head_class,screenshot_path).find_element_by_class_name(self.childall_check).click()
        return self


    def editbutton_state(self,screenshot_path):
        state=self.find_elements_by_xpath(self.edit_delete_state_xpath,screenshot_path)[self.editbutton_id].get_attribute('disabled')
        return state

    def editbutton_click(self, screenshot_path):
        self.find_elements_by_xpath(self.edit_delete_button_xpath, screenshot_path)[self.editbutton_id].click()
        time.sleep(2)
        return self

    def addorgbutton(self,screenshot_path):
        self.find_element_by_xpath(self.addbutton_xpath,screenshot_path).click()
        return self

    def delebutton(self,screenshot_path):
        self.find_elements_by_xpath(self.edit_delete_button_xpath,screenshot_path)[self.delebutton_id].click()
        time.sleep(2)
        return self

    def importbutton(self,screenshot_path):
        self.find_element_by_xpath(self.eximbutton_xpath,screenshot_path).click()
        self.find_element_by_xpath(self.imbutton_xpath,screenshot_path).click()
        return self

    def exportbutton(self,screenshot_path):
        self.find_element_by_xpath(self.eximbutton_xpath,screenshot_path).click()
        self.find_element_by_xpath(self.exbutton_xpath,screenshot_path).click()
        return self

    def addorgpage(self,no,name,comment,screenshot_path):
        edit=self.find_elements_by_class_name(self.org_edit_class,screenshot_path)[self.addorg_edit]
        edit.find_elements_by_tag_name(self.edit_org_tag)[self.edit_org_no].send_keys(no)
        edit.find_elements_by_tag_name(self.edit_org_tag)[self.edit_org_name].send_keys(name)
        edit.find_element_by_tag_name(self.edit_org_comment_tag).send_keys(comment)
        return self

    def editorgpage(self,no,name,comment,screenshot_path):
        edit=self.find_element_by_xpath(self.org_edit_xpath,screenshot_path)
        edit.find_elements_by_tag_name(self.edit_org_tag)[self.edit_org_no].clear()
        edit.find_elements_by_tag_name(self.edit_org_tag)[self.edit_org_no].send_keys(no)
        edit.find_elements_by_tag_name(self.edit_org_tag)[self.edit_org_name].clear()
        edit.find_elements_by_tag_name(self.edit_org_tag)[self.edit_org_name].send_keys(name)
        edit.find_element_by_tag_name(self.edit_org_comment_tag).clear()
        edit.find_element_by_tag_name(self.edit_org_comment_tag).send_keys(comment)
        return self

    def addorgok(self,screenshot_path):
        submit=self.find_elements_by_class_name(self.edit_ord_submit_class,screenshot_path)[self.addorg_submit]
        submit.find_elements_by_tag_name(self.edit_org_submit_tag)[self.addorg_ok].click()
        time.sleep(3)
        return self

    def editorgok(self,screenshot_path):
        submit=self.find_elements_by_class_name(self.edit_ord_submit_class,screenshot_path)[self.addorg_submit]
        submit.find_elements_by_tag_name(self.edit_org_submit_tag)[self.editorg_ok].click()
        time.sleep(3)
        return self

    def addorgcancle(self,screenshot_path):
        submit=self.find_elements_by_class_name(self.edit_ord_submit_class,screenshot_path)[self.addorg_submit]
        submit.find_elements_by_tag_name(self.edit_org_submit_tag)[self.addorg_cancle].click()
        return self

    def addpage_error(self,screenshot_path):
        eles=self.find_elements_by_class_name(self.addorg_error_class,screenshot_path)
        msgs=[]
        for ele in eles:
            msgs.append(ele.text.strip())
        return msgs

    def deleok(self,screenshot_path):
        self.find_element_by_xpath(self.dele_ok_xpath,screenshot_path).click()
        return self

    def delecancle(self,screenshot_path):
        self.find_element_by_xpath(self.dele_cancle_xpath,screenshot_path).click()
        return self

    def delemsg(self,screenshot_path):
        ele=self.find_element_by_class_name(self.dele_msg_class,screenshot_path)
        msg=ele.find_element_by_tag_name('span').text
        return msg

    def imbutton_click(self,screenshot_path):
        icon=self.find_element_by_class_name(self.imex_button_class,screenshot_path)
        webdriver.ActionChains(self.driver).move_to_element(icon).perform()
        time.sleep(2)
        self.find_elements_by_class_name(self.im_ex_class,screenshot_path)[self.import_button].click()
        time.sleep(3)
        return self

    def im_choosefile(self,filepath,screenshot_path):
        self.find_element_by_xpath(self.im_choosefile_xpath,screenshot_path).click()
        l='%s\\import_busi_license.exe %s'%(BASE_DIR,filepath)
        os.system(l)
        time.sleep(3)
        return self

    def impage_error(self,screenshot_path):
        ele=self.find_element_by_class_name(self.imperr_class,screenshot_path,120)
        msg=ele.find_element_by_tag_name('span').text
        return msg

    def impass(self,screenshot_path):
        self.find_element_by_xpath(self.impass_xpath,screenshot_path,200)
        return self

    def impass_click(self,screenshot_path):
        self.find_element_by_xpath(self.impass_xpath,screenshot_path).click()
        return self

    def imresult(self,screenshot_path):
        ele=self.find_element_by_class_name(self.succ_fail_num_class,screenshot_path)
        succ=ele.find_elements_by_tag_name('p')[self.succ_num].text
        succ=re.sub('\D','',succ)
        fail=ele.find_elements_by_tag_name('p')[self.fail_num].text
        fail=re.sub('\D','',fail)
        return succ,fail

    def im_failmsg(self,screenshot_path):
        msgs=[]
        table=self.find_element_by_class_name(self.failmsg_table_class,screenshot_path)
        rows=table.find_elements_by_tag_name('tr')
        for row in rows:
            msg = {}
            msg['No']=row.find_elements_by_tag_name('td')[0].text.strip()
            msg['Name']=row.find_elements_by_tag_name('td')[1].text.strip()
            msg['parentorg']=row.find_elements_by_tag_name('td')[2].text.strip()
            msg['commit']=row.find_elements_by_tag_name('td')[3].text.strip()
            msg['Msg']=row.find_elements_by_tag_name('td')[4].text.strip()
            msgs.append(msg)
        return msgs

    def exbutton_click(self,screenshot_path):
        icon=self.find_element_by_class_name(self.imex_button_class,screenshot_path)
        webdriver.ActionChains(self.driver).move_to_element(icon).perform()
        time.sleep(2)
        self.find_elements_by_class_name(self.im_ex_class,screenshot_path)[self.export_button].click()
        time.sleep(5)
        return self
