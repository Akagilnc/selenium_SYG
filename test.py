import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from Init import InitDriver


class TryLoginAndBackToProductPage(unittest.TestCase):

    def setUpLocally(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.browser.set_window_size(1680, 1080)
        return self.browser

    def test_login_in_SYG(self):
        browser = self.setUpLocally()
        #browser = InitDriver.setUp()

        ## 打开SYG页面
        browser.get('http://10.10.10.54:2334/product/SKII-0066')
        time.sleep(4)
        # assert 'href="/login"' in browser.page_source

        login_elem = browser.find_element_by_css_selector('body > div > header > div > div.user-option > a:nth-child(1) > span')
        login_elem.click()
        time.sleep(4)

        assert 'syg-login' in browser.title

        account_elem = browser.find_element_by_css_selector('#account')
        password_elem = browser.find_element_by_id('password')
        login_btn = browser.find_element_by_css_selector('#submit_btn')

        account_elem.clear()
        account_elem.send_keys('13800001111')
        password_elem.send_keys('a123456')
        password_elem.send_keys(Keys.ENTER)

        time.sleep(0.5)

        login_btn.click()
        time.sleep(4)

        assert "商品详情" in browser.title

        time.sleep(3)
        browser.quit()


if __name__ == '__main__':
    unittest.main()