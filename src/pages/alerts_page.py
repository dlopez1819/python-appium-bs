import pytest
from src.screen_locators.android_screen_enums import *
from src.screen_locators.ios_screen_enums import *
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class AlertsPage(Driver):

    def allowSendNotificationAlert(self):
        if BoH.is_exist(self, AlertsScreen.bohSendNotificationAlert, expected=True):
            BoH.click(self, AlertsScreen.allowButton)

    def allowLocationAlert(self):
        if BoH.is_exist(self, AlertsScreen.locationAlert, expected=True):
            BoH.click(self, AlertsScreen.allowOnceButton)

    def authBOHSignInAlert(self):
        if BoH.is_exist(self, AlertsScreen.bohAuthAlert, expected=True):
            BoH.click(self, AlertsScreen.authContinueButton)
        BoH.wait_until_disappear(self, AlertsScreen.bohAuthAlert, 5)