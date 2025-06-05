import pytest
from src.common.shared_workflow import SharedWorkflow
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver
import allure
from src.pages.headsup_page import HeadsUpPage
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.pages.user_guidelines_page import UserGuideLinesPage

class Account:
    BoHCredentials = [
        # BoHCredentials pre-prod user
        ['diego11.lopez@nttdata.com', 'Password1']
    ]

class TestBoHNormalFeaturedTrail(Driver):
    global flagLogin #userLogged

    def setUp(self):
        super().setUp()
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        SharedWorkflow.verifySplash(self)

    def teardown_method(self):
        super().tearDown()

    @pytest.mark.regression
    @pytest.mark.functional
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_guest_featured_trail_enhancement_BOH19_TC2562(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC-651, BOH19-TC-2522, BOH19-TC-2518, BOH21-TC-2577, BOH19_TC2562
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.oktaUserLoginSkip(self, test_email, test_pwd)
        else:
            UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        # verify Featured from HomePage
        UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        HeadsUpPage.verifyVehicleProfile(self)
        HeadsUpPage.checkTrailAndBadges(self, flagLogin= False)
        HomePage.homePage(self)
        HomePage.homeCheckIn(self)
        HomePage.homeTrailDetails(self)
        SharedWorkflow.scrollDown(self, self.width, (self.height / 2 + self.offset), self.width, (self.height / 2 - self.offset)) # scroll half page
        HomePage.homeViewLeaderboard(self)
        HomePage.homeFeaturedTab(self)
        #MenuPage.logout(self)
        #LoginPage.assertIfLoginPage(self)
