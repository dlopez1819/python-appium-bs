import pytest
from src.common.shared_workflow import SharedWorkflow
from src.helpers.appium_driver import Driver
import allure
from src.pages.headsup_page import HeadsUpPage
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.pages.menu_page import MenuPage
from src.pages.terms_of_use_page import TermsOfUsePage
from src.pages.disclaimer_page import DisclaimerPage
from src.pages.faqs_page import FaqsPage
from src.pages.user_guidelines_page import UserGuideLinesPage


class Account:
    BoHCredentials = [
        # BoHCredentials pre-prod user
        ['diego11.lopez@nttdata.com', 'Password1']
    ]

class TestBoHNormalMoreMenu(Driver):
    global flagLogin #userLogged

    def setUp(self):
        super().setUp()
        SharedWorkflow.verifySplash(self)

    def teardown_method(self):
        super().tearDown()

    @pytest.mark.regression
    @pytest.mark.functional
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_normal_more_menu_terms_of_use_BOH19_TC536(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC-536
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.oktaUserLoginSkip(self, test_email, test_pwd)
        else:
            UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        HeadsUpPage.verifyVehicleProfile(self)
        HeadsUpPage.checkTrailAndBadges(self, flagLogin=True)
        HomePage.assertIfHomePage(self)
        MenuPage.termsOfUse(self)
        TermsOfUsePage.verifyTermsOfUsePage(self)

    @pytest.mark.regression
    @pytest.mark.functional
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_normal_more_menu_disclaimers_BOH19_TC539(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC-539
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.oktaUserLoginSkip(self, test_email, test_pwd)
        else:
            UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        HeadsUpPage.verifyVehicleProfile(self)
        HomePage.assertIfHomePage(self)
        MenuPage.disclaimer(self)
        DisclaimerPage.verifyDisclaimer(self)

    @pytest.mark.regression
    @pytest.mark.functional
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_normal_more_menu_faqs_BOH19_TC541(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC-541
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.oktaUserLoginSkip(self, test_email, test_pwd)
        else:
            UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        HeadsUpPage.verifyVehicleProfile(self)
        HomePage.assertIfHomePage(self)
        MenuPage.faqs(self)
        FaqsPage.verifyFaqs(self)


