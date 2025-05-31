from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver
from src.pages.trail_details_page import TrailDetailsPage

class TrailsSortByPage(Driver):

    def __init__(self):
        self.locators = BoH.get_src_screen_enums(self)

    def sortByPage(self):
        TrailsSortByPage.__init__(self)
        BoH.click(self, self.locators.TrailsMapScreen.iconSortBy)
        TrailsSortByPage.verifySortByPage(self)
        TrailsSortByPage.closeSortByPage(self)

    def verifySortByPage(self):
        TrailsSortByPage.__init__(self)
        BoH.wait_until_appear(self, self.locators.TrailsSortByScreen.sorByTitle, 5)
        BoH.is_exist(self, self.locators.TrailsSortByScreen.byAlphabetical, expected=True)
        BoH.is_exist(self, self.locators.TrailsSortByScreen.byDifficulty, expected=True)
        BoH.is_exist(self, self.locators.TrailsSortByScreen.byMostPopular, expected=True)
        BoH.is_exist(self, self.locators.TrailsSortByScreen.byAverageUserRating, expected=True)
        BoH.is_exist(self, self.locators.TrailsSortByScreen.byResetResults, expected=True)

    def closeSortByPage(self):
        BoH.click(self, self.locators.TrailsSortByScreen.closeButton)

