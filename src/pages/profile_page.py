from src.helpers.app_objects import BoH
from src.pages.home_page import HomePage
from src.helpers.appium_driver import Driver

class ProfilePage(Driver):

    def __init__(self):
        self.locators = BoH.get_src_screen_enums(self)

    def assertIfProfilePage(self):
        HomePage.__init__(self)
        assert (BoH.is_exist(self, self.locators.ProfileScreen.homeTitle))

    def verifyProfileInfoDetails(self):
        ProfilePage.assertIfProfilePage(self)
