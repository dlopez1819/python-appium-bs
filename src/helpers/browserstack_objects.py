from selenium.webdriver.support.wait import WebDriverWait
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver


class BrowserstackObjects(Driver):

    def __init__(self):
        self.locators = BoH.get_src_screen_enums(self)

    def enter_BS_Username(self, test_email):
        BrowserstackObjects.__init__(self)
        if self.apps == 'android':
            if BoH.is_exist(self, self.locators.loginOktaScreen.loginTab_BS, True):
                BoH.click(self, self.locators.loginOktaScreen.loginTab_BS)
            BoH.send_keys(self, self.locators.loginOktaScreen.username_BS, test_email)
        else:
            if BoH.is_exist(self, self.locators.loginOktaScreen.loginTab, True):
                BoH.click(self, self.locators.loginOktaScreen.loginTab)
            BoH.send_keys(self, self.locators.loginOktaScreen.username, test_email)

    def enter_BS_Password(self, test_pwd):
        BrowserstackObjects.__init__(self)
        if self.apps == 'android':
            BoH.send_keys(self, self.locators.loginOktaScreen.password_BS, test_pwd)
        else:
            BoH.send_keys(self, self.locators.loginOktaScreen.password, test_pwd)

    def tap_BS_LoginButton(self):
        BrowserstackObjects.__init__(self)
        if self.apps == 'android':
            BoH.click(self, self.locators.loginOktaScreen.loginButton_BS)
        else:
            BoH.click(self, self.locators.loginOktaScreen.loginButton)

    def swipe_BS_Page(self):
        BrowserstackObjects.__init__(self)
        if self.apps == 'ios':
            BoH.click(self, self.locators.loginOktaScreen.keyboardDone)
            self.driver.execute_script('mobile: scroll', {'direction': 'down'})
