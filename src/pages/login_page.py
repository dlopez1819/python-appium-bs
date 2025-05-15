from operator import truediv
import pytest
from appium.options.ios import XCUITestOptions
from src.common.shared_workflow import SharedWorkflow
from src.pages.alerts_page import AlertsPage
from src.pages.headsup_page import HeadsUpPage
from src.pages.navigation_page import NavigationPage
import src.screen_locators.ios_screen_enums
import src.screen_locators.android_screen_enums
from enum import Enum
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class LoginPage(Driver):
    global locators
    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def isNormalUserLoggedIn(self):
        LoginPage.__init__(self)
        if self.apps == 'ios':
            if BoH.is_exist(self, self.locators.HeadsUpScreen.headsUpText, expected=True, n=1) is True:
                    return False  # Not logged in
        if self.apps == 'android':
            if BoH.is_exist(self, self.locators.HeadsUpScreen.warningTitle, expected=True, n=1) is True:
                return False
        else:
            return True  # logged in

    def selectPreProEnv(self):
        LoginPage.__init__(self)
        AlertsPage.allowLocationAlert(self)
        BoH.is_exist(self, self.locators.LoginScreen.logoBoH, expected=True)
        if self.apps == 'ios':
            BoH.click(self, self.locators.LoginScreen.preprodButton)
        BoH.click(self, self.locators.LoginScreen.loginSignUpButton)

    def oktaUserLogin(self, test_email, test_pwd):
        LoginPage.__init__(self)
        HeadsUpPage.verifyInitHeadsUp(self)
        if BoH.is_exist(self, self.locators.NavigationScreen.exploreTrailsTitle, expected=True, n=1) is True:
            NavigationPage.initBoHExploreNav(self)
        if self.apps == 'ios':
            LoginPage.selectPreProEnv(self)
        else:
            BoH.click(self, self.locators.LoginScreen.loginSignUpButton)
        SharedWorkflow.oktaLogin(self, test_email, test_pwd)

    def loginAsGuest(self):
        # TO DO
        print('login')
