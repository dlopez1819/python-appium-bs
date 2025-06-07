from src.helpers.app_objects import BoH
from src.pages.leaderboard_page import LeaderBoardPage
from src.helpers.appium_driver import Driver
from src.pages.trail_details_page import TrailDetailsPage
from src.pages.checkin_page import CheckInPage


class HomePage(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def assertIfHomePage(self):
        HomePage.__init__(self)
        assert (BoH.is_exist(self, self.locators.HomeScreen.homeTitle)) is True, "Login Page is not displayed"

    def homePage(self):
        HomePage.__init__(self)
        BoH.click(self, self.locators.BottomNavBarScreen.homeBottomBar)
        BoH.click(self, self.locators.HomeScreen.featuredTopNavBar)
        HomePage.verifyHomePage(self)

    def verifyHomePage(self):
        HomePage.__init__(self)
        BoH.wait_until_appear(self, self.locators.HomeScreen.homeTitle, 5)
        BoH.is_exist(self, self.locators.HomeScreen.featuredTopNavBar, expected=True)
        #BoH.is_exist(self, self.locators.HomeScreen.imageFeaturedTrail, expected=True)
        BoH.is_exist(self, self.locators.HomeScreen.iconCheckIn, expected=True)
        BoH.is_exist(self, self.locators.HomeScreen.iconTrailDetails, expected=True)
        BoH.is_exist(self, self.locators.HomeScreen.trailDifficultyText, expected=True)
        BoH.is_exist(self, self.locators.HomeScreen.currentConditionsText, expected=True)
        BoH.is_exist(self, self.locators.HomeScreen.trailForcastText, expected=True)

    def homeAnnouncement(self):
        HomePage.__init__(self)
        if self.appiumserver == 'browserstack' and self.apps == 'ios':
            BoH.wait_until_appear(self, self.locators.HomeScreen.homeBSButton, timeout=5)
            BoH.tap_by_coordinates(self, 395, 80)
        else:
            BoH.wait_until_appear(self, self.locators.HomeScreen.homeButton, timeout=5)
            BoH.click(self, self.locators.HomeScreen.homeButton)

    def homeFeaturedTab(self):
        if BoH.is_exist(self, self.locators.HomeScreen.featuredTopNavBar, expected=True):
            BoH.click(self, self.locators.HomeScreen.featuredTopNavBar)

    def homeCheckIn(self):
        HomePage.__init__(self)
        BoH.wait_until_appear(self, self.locators.HomeScreen.iconCheckIn, 5)
        if BoH.is_exist(self, self.locators.HomeScreen.iconCheckIn, expected=True):
            BoH.click(self, self.locators.HomeScreen.iconCheckIn)
            BoH.wait_until_disappear(self, self.locators.HomeScreen.iconCheckIn, 3)
            CheckInPage.locationServices(self)
        BoH.wait_until_appear(self, self.locators.HomeScreen.homeTitle, 5)

    def homeTrailDetails(self):
        HomePage.__init__(self)
        BoH.wait_until_appear(self, self.locators.HomeScreen.iconTrailDetails, 5)
        if BoH.is_exist(self, self.locators.HomeScreen.iconTrailDetails, expected=True):
            BoH.click(self, self.locators.HomeScreen.iconTrailDetails)
            BoH.wait_until_disappear(self, self.locators.HomeScreen.iconTrailDetails, 3)
        #if self.appiumserver == 'local':
            TrailDetailsPage.verifyTrailDetailsPage(self)

    def homeViewLeaderboard(self):
        HomePage.__init__(self)
        BoH.wait_until_appear(self, self.locators.HomeScreen.trailLeaderboardSection, 5)
        if BoH.is_exist(self, self.locators.HomeScreen.viewLeaderboard, expected=True):
            BoH.click(self, self.locators.HomeScreen.viewLeaderboard)
            BoH.wait_until_disappear(self, self.locators.HomeScreen.viewLeaderboard, 3)
            LeaderBoardPage.verifyLeaderboardPage(self)
          
