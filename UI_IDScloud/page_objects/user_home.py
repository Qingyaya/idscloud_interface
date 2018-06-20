#-*-coding:utf-8-*-
from time import sleep

from selenium import webdriver

from page_objects.market_home import MarketHome
from public.base_page import BasePage
from public.Log import Log
log=Log()
class UserHome(BasePage):
    def Logout(self, screenshot_path):
        icon = self.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/ul/div/div[2]/li[3]/div[1]/span',screenshot_path)
        webdriver.ActionChains(self.driver).move_to_element(icon).perform()
        self.element_to_be_click_able_by_xpath('//*[@id="app"]/div/div/div[1]/ul/div/div[2]/li[3]/div[2]/ul/li[2]',screenshot_path).click()
        return self

    def Login(self,name,password,screenshot_path):
        mh=MarketHome(self.driver)
        mh.Login_link(screenshot_path)
        mh.Login(name,password,screenshot_path)
        icon = self.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/ul/li[9]/div[1]/span',screenshot_path)
        webdriver.ActionChains(self.driver).move_to_element(icon).perform()
        self.find_element_by_class_name('ivu-menu-drop-list',screenshot_path).find_elements_by_tag_name('li')[0].click()
        self.switch_to_lastwin()
        sleep(2)
        return self

    def homepage(self,screenshot_path):
        if 'ivu-menu-item-active' not in self.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/ul/div/div[2]/li[1]',screenshot_path).get_attribute('class'):
            self.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/ul/div/div[2]/li[1]',screenshot_path).click()
            sleep(2)

        return self

    def userapps(self,screenshot_path):
        self.homepage(screenshot_path)
        apps=self.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/section/div/div/div[2]/div[1]',screenshot_path)
        names=[app.text for app in apps.find_elements_by_tag_name('p')]
        return names


