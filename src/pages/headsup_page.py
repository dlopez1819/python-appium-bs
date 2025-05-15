import time
import pytest
from src.common.shared_workflow import SharedWorkflow
from src.helpers.app_objects import BoH
import src.screen_locators.ios_screen_enums
import src.screen_locators.android_screen_enums
from enum import Enum
from src.helpers.appium_driver import Driver
from appium.options.ios import XCUITestOptions


class HeadsUpPage(Driver):
    global locators
    def __init__(self):
        global src
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)
        pass

    def verifyInitHeadsUp(self):
        HeadsUpPage.__init__(self)
        if self.apps == 'ios':
            BoH.wait_until_appear(self, self.locators.HeadsUpScreen.headsUpTitle, 2)
            if BoH.is_exist(self, self.locators.HeadsUpScreen.headsUpText, expected=True):
                BoH.click(self, self.locators.HeadsUpScreen.continueButton)
        BoH.wait_until_appear(self, self.locators.HeadsUpScreen.warningTitle)
        if BoH.is_exist(self, self.locators.HeadsUpScreen.warningTitle, expected=True):
            BoH.click(self, self.locators.HeadsUpScreen.ackContinueButton)

    def verifyUserContentGuideLines(self):
        # validate User Content Guidelines Elements in Page
        HeadsUpPage.__init__(self)
        BoH.wait_until_appear(self, self.locators.HeadsUpScreen.headsUpUserContentTitle, 5)
        BoH.is_exist(self, self.locators.HeadsUpScreen.headsUpUserContentText, expected=True)
        BoH.is_exist(self, self.locators.HeadsUpScreen.headsUpGuidelines1, expected=True)
        BoH.is_exist(self, self.locators.HeadsUpScreen.headsUpGuidelines2, expected=True)
        BoH.is_exist(self, self.locators.HeadsUpScreen.logoutButton, expected=True)
        BoH.is_exist(self, self.locators.HeadsUpScreen.privacyPolicy, expected=True)
        BoH.is_exist(self, self.locators.HeadsUpScreen.termsOfUse, expected=True)
        if BoH.is_exist(self, self.locators.HeadsUpScreen.acceptButton, expected=True):
            BoH.click(self, self.locators.HeadsUpScreen.acceptButton)



