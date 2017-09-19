import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from ..Init import InitDriver

# home_page_url = 'http://47.94.123.58:2334/customer/toInformation'
home_page_url = 'http://47.94.123.58:2334/login'

class userInformation(unittest.TestCase):
    def test_login_userInformation(self):
        browser = InitDriver.set_up_locally()
        browser.get(home_page_url)
        account=browser.find_element_by_css_selector('#account')
        password=browser.find_element_by_css_selector('#password')
        sign_up_btn = browser.find_element_by_css_selector('#submit_btn')
        account.send_keys('15881087265')
        password.send_keys('11111q')
        sign_up_btn.click()
        time.sleep(4)
        browser.get('http://47.94.123.58:2334/customer/toInformation')

        user_name = browser.find_element_by_css_selector('#customerName')
        gender_female = browser.find_element_by_css_selector('#female')
        gender_male = browser.find_element_by_css_selector('#male')
        save = browser.find_element_by_css_selector('#submit_btn')
        body = browser.find_element_by_css_selector('body')
        # copy_btn = browser.find_element_by_css_selector('.copy')
        user_name.clear()
        user_name.send_keys('李宇春')
        user_name.send_keys('陈秋霞')
        gender_male.is_selected()
        body.click()


        time.sleep(3)
        browser.quit()


if __name__ == '__main__':
    unittest.main()

