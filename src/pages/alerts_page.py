import pytest
import src.screen_locators.ios_screen_enums
import src.screen_locators.android_screen_enums
from enum import Enum
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class AlertsPage(Driver):
    global locators
    def __init__(self):
        global src
        self.locators = BoH.get_src_screen_enums(self)

    def allowSendNotificationAlert(self):
        if BoH.is_exist(self, self.locators.AlertsScreen.bohSendNotificationAlert, expected=True):
            BoH.click(self, self.locators.AlertsScreen.allowButton)

    def allowLocationAlert(self):
        AlertsPage.__init__(self)
        if BoH.is_exist(self, self.locators.AlertsScreen.locationAlert, expected=True):
            BoH.click(self,self.locators.AlertsScreen.allowOnceButton)

    def authBOHSignInAlert(self):
        if BoH.is_exist(self, self.locators.AlertsScreen.bohAuthAlert, expected=True):
            BoH.click(self,self.locators. AlertsScreen.authContinueButton)
        BoH.wait_until_disappear(self, self.locators.AlertsScreen.bohAuthAlert, 5)

    def wantToLogOutAlert(self):
        AlertsPage.__init__(self)
        if BoH.is_exist(self, self.locators.AlertsScreen.yesLogOutButton, expected=True):
            BoH.click(self, self.locators.AlertsScreen.yesLogOutButton)
