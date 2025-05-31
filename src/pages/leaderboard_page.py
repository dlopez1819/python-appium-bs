from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver

class LeaderBoardPage(Driver):

    def __init__(self):
        self.width, self.height = BoH.get_screen_dimension(self)
        self.offset = 30
        self.locators = BoH.get_src_screen_enums(self)

    def verifyLeaderboardPage(self):
        LeaderBoardPage.__init__(self)
        # validate Leaderboard tab enabled
        if self.apps == 'ios':
            value = BoH.get_attribute(self, self.locators.LeaderboardScreen.tabLeaderboardTitle, 'value')
            BoH.assert_equal(self, value, "1")
        else:
            value = BoH.get_attribute(self, self.locators.LeaderboardScreen.tabLeaderboardTitle, 'selected')
            BoH.assert_boolean(value, 'true')
