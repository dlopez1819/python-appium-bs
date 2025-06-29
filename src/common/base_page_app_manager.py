from src.common.shared_workflow import SharedWorkflow
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver
from src.pages.headsup_page import HeadsUpPage
from src.pages.login_page import LoginPage
from src.pages.user_guidelines_page import UserGuideLinesPage


class BaseClassAppManager(Driver):

    def __init__(self):
        self.locators = BoH.get_src_screen_enums(self)

    def userLoginSkipHeadsUp(self, test_email, test_pwd):
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.oktaUserLoginSkip(self, test_email, test_pwd)
        else:
            UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        HeadsUpPage.verifyVehicleProfile(self)

    def tapBottomNavBar(self, index):
        SharedWorkflow.__init__(self)
        BoH.click(self, self.locators.BottomNavBarScreen.BottomNavBar(self, index))

    def tapLayoutTabsBar(self, layout):
        SharedWorkflow.__init__(self)
        BoH.click(self, self.locators.layoutTabsBarScreen.layoutTabsBar(self, layout))

