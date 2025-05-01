import pytest
from src.common.shared_workflow import SharedWorkflow
from src.helpers.appium_driver import Driver
from src.pages.headsup_page import HeadsUpPage
from src.pages.navigation_page import NavigationPage


class TestBoHLogin(Driver):

    def setUp(self):
       super().setUp()
       SharedWorkflow.verifySplash(self)
       HeadsUpPage.verifyInitHeadsUp(self)

    def teardown_method(self):
        super().tearDown()


    #@pytest.mark.timeout(400)
    @pytest.mark.functional
    def test_boh_navigation(self):
        NavigationPage.pageIndicatorNav(self)
        # SharedWorkflow.logout(self)