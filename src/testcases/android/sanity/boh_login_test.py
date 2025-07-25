import pytest
import allure
from src.common.shared_workflow import SharedWorkflow
from src.helpers.appium_driver import Driver
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.pages.headsup_page import HeadsUpPage
from src.pages.menu_page import MenuPage
from src.pages.user_guidelines_page import UserGuideLinesPage


class Account:
    BoHCredentials = [
        # BoHCredentials pre-prod user
        ['diego11.lopez@nttdata.com', 'Password1']
    ]
    BoHEnvironments = ('dev', 'test', 'preprod', 'prod')

class TestBoHLogin(Driver):
    global flagLogin  # userLogged
    def setUp(self):
       super().setUp()
       SharedWorkflow.verifySplash(self)

    def teardown_method(self):
        super().tearDown()

    #@pytest.mark.regression
    @pytest.mark.sanity
    @allure.description("BoH Okta Login Test [BOH19-TC-666, BOH19-TC-574, BOH19-TC-2572, BOH19-TC-2569]")
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    # TEST CASES: BOH19-TC-666, BOH19-TC-574, BOH19-TC-2572, BOH19-TC-2569
    def test_okta_login_BOH19_TC666(self, test_email, test_pwd):
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.oktaUserLogin(self, test_email, test_pwd)
        else:
            UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin = True)
        HeadsUpPage.verifyVehicleProfile(self)
        MenuPage.logout(self)
        LoginPage.assertIfLoginPage(self)

    @pytest.mark.regression
    @pytest.mark.skip
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_login_as_guest_BOH19_TC664(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC-664
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.guestUserLogin(self)
        else:
            HomePage.verifyHomePage(self)
        UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin = True)
        MenuPage.guestLogOut(self)
        LoginPage.assertIfLoginPage(self)

    #@pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    # TEST CASES:  BOH19-TC-2572
    def test_logout_email_BOH19_TC2572(self, test_email, test_pwd):
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.oktaUserLogin(self, test_email, test_pwd)
        else:
            UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        HeadsUpPage.verifyVehicleProfile(self)
        MenuPage.logout(self)
        LoginPage.assertIfLoginPage(self)

