import pytest
from src.common.shared_workflow import SharedWorkflow
from src.helpers.appium_driver import Driver
from src.pages.login_page import LoginPage
from src.pages.user_guidelines_page import UserGuideLinesPage


class Account:
    BoHCredentials = [
        # BoHCredentials pre-prod user
        ['diego11.lopez@nttdata.com', 'Password1']
    ]

class TestBoHOnBoarding(Driver):

    def setUp(self):
       super().setUp()
       SharedWorkflow.verifySplash(self)

    def teardown_method(self):
        super().tearDown()

    @pytest.mark.sanity
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    # TEST CASES: BOH19-TC-575. BOH19-TC-574
    def test_boh_onboarding_skip_BOH19_TC575(self, test_email, test_pwd):
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.onboardingLoginSkip(self, test_email, test_pwd)
        else:
            UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        LoginPage.assertIfLoginPage(self)
