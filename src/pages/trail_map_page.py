from src.common.shared_workflow import SharedWorkflow
from src.helpers.app_objects import BoH
from src.helpers.appium_driver import Driver
from src.pages.trail_details_page import TrailDetailsPage
from src.pages.trails_sort_by_page import TrailsSortByPage

class TrailMapPage(Driver):

    def __init__(self):
        self.locators = BoH.get_src_screen_enums(self)

    def getTrayListResults(self):
        TrailMapPage.__init__(self)
        trailResult= BoH.get_attribute(self, self.locators.trailAndMapScreen.trailResults, 'text')
        # VALIDATE TRAIL LIST NOT EMPTY
        assert int("".join(char for char in trailResult if char.isdigit())) != 0, "Trail List is empty"

    def getMultiplePinMapResults(self):
        TrailMapPage.__init__(self)
        pinIndex = BoH.get_list_elements(self, self.locators.trailAndMapScreen.trayPinMapList)
        # VALIDATE MULTIPLE PINS IN MAP
        assert len(pinIndex) > 1, "Pin Map List is empty"

    def getHorizontalCardSize(self):
        card_XY = BoH.get_element_location(self, self.locators.trailAndMapScreen.getHorizontalCard(self, 1))
        card_size = BoH.element(self, self.locators.trailAndMapScreen.getHorizontalCard(self, 1)).size
        return (card_XY['x'], card_XY['y'], card_size['height'], card_size['width'] )

    def collapseTrayResults(self):
        TrailMapPage.__init__(self)
        if BoH.is_exist(self, self.locators.trailAndMapScreen.trailDragIndicator, False) or BoH.is_exist(self, self.locators.trailAndMapScreen.sortButton, True):
            tray_drag_down = BoH.get_element_location(self, self.locators.trailAndMapScreen.sortButton)
            if self.appiumserver == 'local':
                SharedWorkflow.scrolling(self, tray_drag_down['x'] + 420, tray_drag_down['y'], tray_drag_down['x'] + 420,
                                               tray_drag_down['y'] + 1500)
            else:
                #SharedWorkflow.scrolling(self, tray_drag_down['x'] + 420, tray_drag_down['y'], tray_drag_down['x'] + 420,
                                               #tray_drag_down['y'] + 1600)
                BoH.swipe_by_coordinates(self, tray_drag_down['x'] + 420, tray_drag_down['y'], tray_drag_down['x'] + 420, tray_drag_down['y'] + 1600, 900)
        # VALIDATE TRAIL CARD COLLAPSED
        assert (BoH.is_exist(self, self.locators.trailAndMapScreen.trailDragIndicator, True)), "Tray Result is not collapsed"

    def cardDisplay(self):
        TrailMapPage.__init__(self)
        tray_drag_up = BoH.get_element_location(self, self.locators.trailAndMapScreen.trailDragIndicator)
        if self.appiumserver == 'local':
            SharedWorkflow.scrolling(self, tray_drag_up['x'], tray_drag_up['y'], tray_drag_up['x'],
                                      tray_drag_up['y'] - 1500)
        else:
            #SharedWorkflow.scrolling(self, tray_drag_up['x'], tray_drag_up['y'], tray_drag_up['x'],
                                     # tray_drag_up['y'] - 1700)
             BoH.swipe_by_coordinates(self, tray_drag_up['x'], tray_drag_up['y'], tray_drag_up['x'], tray_drag_up['y'] - 1600, 900)
        assert (BoH.is_exist(self, self.locators.trailAndMapScreen.getTrayCard(self, 1), True)), "Tray Result is not collapsed"

    def swipeHorizontalTrailCard(self):
        TrailMapPage.__init__(self)
        card_X, card_Y, card_Height, card_Width = TrailMapPage.getHorizontalCardSize(self)
        if self.appiumserver == 'local':
            # Swipe Horizontal Left - Trail Cards
            SharedWorkflow.scrolling(self, card_X + card_Width  + 30, card_Y + card_Height - 300, card_X - 50, card_Y + card_Height - 300)
            # Swipe Horizontal Right - Trail Cards
            SharedWorkflow.scrolling(self, card_X - 50, card_Y + card_Height - 300, card_X + card_Width + 30, card_Y + card_Height - 300)
        else:
            BoH.swipe_by_coordinates(self, card_X + card_Width  + 30, card_Y + card_Height - 300, card_X - 50, card_Y + card_Height - 300, 900)
            BoH.swipe_by_coordinates(self, card_X - 50, card_Y + card_Height - 300, card_X + card_Width + 30, card_Y + card_Height - 300, 900)

    def verifyTrayCardEventChalenge(self):
        TrailMapPage.__init__(self)
        TrailMapPage.getTrayListResults(self)
        TrailMapPage.cardDisplay(self)
        TrailMapPage.trayImageCardPresent(self)
        TrailMapPage.trayEventPresent(self)
        TrailMapPage.trayChallengePresent(self)

    def verifySwipeCardEventChallengeMap(self):
        TrailMapPage.__init__(self)
        TrailMapPage.pinMapPresent(self)
        TrailMapPage.tapIndividualPinMap(self)
        TrailMapPage.horizontalCardPresent(self)
        TrailMapPage.swipeHorizontalTrailCard(self)

    def trayImageCardPresent(self):
        # Get Card Image List
        cardIndex = BoH.get_list_elements(self, self.locators.trailAndMapScreen.trayCardList)
        assert len(cardIndex) != 0, "Card List is empty"

    def horizontalCardPresent(self):
        # Get Card Image List
        cardIndex = BoH.get_list_elements(self, self.locators.trailAndMapScreen.horizontalCardList)
        assert len(cardIndex) != 0, "Card List is empty"

    def pinMapPresent(self):
        # Get Card Image List
        pinIndex = BoH.get_list_elements(self, self.locators.trailAndMapScreen.trayPinMapList)
        assert len(pinIndex) != 0, "Pin Map List is empty"

    def trayEventPresent(self):
        # Get Card Image List
        eventIndex = BoH.get_list_elements(self, self.locators.trailAndMapScreen.trayEventList)
        assert len(eventIndex) != 0, "Card List is empty"

    def trayChallengePresent(self):
        # Get Card Image List
        challenge_card = 'Twisted'
        challengeIndex = BoH.get_list_elements(self, self.locators.trailAndMapScreen.trayChallengeList)
        if challengeIndex is None or BoH.is_exist(self, self.locators.trailAndMapScreen.trayChallenge, False):
            TrailMapPage.searchForTrail(self, challenge_card)
            assert (BoH.is_exist(self, self.locators.trailAndMapScreen.trayChallenge,True)), "Tray Challenge is not present"
        elif challengeIndex is not None:
            assert (BoH.is_exist(self, self.locators.trailAndMapScreen.getChallenge(self, 1), True)), "Tray Challenge is not present"
        else:
            assert (BoH.is_exist(self, self.locators.trailAndMapScreen.trayChallenge,True)), "Tray Challenge is not present"

    def tapIndividualPinMap(self):
        TrailMapPage.__init__(self)
        BoH.click(self, self.locators.trailAndMapScreen.getPinMap(self, 1))

    def tapMultiplePinMap(self):
        TrailMapPage.__init__(self)
        pinIndex = BoH.get_list_elements(self, self.locators.trailAndMapScreen.trayPinMapList)
        for i in range(1, len(pinIndex)):
            BoH.click(self, self.locators.trailAndMapScreen.getPinMap(self, i))
            TrailDetailsPage.verifyTrailDetailsPage(self)

    def trailCardListDetails(self):
        TrailMapPage.__init__(self)
        card_index = BoH.get_list_elements(self, self.locators.trailAndMapScreen.trayCardList)
        for i in range(1, len(card_index)):
            BoH.click(self, self.locators.trailAndMapScreen.getTrayCard(self, i))
            TrailDetailsPage.verifyTrailDetailsPage(self)

    def pinMapCardDetails(self):
        TrailMapPage.__init__(self)
        cardIndex = BoH.get_list_elements(self, self.locators.trailAndMapScreen.horizontalCardList)
        BoH.click(self, self.locators.trailAndMapScreen.getHorizontalCard(self, len(cardIndex) - 1))
        TrailDetailsPage.verifyTrailDetailsPage(self)

    def searchForTrail(self, text):
        TrailMapPage.__init__(self)
        BoH.wait_until_appear(self, self.locators.trailAndMapScreen.searchTextBox, 3)
        BoH.send_keys(self, self.locators.trailAndMapScreen.searchTextBox, text)

    def verifySearchResult(self, text):
        assert (BoH.is_exist(self, self.locators.trailAndMapScreen.searchResult(self, text),
                             True)), "Search Trail not found"
        

    def trailsMapSortBy(self):
        TrailsSortByPage.sortByPage(self)
