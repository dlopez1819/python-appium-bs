import pytest
import allure
from src.common.shared_workflow import SharedWorkflow
from src.helpers.appium_driver import Driver
from src.pages.login_page import LoginPage
from src.pages.headsup_page import HeadsUpPage
from src.pages.user_guidelines_page import UserGuideLinesPage


class Account:
    BoHCredentials = [
        # BoHCredentials pre-prod user
        ['diego11.lopez@nttdata.com', 'Password1']
    ]
    BoHEnvironments = ('dev', 'test', 'preprod', 'prod')

class TestBoHOnBoarding(Driver):
    global flagLogin  # userLogged
    def setUp(self):
       super().setUp()
       SharedWorkflow.verifySplash(self)

    def teardown_method(self):
        super().tearDown()

    @pytest.mark.regression
    @pytest.mark.functional
    @pytest.mark.sanity
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    # TEST CASES: BOH19-TC-2568. App On-Boarding (Tutorial)
    def test_boh_onboarding_tutorial_BOH19_TC2568(self, test_email, test_pwd):
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.onboardingLoginTutorial(self, test_email, test_pwd)
        else:
            UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        LoginPage.assertIfLoginPage(self)

    @pytest.mark.regression
    @pytest.mark.functional
    @pytest.mark.sanity
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    # TEST CASES: BOH19-TC-575. App On-Boarding - Skip
    def test_boh_onboarding_skip_BOH19_TC575(self, test_email, test_pwd):
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.onboardingLoginSkip(self, test_email, test_pwd)
        else:
            UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        LoginPage.assertIfLoginPage(self)

    @pytest.mark.regression
    @pytest.mark.functional
    @pytest.mark.sanity
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    # TEST CASES: BOH19-TC-574. app On-Boarding
    def test_boh_app_onboarding_BOH19_TC574(self, test_email, test_pwd):
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.onboardingLoginTutorial(self, test_email, test_pwd)
        else:
            UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        LoginPage.assertIfLoginPage(self)

    #@pytest.mark.regression
    @pytest.mark.sanity
    @allure.description("BoH onboarding email Login Test [BOH19-TC-2569]")
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    # TEST CASES: BOH19-TC-2569
    def test_boh_onboarding_email_login_BOH19_TC2569(self, test_email, test_pwd):
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.oktaUserLogin(self, test_email, test_pwd)
        else:
            UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=False)
        #HeadsUpPage.verifyVehicleProfile(self)

