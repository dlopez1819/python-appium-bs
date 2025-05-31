from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class LocationPage(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def verifyLocationServices(self):
        LocationPage.__init__(self)
        if BoH.is_exist(self, self.locators.LocationScreen.sorryLocationMessage, expected=True):
            assert (BoH.is_exist(self, self.locators.LocationScreen.sorryLocationMessage)) is True, "User location service is disabled for BoH"
            BoH.click(self, self.locators.LocationScreen.okLocationButton)
        else:
            if self.apps == 'android':
                BoH.click(self, self.locators.LocationScreen.closeButton)
            else:
                BoH.tap_by_coordinates(self, 25, 70)
