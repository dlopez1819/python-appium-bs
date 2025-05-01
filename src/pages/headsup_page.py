import time
import pytest
from src.helpers.app_objects import BoH
from src.screen_locators.ios_screen_enums import *
from src.screen_locators.android_screen_enums import *
from src.helpers.appium_driver import Driver
from appium.options.ios import XCUITestOptions

class HeadsUpPage(Driver):

    def verifyInitHeadsUp(self):
        BoH.wait_until_appear(self, HeadsUpScreen.headsUpTitle, 2)
        if BoH.is_exist(self, HeadsUpScreen.headsUpText, expected=True):
            BoH.click(self, HeadsUpScreen.continueButton)
        BoH.wait_until_appear(self, HeadsUpScreen.warningTitle)
        if BoH.is_exist(self, HeadsUpScreen.warningTitle, expected=True):
            BoH.click(self, HeadsUpScreen.ackContinueButton)

    def verifyUserContentGuideLines(self):
        # validate User Content Guidelines Elements in Page
        BoH.wait_until_appear(self, HeadsUpScreen.headsUpUserContentTitle, 3)
        BoH.is_exist(self, HeadsUpScreen.headsUpUserContentText, expected=True)
        BoH.is_exist(self, HeadsUpScreen.headsUpGuidelines1, expected=True)
        BoH.is_exist(self, HeadsUpScreen.headsUpGuidelines2, expected=True)
        BoH.is_exist(self, HeadsUpScreen.logoutButton, expected=True)
        BoH.is_exist(self, HeadsUpScreen.privacyPolicy, expected=True)
        BoH.is_exist(self, HeadsUpScreen.termsOfUse, expected=True)
        if BoH.is_exist(self, HeadsUpScreen.acceptButton, expected=True):
            BoH.click(self, HeadsUpScreen.acceptButton)

