from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class LocationPage(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def verifyLocationServices(self):
        LocationPage.__init__(self)
      
