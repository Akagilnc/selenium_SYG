import time
from syg_test.Init import InitDriver

class TestModule():
    @staticmethod
    def test_login(user_name, password, browser = None, page_url = ""):
        if browser is None:
            browser = InitDriver.set_up_locally()
        if page_url != "":
            browser.get(page_url)
        time.sleep(5)
        input_account = browser.find_element_by_css_selector('#input-user-name input[name="username"]')
        input_password = browser.find_element_by_css_selector('#input-user-password input[name="password"]')
        btn_login = browser.find_element_by_id("btn-login")
        input_account.send_keys(user_name)
        input_password.send_keys(password)
        btn_login.click()
        time.sleep(5)

    @staticmethod
    def test_get_pass(email, browser = None, page_url = ""):
        if browser is None:
            browser = InitDriver.set_up_locally()
        if page_url != "":
            browser.get(page_url)
        time.sleep(5)
        btn_forget = browser.find_element_by_css_selector('#input-user-password + a')
        btn_forget.click()
        time.sleep(5)
        input_email = browser.find_element_by_css_selector('#email')
        btn_get = browser.find_element_by_id('btn-get')
        input_email.send_keys(email)
        btn_get.click()
        time.sleep(5)