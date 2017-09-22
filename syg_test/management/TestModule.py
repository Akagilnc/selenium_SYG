import time
from syg_test.Init import InitDriver
from selenium.webdriver.support.ui import Select
import sys
sys.stdout.buffer.write(chr(9986).encode('utf8'))


sleep_time = 4
class TestModule():
    @staticmethod
    def test_login(user_name, password, browser=None, page_url=""):
        global sleep_time
        if browser is None:
            browser = InitDriver.set_up_locally_chrome()
        if page_url != "":
            browser.get(page_url)
        time.sleep(sleep_time)
        input_account = browser.find_element_by_css_selector('#input-user-name input[name="username"]')
        input_password = browser.find_element_by_css_selector('#input-user-password input[name="password"]')
        btn_login = browser.find_element_by_id("btn-login")
        input_account.clear()
        input_account.send_keys(user_name)
        input_password.clear()
        input_password.send_keys(password)
        time.sleep(sleep_time)
        btn_login.click()
        time.sleep(sleep_time)

    @staticmethod
    def test_get_pass(email, browser = None, page_url = ""):
        if browser is None:
            browser = InitDriver.set_up_locally_chrome()
        if page_url != "":
            browser.get(page_url)
        time.sleep(sleep_time)
        btn_forget = browser.find_element_by_css_selector('#input-user-password + a')
        btn_forget.click()
        time.sleep(sleep_time)
        input_email = browser.find_element_by_css_selector('#email')
        btn_get = browser.find_element_by_id('btn-get')
        input_email.send_keys(email)
        btn_get.click()
        time.sleep(sleep_time)

    @staticmethod
    def test_dashboard(browser=None, page_url=""):
        if browser is None:
            browser = InitDriver.set_up_locally_chrome()
        if page_url != "":
            browser.get(page_url)
        link_order_waiting_delivery = browser.find_element_by_css_selector('.dashboard > div:first-child')
        link_order_waiting_delivery.click()
        time.sleep(sleep_time)
        time.sleep(sleep_time)

        condition_status = Select(browser.find_element_by_css_selector('#order-criteria > div > div:nth-child(6) > select'))

        assert condition_status.first_selected_option.get_attribute("value") == "WAITING_DELIVERY"
        time.sleep(sleep_time)

        link_home = browser.find_element_by_css_selector('.sidebar-menu > li:first-child a')
        link_home.click()
        time.sleep(sleep_time)





