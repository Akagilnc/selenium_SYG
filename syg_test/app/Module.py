import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from ..Init import InitDriver


sleep_time = 2
class TestModule():
    @staticmethod
    def detail(home_page_url,browser):
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
        assert 'syg-login' == browser.title

    @staticmethod
    def login(username,password,browser):
        account_elem = browser.find_element_by_id('account')
        password_elem = browser.find_element_by_id('password')
        login_btn = browser.find_element_by_css_selector('#submit_btn')
        assert login_btn.is_displayed()

        account_elem.send_keys(username)
        password_elem.send_keys(password)
        password_elem.send_keys(Keys.ENTER)
        time.sleep(4)
        # 跳转到地址选择画面
        assert '商品详情' == browser.title

    @staticmethod
    def order(browser):
        order_12times_elem = browser.find_element_by_css_selector('#btn > div.btn-switch > button:nth-child(2)')
        agreement_checkbox = browser.find_element_by_css_selector('#btn > div.checkbox > label')
        add_btn = browser.find_element_by_css_selector('#item_picker > button.add')
        sub_btn = browser.find_element_by_css_selector('#item_picker > button.reduce')
        order_btn = browser.find_element_by_css_selector('#order')

        order_12times_elem.click()
        add_btn.click()
        add_btn.click()
        sub_btn.click()
        agreement_checkbox.click()
        assert order_btn.is_enabled()
        order_btn.click()
        time.sleep(sleep_time + 2)
        assert 'syg-has-address' == browser.title or '订单' == browser.title

    @staticmethod
    def no_address(address,name,phone,browser):
        province_select = Select(browser.find_element_by_css_selector('#province'))
        city_select = Select(browser.find_element_by_css_selector('#city'))
        district_select = Select(browser.find_element_by_css_selector('#district'))
        address_textarea = browser.find_element_by_css_selector('textarea')
        person_name_input = browser.find_element_by_css_selector('input[name="recipientName"]')
        phone_input = browser.find_element_by_css_selector('input[name="tel"]')
        default_checkbox = browser.find_element_by_css_selector('.checkbox')
        confirm_btn = browser.find_element_by_css_selector('#submit_btn')

        time.sleep(0.5)
        province_select.select_by_index(4)
        time.sleep(4)
        city_select.select_by_index(2)
        district_select.select_by_index(1)

        address_textarea.send_keys(address)
        time.sleep(0.5)
        person_name_input.send_keys(name)
        time.sleep(0.5)
        phone_input.send_keys(phone)
        time.sleep(0.5)
        default_checkbox.click()
        time.sleep(0.5)

        assert confirm_btn.is_enabled()
        confirm_btn.click()

    @staticmethod
    def order_details(browser):
        order_btn = browser.find_element_by_css_selector(".purchase-btn")

        order_btn.click()

        assert '支付页面' == browser.title




