import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from ..Init import InitDriver
from .Module import TestModule

browser = InitDriver.set_up_locally_firefox()
sleep_time = 1
home_page_url = 'http://47.94.123.58:2334/product/SKII-0066'
class order_flow(unittest.TestCase):
    TestModule.detail(home_page_url,sleep_time,browser)
    TestModule.login("15881087265","11111q",browser)
    TestModule.no_address("天府长城西路天西六百社区斗鱼小区二期10栋8单元22号","LNC","158810872165",browser)



    browser.quit()


if __name__ == '__main__':
    unittest.main()

