import time
import pytest
from src.common.shared_workflow import SharedWorkflow
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver


class UserGuideLinesPage(Driver):
    def __init__(self):
        self.locators = BoH.get_src_screen_enums(self)

    def verifyUserContentGuideLines(self, flagLogin):
        UserGuideLinesPage.__init__(self)
        BoH.wait_until_appear(self, self.locators.HeadsUpScreen.headsUpUserContentTitle, 5)
        BoH.is_exist(self, self.locators.HeadsUpScreen.headsUpUserContentText, expected=True)
        BoH.is_exist(self, self.locators.HeadsUpScreen.headsUpGuidelines1, expected=True)
        BoH.is_exist(self, self.locators.HeadsUpScreen.headsUpGuidelines2, expected=True)
        BoH.is_exist(self, self.locators.UserGuideLinesScreen.logoutButton, expected=True)
        BoH.is_exist(self, self.locators.UserGuideLinesScreen.privacyPolicyButton, expected=True)
        BoH.is_exist(self, self.locators.UserGuideLinesScreen.termsOfUseButton, expected=True)
        if flagLogin == True:
            UserGuideLinesPage.acceptUserGuideLines(self)

    def acceptUserGuideLines(self):
        if BoH.is_exist(self, self.locators.UserGuideLinesScreen.acceptButton, expected=True):
            BoH.click(self, self.locators.UserGuideLinesScreen.acceptButton)

    def verifyTermsOfUse(self):
        if BoH.is_exist(self, self.locators.UserGuideLinesScreen.termsOfUseButton, expected=True):
            BoH.click(self, self.locators.UserGuideLinesScreen.termsOfUseButton)
        BoH.is_exist(self, self.locators.UserGuideLinesScreen.termsOfUseTitle, expected=True)
        BoH.click(self, self.locators.UserGuideLinesScreen.closeTermsOfUse)

    def verifyPrivacyPolicyPage(self):
        if BoH.is_exist(self, self.locators.UserGuideLinesScreen.privacyPolicyButton, expected=True):
            BoH.click(self, self.locators.UserGuideLinesScreen.privacyPolicyButton)
        BoH.is_exist(self, self.locators.UserGuideLinesScreen.privacyPolicyTitle, expected=True)
        #BoH.click(self, self.locators.UserGuideLinesScreen.closePrivacyPolicy)
        if self.apps == 'android':
            BoH.back(self)
        else:
            BoH.tap_by_coordinates(self, 31, 70)

    def logout(self):
        if BoH.is_exist(self, self.locators.UserGuideLinesScreen.logoutButton, expected=True):
            BoH.click(self, self.locators.UserGuideLinesScreen.logoutButton)
