import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from Init import InitDriver

# home_page_url = 'http://47.94.123.58:2334/customer/toInformation'
home_page_url = 'http://47.94.123.58:2334/login'

class userInformation(unittest.TestCase):
    def test_login_userInformation(self):
        browser = InitDriver.set_up_locally()
        browser.get(home_page_url)
        sign_up_btn = browser.find_element_by_css_selector('#forgetPassword')

        sign_up_btn.click()
        time.sleep(4)
        browser.get('http://47.94.123.58:2334/customer/toInformation')
        user_name = browser.find_element_by_css_selector('.username')
        gender_female=Select(browser.find_element_by_css_selector('#female'))
        gender_male=Select(browser.find_element_by_css_selector('#male'))
        copy_btn= browser.find_element_by_css_selector('.copy')
        user_name.send_keys('李宇春')
        gender_male.click()
        copy_btn.click()




