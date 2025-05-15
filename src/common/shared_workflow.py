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
            BrowserstackObjects.enter_BS_Username(self, test_email)
            """""""""
            if BoH.is_exist(self, self.locators.loginOktaScreen.loginTab_BS, True):
                BoH.click(self, self.locators.loginOktaScreen.loginTab_BS)
            BoH.send_keys(self, self.locators.loginOktaScreen.username_BS, test_email)
            """
        else:
            if BoH.is_exist(self, self.locators.loginOktaScreen.loginTab, True):
                BoH.click(self, self.locators.loginOktaScreen.loginTab)
            BoH.send_keys(self, self.locators.loginOktaScreen.username, test_email)
        if self.appiumserver == "browserstack":
            BrowserstackObjects.swipe_BS_Page(self)
     
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
            BrowserstackObjects.enter_BS_Password(self, test_pwd)
        else:
            BoH.send_keys(self, self.locators.loginOktaScreen.password, test_pwd)

        if BoH.is_exist(self, self.locators.loginOktaScreen.loginButton, False) is not True:
            if self.apps == 'ios':
                BoH.hideKeyboard(self, self.locators.loginOktaScreen.keyboardOn, 390, self.height / 2 - self.offset)
        BoH.swipe_by_coordinates(self, self.width, (self.height / 2 + self.offset), self.width,
                                 (self.height / 2 - self.offset), 100)
        # CLICK ON LOGIN BUTTON
        if self.appiumserver == "browserstack" and self.apps == 'android':
            BrowserstackObjects.tap_BS_LoginButton(self)
        else:
            BoH.click(self, self.locators.loginOktaScreen.loginButton)

    def loginAsGuess(self):
        # TO DO
        print("loginAsGuess")

    def home(self):
        BoH.is_exist(self, HomeScreen.featuredTopNavBar)
        BoH.is_exist(self, HomeScreen.imageFeaturedTrail)
        BoH.is_exist(self, HomeScreen.homeBottomNavBar)
        BoH.is_exist(self, HomeScreen.checkinTrailButton)
        BoH.is_exist(self, HomeScreen.featuredTrailRowContainer)
        BoH.is_exist(self, HomeScreen.featuredTrailWeatherContainer)

