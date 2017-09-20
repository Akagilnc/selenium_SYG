from selenium import webdriver


class InitDriver():
    @staticmethod
    def set_up_remotely():
        ## 创建浏览器对象
        desired_cap = {'browser': 'chrome', 'build': 'First build', 'browserstack.debug': 'true', 'browserstack.local': 'true'}

        driver = webdriver.Remote(
            command_executor='http://deronlee1:Ayr2VfvqYzkirpAfYt8t@hub.browserstack.com:80/wd/hub',
            desired_capabilities=desired_cap)

        return driver

    @staticmethod
    def set_up_locally_firefox():
        browser = webdriver.Firefox()
        browser.implicitly_wait(10)
        browser.set_window_size(1680, 1080)
        return browser

    @staticmethod
    def set_up_locally_chrome():
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.set_window_size(1680, 1080)
        return browser


