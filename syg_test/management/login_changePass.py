import time
import unittest

from ..Init import InitDriver
from syg_test.management.TestModule import TestModule

home_page_url = 'http://47.94.123.58:2333/admin/login'

class TryLogin(unittest.TestCase):

    TestModule.test_login("13800001111", "1234567", home_page_url)
    time.sleep(5)

    TestModule.test_get_pass("1234@1111.com")
    time.sleep(5)

    TestModule.test_login("13800001111", "12345678")
    time.sleep(5)

    '''
    mng_user = browser.find_element_by_css_selector('.sidebar-menu li:first-child a')
    mng_user.click()
    
    time.sleep(4)
    
    search_customername = browser.find_element_by_css_selector('#customerName');
    search_phonenumber = browser.find_element_by_css_selector('#search-form .row > .form-group:nth-child(2) input[type="text"]');
    search_btn = browser.find_element_by_css_selector('#search')
    search_customername.send_keys('sko')
    search_btn.click()
    
    time.sleep(4)
    
    search_customername.clear();
    search_phonenumber.send_keys(180)
    search_btn.click()
    
    time.sleep(10)
   '''



if __name__ == '__main__':
    unittest.main()