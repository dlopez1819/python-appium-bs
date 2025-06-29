from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class TrailMapEventsPage(Driver):

    def __init__(self):
        self.locators = BoH.get_src_screen_enums(self)

    def assertIfTrailMapEventsPage(self):
        TrailMapEventsPage.__init__(self)
        assert (BoH.is_exist(self, self.locators.eventsTrailMapScreen.eventsTitle)) is True, "Events Page is not displayed"

    def allTrailEventsPresent(self):
        # Get Event Trail List
        eventsIndex = BoH.get_list_elements(self, self.locators.eventsTrailMapScreen.allTrailActivityList)
        assert eventsIndex != 0, "Events List is empty"
