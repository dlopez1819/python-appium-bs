from src.common.shared_workflow import SharedWorkflow
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class OffRoading101Page(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def verifyOffRoading101(self):
        OffRoading101Page.__init__(self)
        BoH.wait_until_appear(self, self.locators.OffRoading101Screen.offRoadingTitle, 5)
        BoH.is_exist(self, self.locators.OffRoading101Screen.trailDiffRatingContainer, expected=True)
        BoH.is_exist(self, self.locators.OffRoading101Screen.safetyChecklistContainer, expected=True)
        BoH.is_exist(self, self.locators.OffRoading101Screen.briefHistoryContainer, expected=True)
        BoH.is_exist(self, self.locators.OffRoading101Screen.terrainElementsContainer, expected=True)
        BoH.is_exist(self, self.locators.OffRoading101Screen.trailRatedContainer, expected=True)
        BoH.is_exist(self, self.locators.OffRoading101Screen.offRoadsFaqsContainer, expected=True)

    def closeOffRoading101Page(self):
        SharedWorkflow.closePage(self)
