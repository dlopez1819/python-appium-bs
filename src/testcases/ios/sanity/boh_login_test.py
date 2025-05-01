import pytest
from src.common.shared_workflow import SharedWorkflow
from src.helpers.appium_driver import Driver
from src.pages.login_page import LoginPage
from src.pages.headsup_page import HeadsUpPage


class Account:
    BoHCredentials = [
        # BoHCredentials pre-prod user
        ['diego11.lopez@nttdata.com', 'Password1']
    ]
    BoHEnvironments = ('dev', 'test', 'preprod', 'prod')

class TestBoHLogin(Driver):

    def setUp(self):
       super().setUp()
       SharedWorkflow.verifySplash(self)

    def teardown_method(self):
        super().tearDown()

    @pytest.mark.sanity
    @pytest.mark.parametrize('test_email, test_pwd', Account.BoHCredentials)
    def test_boh_okta_login(self, test_email, test_pwd):
        if LoginPage.isNormalUserLoggedIn(self) is False:
            LoginPage.oktaUserLogin(self, test_email, test_pwd)
        else:
            HeadsUpPage.verifyUserContentGuideLines(self)
        HeadsUpPage.verifyUserContentGuideLines(self)


