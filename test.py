import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TryLoginAndBackToProductPage(unittest.TestCase):
    def setUp(self):
        ## 创建浏览器对象
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.browser.set_window_size(1680, 1080)

    def test_process_in_SYG(self):
        browser = self.browser
        ## 打开SYG页面
        browser.get('http://10.10.10.54:2334/product/SKII-0066')
        time.sleep(4)
        assert 'href="/login"' in browser.page_source

        login_elem = browser.find_element_by_xpath('/html/body/div/header/div/div[2]/a[1]/span')
        login_elem.click()
        time.sleep(4)
        assert 'syg-login' in browser.title

        account_elem = browser.find_element_by_id('account')
        password_elem = browser.find_element_by_id('password')
        account_elem.clear()
        account_elem.send_keys('13800001111')
        password_elem.send_keys('a123456')
        account_elem.click()
        time.sleep(0.5)
        login_btn = browser.find_element_by_id('submit_btn')
        login_btn.click()
        time.sleep(4)
        assert "商品详情" in browser.title

    def setDown(self):
        time.sleep(10)
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()