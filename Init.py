from selenium import webdriver

class InitDriver():
    def setUp(self):
        ## 创建浏览器对象
        desired_cap = {'browser': 'chrome', 'build': 'First build', 'browserstack.debug': 'true', 'browserstack.local': 'true'}

        self.driver = webdriver.Remote(
            command_executor='http://deronlee1:Ayr2VfvqYzkirpAfYt8t@hub.browserstack.com:80/wd/hub',
            desired_capabilities=desired_cap)

        return self.driver

