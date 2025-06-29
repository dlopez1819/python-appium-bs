import pytest
from src.common.base_page_app_manager import BaseClassAppManager
from src.common.shared_workflow import SharedWorkflow
from src.helpers.appium_driver import Driver
from src.pages.home_page import HomePage
from src.pages.trail_map_events_page import TrailMapEventsPage
from src.pages.trails_map_page import TrailMapPage

class Account:
    BoHCredentials = [
        # BoHCredentials pre-prod user
        ['diego11.lopez@nttdata.com', 'Password1']
    ]

class TestBoHTrailAndMap(Driver):
    global flagLogin #userLogged

    def setUp(self):
        super().setUp()
        SharedWorkflow.verifySplash(self)

    def teardown_method(self):
        super().tearDown()

    @pytest.mark.regression
    @pytest.mark.functional2
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_tray_list_results_BOH19_TC643(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC643
        BaseClassAppManager.userLoginSkipHeadsUp(self,test_email, test_pwd)
        HomePage.assertIfHomePage(self)
        BaseClassAppManager.tapBottomNavBar(self, 2)
        TrailMapPage.getTrayListResults(self)

    @pytest.mark.regression
    @pytest.mark.functional2
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_collapsed_tray_results_BOH19_TC2586(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC2586
        BaseClassAppManager.userLoginSkipHeadsUp(self,test_email, test_pwd)
        HomePage.assertIfHomePage(self)
        BaseClassAppManager.tapBottomNavBar(self, 2)
        TrailMapPage.getTrayListResults(self)
        TrailMapPage.cardDisplay(self)
        TrailMapPage.collapseTrayResults(self)

    @pytest.mark.regression
    @pytest.mark.functional2
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_card_display_BOH19_TC2587(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC2587
        BaseClassAppManager.userLoginSkipHeadsUp(self,test_email, test_pwd)
        HomePage.assertIfHomePage(self)
        BaseClassAppManager.tapBottomNavBar(self, 2)
        TrailMapPage.getTrayListResults(self)
        TrailMapPage.cardDisplay(self)

    @pytest.mark.regression
    @pytest.mark.functional2
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_tray_card_event_challenge_BOH19_TC2590(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC2590
        BaseClassAppManager.userLoginSkipHeadsUp(self, test_email, test_pwd)
        HomePage.assertIfHomePage(self)
        BaseClassAppManager.tapBottomNavBar(self, 2)
        TrailMapPage.verifyTrayCardEventChalenge(self)

    @pytest.mark.regression
    @pytest.mark.functional2
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_trail_details_BOH19_TC639(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC639
        BaseClassAppManager.userLoginSkipHeadsUp(self, test_email, test_pwd)
        HomePage.assertIfHomePage(self)
        BaseClassAppManager.tapBottomNavBar(self, 2)
        TrailMapPage.cardDisplay(self)
        TrailMapPage.trailCardListDetails(self)

    @pytest.mark.regression
    @pytest.mark.functional2
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_multiple_pin_map_result_map_BOH19_TC2600(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC2600
        BaseClassAppManager.userLoginSkipHeadsUp(self, test_email, test_pwd)
        HomePage.assertIfHomePage(self)
        BaseClassAppManager.tapBottomNavBar(self, 2)
        TrailMapPage.getMultiplePinMapResults(self)

    @pytest.mark.regression
    @pytest.mark.functional2
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_swipe_card_event_challenge_map_BOH19_TC2591(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC2591
        BaseClassAppManager.userLoginSkipHeadsUp(self, test_email, test_pwd)
        HomePage.assertIfHomePage(self)
        BaseClassAppManager.tapBottomNavBar(self, 2)
        TrailMapPage.verifySwipeCardEventChallengeMap(self)

    @pytest.mark.regression
    @pytest.mark.functional2
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_pin_map_card_details_BOH19_TC2601(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC2601
        BaseClassAppManager.userLoginSkipHeadsUp(self, test_email, test_pwd)
        HomePage.assertIfHomePage(self)
        BaseClassAppManager.tapBottomNavBar(self, 2)
        TrailMapPage.tapIndividualPinMap(self)
        TrailMapPage.horizontalCardPresent(self)
        TrailMapPage.pinMapCardDetails(self)

    @pytest.mark.regression
    @pytest.mark.functional2
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_search_trail_BOH19_TC641_and_BOH19_TC2585(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC641 & BOH19-TC2585
        search_trail = 'Twisted'
        BaseClassAppManager.userLoginSkipHeadsUp(self, test_email, test_pwd)
        HomePage.assertIfHomePage(self)
        BaseClassAppManager.tapBottomNavBar(self, 2)
        TrailMapPage.cardDisplay(self)
        TrailMapPage.searchForTrail(self, search_trail)
        TrailMapPage.getTrayListResults(self)

    @pytest.mark.regression
    @pytest.mark.functional2
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_all_trail_events_BOH19_TC651(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC651
        search_trail = 'Twisted'
        BaseClassAppManager.userLoginSkipHeadsUp(self, test_email, test_pwd)
        HomePage.assertIfHomePage(self)
        BaseClassAppManager.tapBottomNavBar(self, 5)
        BaseClassAppManager.tapLayoutTabsBar(self, 'LIST')
        TrailMapEventsPage.assertIfTrailMapEventsPage(self)
        TrailMapEventsPage.allTrailEventsPresent(self)

