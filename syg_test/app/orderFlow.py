import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from syg_test.Init import InitDriver

home_page_url = 'http://47.94.123.58:2334/login'
class order_flow(unittest.TestCase):
    def test_login_in_SYG(self):
        browser = InitDriver.set_up_locally()

        # 打开SYG页面
        browser.get('http://47.94.123.58:2334/product/SKII-0066')
        time.sleep(0.5)
        # assert 'href="/login"' in browser.page_source

        login_elem = browser.find_element_by_css_selector(
            'body > div > header > div > div.user-option > a:nth-child(1) > span')
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

        time.sleep(4)

        assert "商品详情" in browser.title

        time.sleep(3)
        browser.quit()




if __name__ == '__main__':
    unittest.main()

