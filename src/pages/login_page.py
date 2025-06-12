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
    global locators, flagOkta
    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def assertIfLoginPage(self):
        LoginPage.__init__(self)
        assert (BoH.is_exist(self, self.locators.LoginScreen.loginSignUpButton)) is True, "Login Page is not displayed"

    def isUserSignedUp(self):
        LoginPage.__init__(self)
        if BoH.is_exist(self, self.locators.LoginScreen.loginSignUpButton, expected=True):
            return False #user not logged
        else:
            return True #user logged
    
    def isNormalUserLoggedIn(self):
        LoginPage.__init__(self)
        if self.apps == 'ios':
            if BoH.is_exist(self, self.locators.HeadsUpScreen.headsUpText, expected=True, n=1) is True:
                    return False  # Not logged in
        if self.apps == 'android':
            BoH.wait_until_appear(self, self.locators.HeadsUpScreen.warningTitle, 5)
            if BoH.is_exist(self, self.locators.HeadsUpScreen.warningTitle, expected=True, n=1) is True:
                return False
        else:
            return True  # logged in

    def initLogin(self, flagOkta):
        LoginPage.__init__(self)
        if self.apps == 'android':
            BoH.wait_until_appear(self, self.locators.HeadsUpScreen.warningTitle, 5)
            if self.appiumserver == 'browserstack':
                BoH.tap_by_coordinates(self, 550, 1980)
            else:
                if BoH.is_exist(self, self.locators.HeadsUpScreen.ackContinueButton, expected=True):
                    BoH.click(self, self.locators.HeadsUpScreen.ackContinueButton)
        else:
            HeadsUpPage.verifyInitHeadsUp(self)
        if flagOkta == True:
            BoH.wait_until_appear(self, self.locators.NavigationScreen.exploreTrailsTitle, 5)
            if BoH.is_exist(self, self.locators.NavigationScreen.exploreTrailsTitle, expected=True, n=1) is True:
                NavigationPage.initBoHExploreNav(self)
        else:
            BoH.wait_until_appear(self, self.locators.NavigationScreen.skipButton, 5)
            BoH.click(self, self.locators.NavigationScreen.skipButton)
        if self.apps == 'ios':
            LoginPage.selectPreProEnv(self)
        #else:
            #AlertsPage.allowLocationAlert(self)
    
    def selectPreProEnv(self):
        LoginPage.__init__(self)
        AlertsPage.allowLocationAlert(self)
        BoH.is_exist(self, self.locators.LoginScreen.logoBoH, expected=True)
        if self.apps == 'ios':
            BoH.click(self, self.locators.LoginScreen.preprodButton)

    def oktaUserLogin(self, test_email, test_pwd):
        lagOkta = True
        LoginPage.__init__(self)
        LoginPage.initLogin(self, flagOkta)
        BoH.wait_until_appear(self, self.locators.LoginScreen.loginSignUpButton, 5)
        BoH.click(self, self.locators.LoginScreen.loginSignUpButton)
        SharedWorkflow.oktaLogin(self, test_email, test_pwd)

    def oktaUserLoginSkip(self, test_email, test_pwd):
        flagOkta = False
        LoginPage.__init__(self)
        LoginPage.initLogin(self, flagOkta)
        BoH.wait_until_appear(self, self.locators.LoginScreen.loginSignUpButton, 5)
        BoH.click(self, self.locators.LoginScreen.loginSignUpButton)
        SharedWorkflow.oktaLogin(self, test_email, test_pwd)

    def guestUserLogin(self):
        flagOkta = False
        LoginPage.__init__(self)
        LoginPage.initLogin(self, flagOkta)
        BoH.wait_until_appear(self, self.locators.LoginScreen.continueAsGuessButton, 5)
        BoH.click(self, self.locators.LoginScreen.continueAsGuessButton)
        SharedWorkflow.loginAsGuess(self)

    def onboardingLoginSkip(self, test_email, test_pwd):
        flagOkta = False
        LoginPage.__init__(self)
        LoginPage.initLogin(self, flagOkta)

    def onboardingLoginTutorial(self, test_email, test_pwd):
        flagOkta = True
        LoginPage.__init__(self)
        LoginPage.initLogin(self, flagOkta)

    def userSignUp(self, test_email, test_pwd):
        flagOkta = False
        LoginPage.__init__(self)
        LoginPage.initLogin(self, flagOkta)
        BoH.wait_until_appear(self, self.locators.LoginScreen.loginSignUpButton, 5)
        BoH.click(self, self.locators.LoginScreen.loginSignUpButton)
        LoginPage.authBOHSignInAlert(self)
        SharedWorkflow.oktaLogin(self, test_email, test_pwd)
