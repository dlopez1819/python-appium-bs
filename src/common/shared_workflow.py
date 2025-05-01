import time
from src.helpers.appium_driver import Driver
from src.helpers.app_objects import BoH
from src.pages.alerts_page import AlertsPage
from src.screen_locators.android_screen_enums import *
from src.screen_locators.ios_screen_enums import *
from enum import Enum
import re

class SharedWorkflow(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30

    def verifySplash(self):
        BoH.is_exist(self, SplashScreen.splashLogo, expected=True)
        if self.appiumserver == "browserstack":
            if BoH.is_exist(self, AlertsScreen.bohSendNotificationAlert) is True:
                BoH.click(self, AlertsScreen.allowButton)

    def oktaLogin(self, test_email, test_pwd):
        SharedWorkflow.__init__(self)
        env = 'pre-prod'
        AlertsPage.authBOHSignInAlert(self)
        BoH.wait_until_appear(self, loginOktaScreen.urlField, 5)
        url = BoH.get_attribute(self, loginOktaScreen.urlField, 'value')
        BoH.hideKeyboard(self, loginOktaScreen.keyboardOn, 390, self.height / 2 - self.offset)
        if env in url:  # verify Pre-Prod URL connection
            if BoH.is_exist(self, loginOktaScreen.loginTab, True):
                BoH.click(self, loginOktaScreen.loginTab)
            BoH.send_keys(self, loginOktaScreen.username, test_email)
            if  BoH.is_exist(self, loginOktaScreen.loginButton, False) is not True:
                BoH.hideKeyboard(self, loginOktaScreen.keyboardOn, 390, self.height / 2 - self.offset)
            BoH.swipe_by_coordinates(self, self.width,  (self.height  / 2 + self.offset), self.width, (self.height / 2 - self.offset), 100)
            if BoH.is_exist(self, loginOktaScreen.loginButton, False) is not True:
                BoH.hideKeyboard(self, loginOktaScreen.keyboardOn, 390, self.height / 2 - self.offset)
            BoH.send_keys(self, loginOktaScreen.password, test_pwd)
            if BoH.is_exist(self, loginOktaScreen.loginButton, False) is not True:
                BoH.hideKeyboard(self, loginOktaScreen.keyboardOn, 390, self.height / 2 - self.offset)
            BoH.click(self, loginOktaScreen.loginButton)


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

