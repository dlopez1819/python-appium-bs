import pytest
from appium.options.ios import XCUITestOptions
from src.common.shared_workflow import SharedWorkflow
from src.screen_locators.android_screen_enums import *
from src.screen_locators.ios_screen_enums import *
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class NavigationPage(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30

    def initBoHExploreNav(self):
        NavigationPage.__init__(self)
        pages =  {0: NavigationScreen.exploreTrailsTitle, 1: NavigationScreen.uploadPhotosTitle,
                    2: NavigationScreen.earnPointBadgesTitle, 3: NavigationScreen.learnEssentialsTitle}
        for index, element in pages.items():
            BoH.is_exist(self, element, expected=True)
            if self.apps == 'ios':
                BoH.swipe_by_coordinates(self, self.width - self.offset,  self.height  / 2, self.offset, self.height / 2, 100)
        btn_location = BoH.get_element_location(self, NavigationScreen.pageIndicatorDots)
        BoH.tap_by_coordinates(self, btn_location['x'], btn_location['y'] - 50)


    def checkTrailsAndBadgesNav(self):
       NavigationPage.__init__(self)
