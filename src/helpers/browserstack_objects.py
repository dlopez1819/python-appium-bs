from selenium.webdriver.support.wait import WebDriverWait
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver


class BrowserstackObjects(Driver):

    def __init__(self):
        self.locators = BoH.get_src_screen_enums(self)

    def enter_bs_username(self, test_email):
        BrowserstackObjects.__init__(self)
        if self.apps == 'android':
            if BoH.is_exist(self, self.locators.loginOktaScreen.loginTab_BS, True):
                BoH.click(self, self.locators.loginOktaScreen.loginTab_BS)
            BoH.send_keys(self, self.locators.loginOktaScreen.username_BS, test_email)
        else:
            if BoH.is_exist(self, self.locators.loginOktaScreen.loginTab, True):
                BoH.click(self, self.locators.loginOktaScreen.loginTab)
            BoH.send_keys(self, self.locators.loginOktaScreen.username, test_email)

    def enter_bs_password(self, test_pwd):
        BrowserstackObjects.__init__(self)
        if self.apps == 'android':
            BoH.send_keys(self, self.locators.loginOktaScreen.password_BS, test_pwd)
        else:
            BoH.send_keys(self, self.locators.loginOktaScreen.password, test_pwd)

    def tap_bs_login_button(self):
        BrowserstackObjects.__init__(self)
        if self.apps == 'android':
            BoH.click(self, self.locators.loginOktaScreen.loginButton_BS)
        else:
            BoH.click(self, self.locators.loginOktaScreen.loginButton)

    def tap_bs_close_button(self):
        BrowserstackObjects.__init__(self)
        if self.apps == 'android':
            BoH.click(self, self.locators.loginOktaScreen.closeTab_BS)

    def swipe_bs_page(self):
        BrowserstackObjects.__init__(self)
        if self.apps == 'ios':
            BoH.click(self, self.locators.loginOktaScreen.keyboardDone)
            self.driver.execute_script('mobile: scroll', {'direction': 'down'})

    def scroll_bs_down(self):
        BrowserstackObjects.__init__(self)
        if self.apps == 'ios':
            self.driver.execute_script('mobile: scroll', {'direction': 'down'})
        else:
            self.driver.execute_script("mobile:swipe", {"direction": "down"})

    def scroll_bs_up(self):
        if self.apps == 'ios':
            self.driver.execute_script('mobile: scroll', {'direction': 'up'})
        else:
            self.driver.execute_script("mobile:swipe", {"direction": "up"})
