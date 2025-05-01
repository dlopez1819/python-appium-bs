import pytest
from src.common.shared_workflow import SharedWorkflow
from src.helpers.appium_driver import Driver
from src.pages.navigation_page import NavigationPage
from src.pages.headsup_page import HeadsUpPage
import allure


class TestBoHSmoke(Driver):

    def setUp(self):
       super().setUp()
       # VALIDATE SPLASH & WARNING PAGES
       #allure("Launching app")
       SharedWorkflow.verifySplash(self)
       HeadsUpPage.verifyInitHeadsUp(self)

    def teardown_method(self):
        super().tearDown()

    @pytest.mark.smoke
    def test_boh_navigation(self):
        NavigationPage.pageIndicatorNav(self)
        #SharedWorkflow.logout(self)