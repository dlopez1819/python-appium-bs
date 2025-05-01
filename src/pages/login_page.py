import pytest
from appium.options.ios import XCUITestOptions
from src.common.shared_workflow import SharedWorkflow
from src.pages.alerts_page import AlertsPage
from src.pages.headsup_page import HeadsUpPage
from src.pages.navigation_page import NavigationPage
from src.screen_locators.android_screen_enums import *
from src.screen_locators.ios_screen_enums import *
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class LoginPage(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30

    def isNormalUserLoggedIn(self):
        if BoH.is_exist(self, HeadsUpScreen.headsUpText, expected=True, n=1) is True:
            return False  # Not logged in
        else:
            return True  # logged in

    def selectPreProEnv(self):
        AlertsPage.allowLocationAlert(self)
        BoH.is_exist(self, LoginScreen.logoBoH, expected=True)
        BoH.click(self, LoginScreen.preprodButton)
        BoH.click(self, LoginScreen.loginSignUpButton)


    def oktaUserLogin(self, test_email, test_pwd):
        if BoH.is_exist(self, HeadsUpScreen.headsUpText, expected=True, n=1) is True:
            HeadsUpPage.verifyInitHeadsUp(self)
        if BoH.is_exist(self, NavigationScreen.exploreTrailsTitle, expected=True, n=1) is True:
            NavigationPage.initBoHExploreNav(self)
        LoginPage.selectPreProEnv(self)
        SharedWorkflow.oktaLogin(self, test_email, test_pwd)

    def loginAsGuest(self):
        # TO DO
        print('login')