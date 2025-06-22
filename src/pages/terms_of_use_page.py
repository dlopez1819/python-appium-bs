from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver
from src.common.shared_workflow import SharedWorkflow

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

    def closeTermsOfUsePage(self):
        SharedWorkflow.closePage(self)
