import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from ..Init import InitDriver


home_page_url = 'http://47.94.123.58:2334/product/SKII-0066'
class order_flow(unittest.TestCase):
    @staticmethod
    def test_login():
        browser = InitDriver.set_up_locally_firefox()
        browser.get(home_page_url)
        time.sleep(5)
        agree_checkbox= browser.find_element_by_css_selector('.checkbox')
        add=browser.find_element_by_css_selector('.add')
        submit_btn=browser.find_element_by_css_selector('.purchase-btn')

        time.sleep(2)
        agree_checkbox.click()
        add.click()
        submit_btn.click()

        time.sleep(2)
        # 跳转到登陆画面
        assert 'syg-login' in browser.title

    @staticmethod
    def login():
        account_elem=browser.find_element_by_css_selector('#account')
        password_elem = browser.find_element_by_id('password')
        login_btn = browser.find_element_by_css_selector('#submit_btn')

        account_elem.clear()
        account_elem.send_keys('15881087265')
        password_elem.send_keys('11111q')
        password_elem.send_keys(Keys.ENTER)


        # 跳转到推荐码设置画面
        assert 'syg-syg-recommend-code' in browser.title

    @staticmethod
    def recommend(self):
        recommend_input=browser.find_element_by_css_selector('input[name="recommend"]')
        recommend_btn=browser.find_element_by_css_selector('button[type="submit"]')

        recommend_input.send_keys('QQQQQQQQ')
        recommend_btn.click()

        # 跳转到地址选择画面
        assert 'syg-syg-recommend-code' in browser.title


if __name__ == '__main__':
    unittest.main()

