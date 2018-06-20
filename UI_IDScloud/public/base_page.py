# coding=UTF-8
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidElementStateException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from datas.setting import *
from public.Log import Log

log = Log()

def fail_on_screenshot(function):

    def wrapper(*args, **kwargs):
        instance, selector,pathname = args[0], args[1],args[2]
        try:
            return function(*args, **kwargs)
        except (TimeoutException, NoSuchElementException, InvalidElementStateException) as ex:
            log.error("Could not find the selector: [{}].".format(selector))
            # log.debug(instance.driver.page_source)
            instance.driver.save_screenshot(pathname)
            raise ex
    return wrapper


class BasePage(object):
    url = ""
    base_url = BASE_URL

    def __init__(self, driver, url_params=None):
        if not url_params:
            url_params = []
        self.driver = driver
        self.url_params = url_params

    def refresh(self):
        self.driver.refresh()

    def navigate_back(self):
        self.driver.back()

    def get_current_page_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title

    def get_cookie_value(self):
        return self.driver.get_cookie('client_identity')['value']

    def win_handls(self):
        return self.driver.window_handles

    def switch_to_lastwin(self):
        wins=self.driver.window_handles
        return self.driver.switch_to.window(wins[-1])

    def click_ele_xpath_until_pass(self, selector):
        for i in range(30):
            try:
                self.driver.find_element_by_xpath(selector).click()
                break
            except:
                pass
    def click_ele_until_pass(self,ele):
        start=time.time()
        while time.time()-start <10:
            try:
                ele.click()
                break
            except:
                pass


#-------------------------------------------------------------------------------------------------------------------

    '''判断元素是否存在，存在返回TRUE，不存在False'''
    def is_exist_element_xpath(self,selector):
        try:
            self.driver.find_element_by_xpath(selector)
            flag=True
        except:
            flag=False
        return flag

    '''判断元素是否可见，如果可见就返回这个元素'''
    @fail_on_screenshot
    def visib_element_by_xpath(self,selector,name,wait_time=WAIT_TIME):
        return  WebDriverWait(self.driver,wait_time).until(
            expected.visibility_of(self.driver.find_element(By.XPATH,selector)))


    # ---------------------------------------------------------------------------------------------------------------
    '''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''

    @fail_on_screenshot
    def find_element_by_css(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    @fail_on_screenshot
    def find_element_by_link_text(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.visibility_of_element_located((By.LINK_TEXT, selector)))

    @fail_on_screenshot
    def find_element_by_partial_link_text(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.visibility_of_element_located((By.PARTIAL_LINK_TEXT, selector)))

    @fail_on_screenshot
    def find_element_by_id(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.visibility_of_element_located((By.ID, selector)))

    @fail_on_screenshot
    def find_element_by_xpath(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.visibility_of_element_located((By.XPATH, selector)))

    @fail_on_screenshot
    def find_element_by_name(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.visibility_of_element_located((By.NAME, selector)))

    @fail_on_screenshot
    def find_element_by_class_name(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.visibility_of_element_located((By.CLASS_NAME, selector)))

    @fail_on_screenshot
    def find_element_by_tag_name(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.visibility_of_element_located((By.TAG_NAME, selector)))

    # ----------------------------------------------------------------------------------------------------------------
    '''判断是否至少有1个元素存在于dom树中，如果定位到就返回列表'''

    @fail_on_screenshot
    def find_elements_by_css(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

    @fail_on_screenshot
    def find_elements_by_class_name(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.presence_of_all_elements_located((By.CLASS_NAME, selector)))

    @fail_on_screenshot
    def find_elements_by_link_text(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.presence_of_all_elements_located((By.LINK_TEXT, selector)))

    @fail_on_screenshot
    def find_elements_by_xpath(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.presence_of_all_elements_located((By.XPATH, selector)))

    @fail_on_screenshot
    def find_elements_by_tag_name(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.presence_of_all_elements_located((By.TAG_NAME, selector)))

    # -------------------------------------------------------------------------------------------------------------
    '''判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回这个元素'''

    @fail_on_screenshot
    def invisible_element_by_id(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.invisibility_of_element_located((By.ID, selector)))

    @fail_on_screenshot
    def invisible_element_by_xpath(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.invisibility_of_element_located((By.XPATH, selector)))

    @fail_on_screenshot
    def invisible_element_by_css(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.invisibility_of_element_located((By.CSS_SELECTOR, selector)))

    @fail_on_screenshot
    def invisible_element_by_link_text(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.invisibility_of_element_located((By.LINK_TEXT, selector)))

    @fail_on_screenshot
    def invisible_element_by_name(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.invisibility_of_element_located((By.NAME, selector)))

    @fail_on_screenshot
    def invisible_element_by_class_name(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.invisibility_of_element_located((By.CLASS_NAME, selector)))

    @fail_on_screenshot
    def invisible_element_by_tag_name(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.invisibility_of_element_located((By.TAG_NAME, selector)))

    @fail_on_screenshot
    def invisible_element_by_partial_link_text(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.invisibility_of_element_located((By.PARTIAL_LINK_TEXT, selector)))

    # -----------------------------------------------------------------------------------------------------------------

    '''判断指定的元素中是否包含了预期的字符串，返回布尔值'''

    @fail_on_screenshot
    def text_to_be_present_in_element_by_id(self, selector,name, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.driver, wait_time).until(
            expected.text_to_be_present_in_element((By.ID, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_by_name(self, selector,name, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.driver, wait_time).until(
            expected.text_to_be_present_in_element((By.NAME, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_by_class_name(self, selector,name, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.driver, wait_time).until(
            expected.text_to_be_present_in_element((By.CLASS_NAME, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_by_xpath(self, selector,name, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.driver, wait_time).until(
            expected.text_to_be_present_in_element((By.XPATH, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_by_tag_name(self, selector,name, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.driver, wait_time).until(
            expected.text_to_be_present_in_element((By.TAG_NAME, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_by_css(self, selector,name, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.driver, wait_time).until(
            expected.text_to_be_present_in_element((By.CSS_SELECTOR, selector),text))

    # -----------------------------------------------------------------------------------------------------------------

    '''判断指定元素的属性值中是否包含了预期的字符串，返回布尔值'''

    @fail_on_screenshot
    def text_to_be_present_in_element_value_by_css(self, selector,name, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.driver, wait_time).until(
            expected.text_to_be_present_in_element_value((By.CSS_SELECTOR, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_value_by_id(self, selector,name, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.driver, wait_time).until(
            expected.text_to_be_present_in_element_value((By.ID, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_value_by_name(self, selector,name, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.driver, wait_time).until(
            expected.text_to_be_present_in_element_value((By.NAME, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_value_by_css_name(self, selector,name, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.driver, wait_time).until(
            expected.text_to_be_present_in_element_value((By.CLASS_NAME, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_value_by_xpath(self, selector,name, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.driver, wait_time).until(
            expected.text_to_be_present_in_element_value((By.XPATH, selector),text))

    @fail_on_screenshot
    def text_to_be_present_in_element_value_by_tag_name(self, selector,name, wait_time=WAIT_TIME,text=None):
        return WebDriverWait(self.driver, wait_time).until(
            expected.text_to_be_present_in_element_value((By.TAG_NAME, selector),text))


    # -----------------------------------------------------------------------------------------------------------------
    '''判断title,返回布尔值'''

    @fail_on_screenshot
    def page_title_is(self, title, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(expected.title_is(title))

    @fail_on_screenshot
    def page_title_contains(self, title, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(expected.title_contains(title))

    # -----------------------------------------------------------------------------------------------------------------

    '''判断某个元素中是否可见并且是enable的，代表可点击'''

    @fail_on_screenshot
    def element_to_be_click_able_by_id(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.element_to_be_clickable((By.ID, selector)))

    @fail_on_screenshot
    def element_to_be_click_able_by_name(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.element_to_be_clickable((By.NAME, selector)))

    @fail_on_screenshot
    def element_to_be_click_able_by_class_name(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.element_to_be_clickable((By.CLASS_NAME, selector)))

    @fail_on_screenshot
    def element_to_be_click_able_by_css(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    @fail_on_screenshot
    def element_to_be_click_able_by_tag_name(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.element_to_be_clickable((By.TAG_NAME, selector)))

    @fail_on_screenshot
    def element_to_be_click_able_by_xpath(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.element_to_be_clickable((By.XPATH, selector)))

    @fail_on_screenshot
    def element_to_be_click_able_by_link_text(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.element_to_be_clickable((By.LINK_TEXT, selector)))

    # -----------------------------------------------------------------------------------------------------------------

    '''判断元素是否可见，如果可见就返回这个元素，不可见返回False'''

    @fail_on_screenshot
    def visibility_of_element_by_id(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.visibility_of_element_located((By.ID, selector)))

    @fail_on_screenshot
    def visibility_of_element_by_name(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.visibility_of_element_located((By.NAME, selector)))

    @fail_on_screenshot
    def visibility_of_element_by_class_name(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.visibility_of_element_located((By.CLASS_NAME, selector)))

    @fail_on_screenshot
    def visibility_of_element_by_css(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    @fail_on_screenshot
    def visibility_of_element_by_xpath(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.visibility_of_element_located((By.XPATH, selector)))

    @fail_on_screenshot
    def visibility_of_element_by_tag_name(self, selector,name, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(
            expected.visibility_of_element_located((By.TAG_NAME, selector)))

    def get_cookie_by_name(self, name):
        cookie = self.driver.get_cookie(name)
        return cookie['value']

    def get_session_id(self):
        return self.get_cookie_by_name("TSID")