from src.common.shared_workflow import SharedWorkflow
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver
from src.pages.trail_details_page import TrailDetailsPage
from src.pages.trails_sort_by_page import TrailsSortByPage


class TrailsMapPage(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def trailsMapPage(self):
        TrailsMapPage.__init__(self)
        BoH.click(self, self.locators.TrailsMapScreen.mapsBottomNavBar)
        BoH.click(self, self.locators.TrailsMapScreen.trailsTopNavBar)
        TrailsMapPage.verifyTrailsMapPage(self)

    def verifyTrailsMapPage(self):
        TrailsMapPage.__init__(self)
        BoH.wait_until_appear(self, self.locators.TrailsMapScreen.trailMapTitle, 5)
        BoH.is_exist(self, self.locators.TrailsMapScreen.trailsTopNavBar, expected=True)
        BoH.is_exist(self, self.locators.TrailsMapScreen.searchTextField, expected=True)
        BoH.is_exist(self, self.locators.TrailsMapScreen.iconSort, expected=True)
        BoH.is_exist(self, self.locators.TrailsMapScreen.trailsList, expected=True)

    def trailsMapSortBy(self):
        TrailsSortByPage.sortByPage(self)

    def verifyTrailsAndMap(self):
        TrailsMapPage.__init__(self)
        lccationXY = BoH.element(self, self.locators.TrailsMapScreen.searchTextField).location
        #first_xPoint = ref_drawing_point['x'] + xOffset
        SharedWorkflow.scrollDown(self, self.width - 100, (self.height / 2 + self.offset), self.width - 100, self.offset)

