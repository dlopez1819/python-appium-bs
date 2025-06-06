from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver
from src.pages.alerts_page import AlertsPage
from src.pages.home_page import HomePage


class MenuPage(Driver):

    def __init__(self):
        self.locators = BoH.get_src_screen_enums(self)

    def logout(self):
        HomePage.homeAnnouncement(self)
        MenuPage.userLogOut(self)
        AlertsPage.wantToLogOutAlert(self)

    def guestLogOut(self):
        HomePage.homeAnnouncement(self)
        MenuPage.logInOrSignUp(self)

    def userLogOut(self):
        MenuPage.__init__(self)
        BoH.wait_until_appear(self, self.locators.MenuScreen.logoutButton)
        BoH.click(self, self.locators.MenuScreen.logoutButton)
        BoH.wait_until_disappear(self, self.locators.MenuScreen.logoutButton, 5)

    def logInOrSignUp(self):
        MenuPage.__init__(self)
        BoH.wait_until_appear(self, self.locators.MenuScreen.guestLogOutButton)
        BoH.click(self, self.locators.MenuScreen.guestLogOutButton)
        BoH.wait_until_disappear(self, self.locators.MenuScreen.guestLogOutButton, 5)

    def termsOfUse(self):
        MenuPage.__init__(self)
        HomePage.homeAnnouncement(self)
        BoH.click(self, self.locators.MenuScreen.termsOfUseButton)
        BoH.wait_until_disappear(self, self.locators.MenuScreen.termsOfUseButton, 5)

