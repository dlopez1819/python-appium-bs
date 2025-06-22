from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver
from src.common.shared_workflow import SharedWorkflow

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

    def closeFaqsPage(self):
        SharedWorkflow.closePage(self)
