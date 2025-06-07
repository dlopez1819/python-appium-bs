from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class TrailDetailsPage(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def verifyTrailDetailsPage(self):
        TrailDetailsPage.__init__(self)
        BoH.wait_until_appear(self, self.locators.TrailsDetailsScreen.trailDetailsTitle, 5)
        assert (BoH.is_exist(self, self.locators.TrailsDetailsScreen.trailDetailsTitle)) is True, "Trail Details page is not displayed"
        if self.appiumserver == 'local':
            BoH.click(self, self.locators.TrailsDetailsScreen.iconBackArrow)
            BoH.wait_until_disappear(self, self.locators.TrailsDetailsScreen.iconBackArrow, 5)
        else:
            BoH.click(self, self.locators.BottomNavBarScreen.homeBottomBar)
  
