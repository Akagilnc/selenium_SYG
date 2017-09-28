import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from ..Init import InitDriver
from ..test import TryLoginAndBackToProductPage
from .Module import TestModule


browser = InitDriver.set_up_locally_firefox()
sleep_time = 2
home_page_url = 'http://47.94.123.58:2334/product/SKII-0066'
login_page_url = 'http://47.94.123.58:2334/login'


class order_flow(unittest.TestCase):
    account = '13800008474'
    TryLoginAndBackToProductPage.test_sign_up(account, browser)
    #TestModule.detail(home_page_url,browser)
    # browser.get(login_page_url)
    # TestModule.login(account,"a123456",browser)
    time.sleep(sleep_time)
    TestModule.order(browser)
    time.sleep(sleep_time)
    if 'syg-has-address' == browser.title:
        TestModule.no_address("天府长城西路天西六百社区斗鱼小区二期10栋8单元22号","LNC",account,browser)
    elif '订单' == browser.title:
        TestModule.order_details(browser)

    time.sleep(2)
    browser.quit()


if __name__ == '__main__':
    unittest.main()

