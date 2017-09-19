import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from Init import InitDriver

home_page_url = 'http://47.94.123.58:2334/login'


class TryLoginAndBackToProductPage(unittest.TestCase):

    def test_sign_up(self):
        browser = InitDriver.set_up_locally()

        browser.get(home_page_url)

        sign_up_btn = browser.find_element_by_css_selector('#forgetPassword')

        sign_up_btn.click()
        time.sleep(4)

        assert True

        phonenum_input = browser.find_element_by_css_selector('#account')
        verify_code_input = browser.find_element_by_css_selector(
            '#sign_up_form > div > div:nth-child(2) > div.verification-pc > div > input')
        password_input = browser.find_element_by_css_selector(
            '#sign_up_form > div > div:nth-child(4) > div.password.form-control > input')
        confirm_pass_input = browser.find_element_by_css_selector('#password_confirm')
        agree_checkbox = browser.find_element_by_css_selector('#agreement')
        submit_btn = browser.find_element_by_css_selector('#submit_btn')

        phonenum_input.send_keys('13800001111')
        verify_code_input.send_keys('123456')
        password_input.send_keys('a123456')
        confirm_pass_input.send_keys('a123456')
        time.sleep(0.5)

        agree_checkbox.click()

        time.sleep(0.5)

        submit_btn.click()

        time.sleep(4)

        assert 'syg-syg-recommend-code' in browser.title

        recommend_code_input = browser.find_element_by_css_selector('#recommend-code > div.form-group.has-feedback > input')
        next_btn = browser.find_element_by_css_selector('body > div > div > div > section > div > button')

        recommend_code_input.send_keys('00001111')
        next_btn.click()

        time.sleep(4)

        assert 'syg-has-address'

        province_select = Select(browser.find_element_by_css_selector('#province'))
        city_select = Select(browser.find_element_by_css_selector('#city'))
        district_select = Select(browser.find_element_by_css_selector('#district'))
        address_textarea = browser.find_element_by_css_selector('#addressForm > div.detail-address.form-group.form-inline.has-error > div > textarea')
        person_name_input = browser.find_element_by_css_selector('#addressForm > div.input-container > div:nth-child(1) > div > input')
        phone_input = browser.find_element_by_css_selector('#addressForm > div.input-container > div:nth-child(2) > div > input')
        default_checkbox = browser.find_element_by_css_selector('#addressForm > div.checkbox.form-group > label')
        confirm_btn = browser.find_element_by_css_selector('#submit_btn')

        province_select.select_by_index(10)
        time.sleep(1)
        city_select.select_by_value('109')
        time.sleep(0.5)
        district_select.select_by_index(1)

        address_textarea.send_keys('天府长城西路天西六百社区斗鱼小区二期10栋8单元22号')
        person_name_input.send_keys('LNC')
        phone_input.send_keys('13800001111')
        default_checkbox.click()
        confirm_btn.click()

        time.sleep(4)

        assert '商品详情' in browser.title


    def test_login_in_SYG(self):
        browser = InitDriver.set_up_locally()

        # 打开SYG页面
        browser.get('http://47.94.123.58:2334/product/SKII-0066')
        time.sleep(0.5)
        # assert 'href="/login"' in browser.page_source

        login_elem = browser.find_element_by_css_selector('body > div > header > div > div.user-option > a:nth-child(1) > span')
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