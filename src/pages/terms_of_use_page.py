from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class TermsOfUsePage(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def verifyTermsOfUsePage(self):
        TermsOfUsePage.__init__(self)
        BoH.wait_until_appear(self, self.locators.TermsOfUseScreen.termOfUseTitle, 5)
        BoH.is_exist(self, self.locators.TermsOfUseScreen.termOfUseTitle, expected=True)
        BoH.is_exist(self, self.locators.TermsOfUseScreen.contentBodyText, expected=True)
        TermsOfUsePage.closeTermsOfUsePage(self)

    def closeTermsOfUsePage(self):
        BoH.click(self, self.locators.TermsOfUseScreen.closeButton)
