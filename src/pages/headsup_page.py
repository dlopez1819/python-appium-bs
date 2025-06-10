import time
import pytest
from src.common.shared_workflow import SharedWorkflow
from src.helpers.app_objects import BoH
import src.screen_locators.ios_screen_enums
import src.screen_locators.android_screen_enums
from enum import Enum
from src.helpers.appium_driver import Driver
from src.pages.navigation_page import NavigationPage


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
            BoH.wait_until_appear(self, self.locators.HeadsUpScreen.headsUpText, 5)
            if BoH.is_exist(self, self.locators.HeadsUpScreen.headsUpText, expected=True):
                BoH.click(self, self.locators.HeadsUpScreen.continueButton)
        if BoH.is_exist(self, self.locators.HeadsUpScreen.warningTitle, expected=True):
            BoH.click(self, self.locators.HeadsUpScreen.ackContinueButton)

    def verifyVehicleProfile(self):
        HeadsUpPage.__init__(self)
        BoH.wait_until_appear(self, self.locators.VehicleProfileScreen.updateProfileButton, 5)
        if BoH.is_exist(self, self.locators.VehicleProfileScreen.updateProfileButton, expected=True):
            BoH.click(self, self.locators.VehicleProfileScreen.dismissProfileButton)

    def checkTrailAndBadges(self, flagLogin):
        HeadsUpPage.__init__(self)
        BoH.wait_until_appear(self, self.locators.NavigationScreen.trailAndBadgesTitle, 5)
        if flagLogin == True:
            if self.apps == 'ios':
                if BoH.is_exist(self, self.locators.NavigationScreen.trailAndBadgesTitle, expected=True):
                    NavigationPage.checkTrailsAndBadgesNav(self)
        else:
            if BoH.is_exist(self, self.locators.NavigationScreen.trailAndBadgesTitle, expected=True):
                BoH.click(self, self.locators.NavigationScreen.closePage)



