from src.common.shared_workflow import SharedWorkflow
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class SuggestATrailPage(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def verifySuggestATrail(self):
        SuggestATrailPage.__init__(self)
        BoH.wait_until_appear(self, self.locators.SuggestATrailScreen.suggestATrailTitle, 5)
        BoH.is_exist(self, self.locators.SuggestATrailScreen.suggestATrailTitle, expected=True)

    def closeSuggestATrailPage(self):
        SharedWorkflow.closePage(self)
