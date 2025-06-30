import time
from src.helpers.appium_driver import Driver
from src.helpers.app_objects import BoH
from src.helpers.browserstack_objects import BrowserstackObjects
from src.pages.alerts_page import AlertsPage
from src.screen_locators.android_screen_enums import *
from src.screen_locators.ios_screen_enums import *
import src.screen_locators.ios_screen_enums
import src.screen_locators.android_screen_enums
from enum import Enum
import re


class SharedWorkflow(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def verifySplash(self):
        SharedWorkflow.__init__(self)
        BoH.is_exist(self, self.locators.SplashScreen.splashLogo, expected=True)
        if self.apps == 'android':
            AlertsPage.allowSendNotificationAlert(self)

    def oktaLogin(self, test_email, test_pwd):
        SharedWorkflow.__init__(self)
        env = 'pre-prod'
        if self.apps == 'ios':
            AlertsPage.authBOHSignInAlert(self)
        BoH.wait_until_appear(self, self.locators.loginOktaScreen.urlField, 10)
        if self.apps == 'ios':
            url = BoH.get_attribute(self, self.locators.loginOktaScreen.urlField, 'value')
            BoH.hideKeyboard(self, self.locators.loginOktaScreen.keyboardOn, 390, self.height / 2 - self.offset)
        else:
            url = BoH.get_attribute(self, self.locators.loginOktaScreen.urlField, 'text')
        #if env in url:  # verify Pre-Prod URL connection
        print(f'Test run on {url} environment')
        # SELECT & ENTER USERNAME
        if (self.appiumserver == "browserstack") and (self.apps == 'android'):
            BrowserstackObjects.enter_bs_username(self, test_email)
        else:
            if BoH.is_exist(self, self.locators.loginOktaScreen.loginTab, True):
                BoH.click(self, self.locators.loginOktaScreen.loginTab)
            BoH.wait_until_appear(self, self.locators.loginOktaScreen.username, 3)
            BoH.send_keys(self, self.locators.loginOktaScreen.username, test_email)
        if self.appiumserver == "browserstack":
            BrowserstackObjects.swipe_bs_page(self)
        else:
            if self.apps == 'ios':
                BoH.hideKeyboard(self, self.locators.loginOktaScreen.keyboardOn, 390, self.height / 2 - self.offset)
            BoH.swipe_by_coordinates(self, self.width, (self.height / 2 + self.offset), self.width,
                                     (self.height / 2 - self.offset), 100)
        if BoH.is_exist(self, self.locators.loginOktaScreen.loginButton, False) is not True:
            if self.apps == 'ios':
                BoH.hideKeyboard(self, self.locators.loginOktaScreen.keyboardOn, 390, self.height / 2 - self.offset)
        # SELECT & ENTER PASSWORD
        if self.appiumserver == "browserstack" and self.apps == 'android':
            BrowserstackObjects.enter_bs_password(self, test_pwd)
            if BoH.get_attribute(self, self.locators.loginOktaScreen.username_BS, 'text') is None:
                BrowserstackObjects.tap_bs_close_button(self)
                BoH.click(self, self.locators.LoginScreen.loginSignUpButton)
                BrowserstackObjects.enter_bs_username(self, test_email)
                BrowserstackObjects.swipe_bs_page(self)
                BrowserstackObjects.enter_bs_password(self, test_pwd)
        else:
            BoH.wait_until_appear(self, self.locators.loginOktaScreen.password, 5)
            BoH.send_keys(self, self.locators.loginOktaScreen.password, test_pwd)

        if BoH.is_exist(self, self.locators.loginOktaScreen.loginButton, False) is not True:
            if self.apps == 'ios':
                BoH.hideKeyboard(self, self.locators.loginOktaScreen.keyboardOn, 390, self.height / 2 - self.offset)
        BoH.swipe_by_coordinates(self, self.width, (self.height / 2 + self.offset), self.width,
                                 (self.height / 2 - self.offset), 100)
        # CLICK ON LOGIN BUTTON
        if self.appiumserver == "browserstack" and self.apps == 'android':
            BrowserstackObjects.tap_bs_login_button(self)
            BoH.wait_until_disappear(self, self.locators.loginOktaScreen.loginButton_BS, 5)
        else:
            BoH.click(self, self.locators.loginOktaScreen.loginButton)
            BoH.wait_until_disappear(self, self.locators.loginOktaScreen.loginButton, 5)

    def loginAsGuess(self):
        SharedWorkflow.__init__(self)
        BoH.wait_until_appear(self, self.locators.loginAsGuest.dontHaveProfileTitle, 2)
        if BoH.is_exist(self, self.locators.loginAsGuest.continueAsGuestButton, expected=True):
            BoH.click(self, self.locators.loginAsGuest.continueAsGuestButton)


    def scrollDown(self, startX, startY, endX, endY):
        SharedWorkflow.__init__(self)
        if self.appiumserver == 'local':
            if self.apps == 'ios':
                BoH.swipe_by_coordinates(self, startX, startY, endX, endY, 50)
            else:
                BoH.swipe_by_coordinates(self, startX, startY, endX, endY,500)
        else:
            if self.apps == 'ios':
                BrowserstackObjects.scroll_bs_down(self)
            else:
                BoH.swipe_by_coordinates(self, startX, startY, endX, endY, 1000)

    def closePage(self):
        if self.apps == 'ios':
            # FaqsPage.closeFaqsPage(self)
            BoH.tap_by_coordinates(self, 25, 70)
        else:
            BoH.tap_by_coordinates(self, 85, 105)

