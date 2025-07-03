import pytest
from src.common.shared_workflow import SharedWorkflow
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver
import allure
from src.pages.login_page import LoginPage
from src.pages.user_guidelines_page import UserGuideLinesPage

class Account:
    BoHCredentials = [
        # BoHCredentials pre-prod user
        ['diego11.lopez@nttdata.com', 'Password1']
    ]

class TestBoHUserContent(Driver):
    global flagLogin #userLogged

    def setUp(self):
        super().setUp()
        SharedWorkflow.verifySplash(self)

    def teardown_method(self):
        super().tearDown()

    @pytest.mark.regression
    @pytest.mark.functional
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_user_content_guidelines_BOH19_TC2540(self, test_email, test_pwd):
        # TEST CASES: BOH19-TC-2540
        self.locators = BoH.get_src_screen_enums(self)
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.oktaUserLoginSkip(self, test_email, test_pwd)
        else:
            UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin=True)
        # verify UserGuideLinesPage
        BoH.wait_until_appear(self, self.locators.HeadsUpScreen.headsUpUserContentTitle, 5)
        if BoH.is_exist(self, self.locators.HeadsUpScreen.headsUpUserContentTitle, expected=True):
            UserGuideLinesPage.verifyUserContentGuideLines(self, flagLogin = False)
            UserGuideLinesPage.verifyTermsOfUse(self)
            UserGuideLinesPage.verifyPrivacyPolicyPage(self)
            UserGuideLinesPage.logout(self)
            LoginPage.assertIfLoginPage(self)


