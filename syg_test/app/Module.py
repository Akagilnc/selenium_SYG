import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from ..Init import InitDriver

class TestModule():
    @staticmethod
    def detail(home_page_url,sleep_time,browser):
        browser.get(home_page_url)
        time.sleep(sleep_time)
        agree_checkbox = browser.find_element_by_css_selector('.checkbox')
        add = browser.find_element_by_css_selector('.add')
        submit_btn = browser.find_element_by_css_selector('.purchase-btn')

        time.sleep(sleep_time)
        agree_checkbox.click()
        add.click()
        submit_btn.click()

        time.sleep(sleep_time)
        # 跳转到登陆画面
        assert 'syg-login' in browser.title

    def login(username,password,browser):
        account_elem = browser.find_element_by_id('account')
        password_elem = browser.find_element_by_id('password')
        login_btn = browser.find_element_by_css_selector('#submit_btn')

        account_elem.send_keys(username)
        password_elem.send_keys(password)
        password_elem.send_keys(Keys.ENTER)
        time.sleep(2)
        # 跳转到地址选择画面
        print(browser.title)
        assert 'syg-has-address' in browser.title

    def no_address(address,name,phone,browser):
        province_select = Select(browser.find_element_by_css_selector('#province'))
        city_select = Select(browser.find_element_by_css_selector('#city'))
        district_select = Select(browser.find_element_by_css_selector('#district'))
        address_textarea = browser.find_element_by_css_selector('textarea')
        person_name_input = browser.find_element_by_css_selector('input[name="recipientName"]')
        phone_input = browser.find_element_by_css_selector('input[name="tel"]')
        default_checkbox = browser.find_element_by_css_selector('.checkbox')
        confirm_btn = browser.find_element_by_css_selector('#submit_btn')

        province_select.select_by_index(10)
        city_select.select_by_value('111')
        district_select.select_by_index(1)

        address_textarea.send_keys(address)
        person_name_input.send_keys(name)
        phone_input.send_keys(phone)
        default_checkbox.click()
        confirm_btn.click()




