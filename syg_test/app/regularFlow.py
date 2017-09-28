import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from ..Init import InitDriver
from .Module import TestModule
browser = InitDriver.set_up_locally_firefox()
sleep_time = 1
admin_home_page = 'http://47.94.123.58:2333/backyard/admin/login'
login_page_url = 'http://47.94.123.58:2334/login'
start_time='2017-09-28'
end_time='2017-09-28'
class regular_flow(unittest.TestCase):
    TestModule.admin_login("13811111111",browser,"a123456",admin_home_page)
    time.sleep(sleep_time)
    TestModule.admin_coupon(browser)
    time.sleep(sleep_time)
    TestModule.admin_coupon_add(browser,start_time,end_time)










if __name__ == '__main__':
        unittest.main()
