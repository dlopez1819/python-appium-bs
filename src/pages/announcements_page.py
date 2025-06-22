from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver
from src.common.shared_workflow import SharedWorkflow

class AnnouncementsPage(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def verifyAnnouncements(self):
        AnnouncementsPage.__init__(self)
        BoH.wait_until_appear(self, self.locators.AnnouncementsScreen.announcementsTitle, 5)
        BoH.is_exist(self, self.locators.AnnouncementsScreen.announcementsTitle, expected=True)
        # Validate if list of announcements is not empty
        assert len(BoH.get_list_elements(self, self.locators.AnnouncementsScreen.announcementsContainerList)) != 0

    def closeAnnouncementsPage(self):
        SharedWorkflow.closePage(self)
