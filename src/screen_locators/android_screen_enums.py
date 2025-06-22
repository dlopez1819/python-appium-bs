from appium.webdriver.common.appiumby import AppiumBy
from src.helpers.appium_driver import Driver

class SplashScreen(Driver):
    splashLogo= (AppiumBy.XPATH, "//*[ends-with(@resource-id, 'com.chrysler.JeepBOH:id/imageSplashLogo')]")
    warningBeforeBegin = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textOnboardingTitle")
    continueButton= (AppiumBy.XPATH, "//*[ends-with(@resource-id, 'id/com.chrysler.JeepBOH:id/imageSplashLogo')]")
    alertNotification = (AppiumBy.XPATH, "//*[ends-with(@resource-id, 'id/com.chrysler.JeepBOH:id/iAcceptButton')]")
    allowButton = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")

class AlertsScreen(Driver):
    locationAlert = (AppiumBy.XPATH, "//*[contains(@text, 'Allow Badge of Honor to access this device’s location?')]")
    allowOnceButton = (AppiumBy.XPATH, "//*[contains(@text, 'While using the app')]")
    bohSendNotificationAlert = (AppiumBy.XPATH, "//*[contains(@text, 'Allow Badge of Honor to send you notifications?')]")
    allowButton = (AppiumBy.XPATH, "//*[contains(@text, 'Allow')]")
    wantToLogOut = (AppiumBy.ID, "com.chrysler.JeepBOH:id/alertTitle")
    yesLogOutButton = (AppiumBy.XPATH, '//*[contains(@text, "YES")]')

class HeadsUpScreen(Driver):
    warningTitle = (AppiumBy.ID, 'com.chrysler.JeepBOH:id/textOnboardingTitle')
    warningText = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textOnboardingBody")
    ackContinueButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/iAcceptButton")

    headsUpUserContentTitle = (AppiumBy.XPATH, '//*[contains(@text, "USER CONTENT GUIDELINES")]')
    headsUpUserContentText = (AppiumBy.XPATH, '//*[contains(@text, "The user generated content policies for Jeep® Badge of Honor are designed to help ensure that everyone viewing contributed content has a positive experience. '
                                              'In order to use Badge of Honor as a registered user, please accept the following guidelines:")]')
    headsUpGuidelines1 = (AppiumBy.XPATH, '//*[contains(@text, "I represent and warrant that the content I post is not threatening, abusive, harmful, harassing, defamatory, vulgar, obscene, indecent, '
                                          'pornographic, invasive of another’s privacy, or racially, ethnically, unlawful, or otherwise unlawful or objectionable.")]')

    headsUpGuidelines2 = (AppiumBy.XPATH, '//*[contains(@text, "I have read the program Terms of Use and Privacy Policy.")]')

class UserGuideLinesScreen(Driver):
    acceptButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonUgcPrimary")
    logoutButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textUgcLogOutButton")
    termsOfUseButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textUgcTermsButton")
    privacyPolicyButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textUgcPrivacyButton")

    termsOfUseTitle = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textHamburgerContentToolbarTitle")
    privacyPolicyTitle = (AppiumBy.XPATH, "//android.widget.TextView[@text='FCA US Privacy Policy']")
    closeTermsOfUse = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonHamburgerContentClose")

class NavigationScreen(Driver):
    exploreTrailsTitle = (AppiumBy.XPATH, "//*[contains(@text, 'Explore Trails')]")
    exploreTrailsText = (AppiumBy.XPATH, "//*[contains(@text, 'Use the Badge of Honor Trail Map to discover new trails to conquer, near or far.')]")
    uploadPhotosTitle = (AppiumBy.XPATH, "//*[contains(@text, 'Upload Photos')]")
    uploadPhotosText = (AppiumBy.XPATH, "//*[contains(@text, 'Capture your trail experiences and share them with the Jeep® brand community.')]")
    earnPointBadgesTitle = (AppiumBy.XPATH, "//*[contains(@text, 'Earn Points & Badges')]")
    earnPointBadgesText = (AppiumBy.XPATH, "//*[contains(@text, 'Become a decorated trail expert by checking in at the trailhead and earning badges for your Jeep® brand vehicle.')]")
    learnEssentialsTitle = (AppiumBy.XPATH, "//*[contains(@text, 'Learn the Essentials)]")
    learnEssentialsText = (AppiumBy.XPATH, "//*[contains(@text, 'Explore Off-Roading 101 to learn the basic safety principles and maneuvers of off-roading in your Jeep® brand vehicle.)]")
    skipButton = (AppiumBy.XPATH, "//*[contains(@text, 'Skip')]")
    letsGoButton = (AppiumBy.XPATH, "//*[ends-with(@resource-id, 'com.chrysler.JeepBOH:id/buttonOnboardingEssentialsGo')]") # Let’s Go
    okButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/btn_popup_dialog_action_primary")
    closeButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/btn_popup_dialog_action_close")

class HomeScreen(Driver):
    homeTitle = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textToolbarMainTitle")
    featuredTopNavBar = (AppiumBy.ACCESSIBILITY_ID, "FEATURED")
    imageFeaturedTrail = (AppiumBy.ID, "com.chrysler.JeepBOH:id/imageFeaturedTrailItem")

    iconCheckIn = (AppiumBy.ACCESSIBILITY_ID, "Check in to this trail")
    iconTrailDetails = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textFeaturedTrailName")
    trailDifficultyText = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textFeaturedTrailDifficultyHeaderButton")
    currentConditionsText = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textFeaturedTrailCurrentConditionsHeader")
    trailForcastText = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textFeaturedTrailForecastHeader")
    daylightRemainingText = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textFeaturedTrailDaylightHeader")
    trailLeaderboardSection = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textFeaturedTrailLeaderboardHeader")
    viewLeaderboard = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonFeaturedTrailLeaderboardViewAll")
    
    homeBottomNavBar = (AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='android:id/icon'])[1]")
    checkinTrailButton = (AppiumBy.ACCESSIBILITY_ID, "Check in to this trail")
    featuredTrailRowContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutFeaturedTrailRowOneContainer")
    featuredTrailWeatherContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutFeaturedTrailWeatherContainer")
    homeButton = (AppiumBy.ACCESSIBILITY_ID, "menu")

class BottomNavBarScreen(Driver):
    homeBottomBar = (AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='android:id/icon'])[1]")

class LoginScreen(Driver):
    logoBoH = (AppiumBy.XPATH, "//*/android.widget.ImageView[2]")
    loginSignUpButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonLoginLogin") 
    alertAllowLocation = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_message")
    whileUsingAppButton = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    continueAsGuessButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonLoginSkip")

class loginOktaScreen(Driver):
    urlField = (AppiumBy.ID, "com.android.chrome:id/url_bar")
    bohText = (AppiumBy.XPATH, "//android.widget.TextView[@text='Badge of Honor - Android']")
    loginTab = (AppiumBy.XPATH, "//android.view.View[@text='Log In']")
    username = (AppiumBy.XPATH, "*//android.widget.EditText[@hint='Email']")
    password = (AppiumBy.XPATH, "*//android.widget.EditText[@hint='Password']")
    loginButton = (AppiumBy.XPATH, "//android.widget.Button[@text='Log In']")
    forgotPassword = (AppiumBy.XPATH, "//android.widget.TextView[@text='Don't remember your password?']")
    username_BS = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='1-email']")
    password_BS = (AppiumBy.XPATH, "//*/android.view.View[4]/android.view.View/android.view.View/android.widget.EditText")
    loginButton_BS = (AppiumBy.XPATH, "//android.widget.Button[@text='Log In']")
    loginTab_BS =  (AppiumBy.XPATH, "//android.view.View[@text='Log In']")
    closeTab_BS = (AppiumBy.ACCESSIBILITY_ID, "Close tab")

class loginAsGuest(Driver):
    continueAsGuestButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonSkipLoginSkip")
    dontHaveProfileTitle = (AppiumBy.ID, "com.chrysler.JeepBOH:id/no_profile_header")

class MenuScreen(Driver):
    logoutButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonHamburgerSignOut")
    guestLogOutButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonHamburgerGuestSignIn")
    termsOfUseButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonHamburgerTermsOfUse")
    disclaimerButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonHamburgerDisclaimer")
    faqsButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonHamburgerFaqs")
    offRoading101Button = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonHamburgerOffRoading")
    announcementsButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonHamburgerAnnouncements")
    suggestATrailButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonHamburgerSuggest")
    earnABadgeButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonHamburgerTutorialCheckInTrail")

class ProfileScreen(Driver):
    logoutButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonHamburgerSignOut")

class VehicleProfileScreen(Driver):
    updateProfileButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonEvUpdate")
    dismissProfileButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonEvDismiss")
    closeVehicleNotification = (AppiumBy.ID, "Close notification")

class LocationScreen(Driver):
    sorryLocationMessage = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textGeneralFragmentTitle")
    okLocationButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonGeneralFragmentPrimary")
    checkinLocationTitle = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textToolbarDialogTitle")
    checkinButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/trail_checkin_button")
    closeButton = (AppiumBy.ACCESSIBILITY_ID, "Close")

class TrailsDetailsScreen(Driver):
    trailDetailsTitle = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textToolbarMainTitle")
    iconBackArrow = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonToolbarMainLeft")

    iconBackBSArrow = (AppiumBy.XPATH, "//android.widget.ImageButton[@resource-id='com.chrysler.JeepBOH:id/buttonToolbarMainLeft']")


class LeaderboardScreen(Driver):
    tabLeaderboardTitle = (AppiumBy.ACCESSIBILITY_ID, "LEADERBOARD")
    iconTrophy= (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonLeaderboardMyRank")
    trailsList = (AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='com.chrysler.JeepBOH:id/layoutLeaderboardItemContent'])")
    trailExplorer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textLeaderboardTrailFilter")

class CheckInScreen(Driver):
    subHeaderText = (AppiumBy.ID, "com.chrysler.JeepBOH:id/trail_checkin_subheader")
    headerText = (AppiumBy.ID, "com.chrysler.JeepBOH:id/trail_checkin_header")
    checkInBodyTextView = (AppiumBy.XPATH, "//*[contains(@text, 'Checking in to a trail displays on your profile so other off-roaders can follow your adventures. "
                                  "After you check in, you can also request a hard badge, if you haven’t already.')]")
    checkInButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/trail_checkin_button")
    checkInTitle = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textToolbarDialogTitle")
    closeButton = (AppiumBy.ACCESSIBILITY_ID, "Close")
    sorryCheckInMessage = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textGeneralFragmentTitle")
    okCheckInButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonGeneralFragmentPrimary")

class TermsOfUseScreen(Driver):
    termOfUseTitle = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textHamburgerContentToolbarTitle")
    closeButton= (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonHamburgerContentClose")
    contentBodyText = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textHamburgerContentBody")

class DisclaimerScreen(Driver):
    disclaimerTitle = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textHamburgerContentToolbarTitle")
    closeButton= (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonHamburgerContentClose")
    contentBodyText = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textHamburgerContentBody")

class FAQsScreen(Driver):
    faqsTitle = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textOffroadingDialogToolbar")
    closeButton= (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonOffroadingDialogToolbarBack")
    contentBodyText = (AppiumBy.XPATH, '//*[contains(@text, "Can anyone sign up for the program and get hard badges for their vehicle?")]')

class OffRoading101Screen(Driver):
    offRoadingTitle = (AppiumBy.ID, "com.chrysler.JeepBOH:id/imageOffroadingHeaderBanner")
    trailDiffRatingContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutOffroadingTrailDifficultyContainer")
    safetyChecklistContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutOffroadingSafetyContainer")
    briefHistoryContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutOffroadingHistoryContainer")
    terrainElementsContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutOffroadingElementsContainer")
    trailRatedContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutOffroadingVehiclesContainer")
    offRoadsFaqsContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutOffroadingFaqsContainer")

class AnnouncementsScreen(Driver):
    announcementsTitle = (AppiumBy.XPATH, "//*[contains(@text, 'ANNOUNCEMENTS')]")
    announcementsContainerList = (AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='com.chrysler.JeepBOH:id/layoutAnnouncementItemBottomContainer'])[1]")

class SuggestATrailScreen(Driver):
    suggestATrailTitle = (AppiumBy.XPATH, "//*[contains(@text, 'SUGGEST A TRAIL')]")

class earnABadgeScreen(Driver):
    earnBadgeTitle = (AppiumBy.XPATH, "//*[contains(@text, 'Check Into Trails And Earn Badges')]")
    openMapsTitle = (AppiumBy.XPATH, "//*[contains(@text, 'Open Maps from the Bottom Menu')]")
    openTrailTitle = (AppiumBy.XPATH, "//*[contains(@text, 'Open a Trail')]")
    tapEarnBadgeTitle = (AppiumBy.XPATH, "//*[contains(@text, 'Tap the Earn Badge Button')]")
    checkIntoTrailTitle = (AppiumBy.XPATH, "//*[contains(@text, 'Check Into the Trail')]")


    

