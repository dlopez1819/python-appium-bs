from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class FaqsPage(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def verifyFaqs(self):
        FaqsPage.__init__(self)
        BoH.wait_until_appear(self, self.locators.FAQsScreen.faqsTitle, 5)
        BoH.is_exist(self, self.locators.FAQsScreen.faqsTitle, expected=True)
        BoH.is_exist(self, self.locators.FAQsScreen.contentBodyText, expected=True)
        if self.apps == 'ios':
            BoH.tap_by_coordinates(self, 25, 70)
        else:
            BoH.tap_by_coordinates(self, 85, 105)

    def closeFaqsPage(self):
        BoH.click(self, self.locators.DisclaimerScreen.closeButton)
