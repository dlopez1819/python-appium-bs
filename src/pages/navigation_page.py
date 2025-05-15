import pytest
from appium.options.ios import XCUITestOptions
from src.common.shared_workflow import SharedWorkflow
from src.pages.alerts_page import AlertsPage
from src.screen_locators.android_screen_enums import *
from src.screen_locators.ios_screen_enums import *
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver
import src.screen_locators.ios_screen_enums
import src.screen_locators.android_screen_enums


class NavigationPage(Driver):
    global locators
    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def initBoHExploreNav(self):
        NavigationPage.__init__(self)
        pages =  {0: self.locators.NavigationScreen.exploreTrailsTitle, 1: self.locators.NavigationScreen.uploadPhotosTitle,
                    2: self.locators.NavigationScreen.earnPointBadgesTitle, 3: self.locators.NavigationScreen.learnEssentialsTitle}
        for index, element in pages.items():
            BoH.is_exist(self, element, expected=True)
            if self.apps == 'ios':
                BoH.swipe_by_coordinates(self, self.width - self.offset,  self.height  / 2, self.offset, self.height / 2, 500)
            else:
                BoH.swipe_by_coordinates(self, self.width - 100, self.height / 2, self.offset, self.height / 2,500)
        if self.apps == 'ios':
            btn_location = BoH.get_element_location(self, self.locators.NavigationScreen.pageIndicatorDots)
            BoH.tap_by_coordinates(self, btn_location['x'], btn_location['y'] - 50)
        else:
            BoH.click(self, self.locators.NavigationScreen.letsGoButton)
        if self.appiumserver == "browserstack":
            AlertsPage.allowLocationAlert(self)

    def checkTrailsAndBadgesNav(self):
       NavigationPage.__init__(self)
