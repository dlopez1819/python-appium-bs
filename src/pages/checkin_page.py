from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class CheckInPage(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def assertIfCheckingPage(self):
        CheckInPage.__init__(self)
        assert (BoH.is_exist(self, self.locators.CheckInScreen.checkInTitle)) is True, "Check-In Page is not displayed"

    def locationServices(self):
        CheckInPage.__init__(self)
        if BoH.is_exist(self, self.locators.CheckInScreen.sorryCheckInMessage, expected=True):
            assert (BoH.is_exist(self, self.locators.CheckInScreen.sorryCheckInMessage)) is True, "User location service is disabled for BoH"
            #BoH.click(self, self.locators.CheckInScreen.okCheckInButton)
            if self.apps == 'android':
                BoH.click(self, self.locators.CheckInScreen.okCheckInButton)
            else:
                #BoH.tap_by_coordinates(self, 195, 780)
                 BoH.tap_by_coordinates(self, 25, 65)
        else:
            if self.apps == 'android':
                BoH.click(self, self.locators.CheckInScreen.closeButton)
            else:
                BoH.tap_by_coordinates(self, 25, 65)
