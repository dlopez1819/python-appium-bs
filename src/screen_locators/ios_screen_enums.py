from appium.webdriver.common.appiumby import AppiumBy
from src.helpers.appium_driver import Driver

class SplashScreen(Driver):
    splashLogo= (AppiumBy.ACCESSIBILITY_ID, "logo-boh-new")
    alertNotification = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == ''Badge of Honor' Would Like to Send You Notifications'`]")
    allowButton = (AppiumBy.ACCESSIBILITY_ID, "Allow")

class AlertsScreen(Driver):
    locationAlert = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Allow “Badge of Honor” to use your location?'`]")
    allowOnceButton = (AppiumBy.ACCESSIBILITY_ID, "Allow Once")
    bohAuthAlert=  (AppiumBy.IOS_CLASS_CHAIN, "** / XCUIElementTypeStaticText[`name == '“BadgeOfHonor” Wants to Use “auth0.com” to Sign In'`]")
    authContinueButton = (AppiumBy.ACCESSIBILITY_ID, "Continue")
    bohSendNotificationAlert = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "“Badge of Honor” Would Like to Send You Notifications"`]')
    allowButton = (AppiumBy.ACCESSIBILITY_ID, "Allow")

class HeadsUpScreen(Driver):
    headsUpTitle = (AppiumBy.ACCESSIBILITY_ID, "Heads Up")
    headsUpText = (AppiumBy.ACCESSIBILITY_ID, "Some services are down on our end and functionality might be limited. "
                                              "You can continue to explore Badge of Honor but may experience bumps along the way.")
    continueButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'OK'`]")
    warningTitle = (AppiumBy.ACCESSIBILITY_ID, "Warning Before We Begin")
    warningText = (AppiumBy.ACCESSIBILITY_ID, "Rock crawling and off-road driving are inherently dangerous activities. "
                                              "By experiencing the Badge of Honor program, users assume the risk of off-road driving. "
                                              "Always take proper precautions and exercise discretion before attempting off-road driving. "
                                              "Including, without limitation, driving within your ability and experience, "
                                              "using appropriate harnessing devices and having proper safety gear ready.")
    ackContinueButton = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Acknowledge & Continue"`]')

    headsUpUserContentTitle = (AppiumBy.ACCESSIBILITY_ID, "USER CONTENT GUIDELINES")
    headsUpUserContentText = (AppiumBy.ACCESSIBILITY_ID, "The user generated content policies for Jeep® Badge of Honor are designed to help ensure that everyone viewing contributed content has a positive experience. "
                                                    "In order to use Badge of Honor as a registered user, please accept the following guidelines:")
    headsUpGuidelines1 = (AppiumBy.ACCESSIBILITY_ID, "I represent and warrant that the content I post is not threatening, abusive, harmful, harassing, defamatory, vulgar, obscene, indecent, pornographic,"
                                                     " invasive of another’s privacy, or racially, ethnically, unlawful, or otherwise unlawful or objectionable.")

    headsUpGuidelines2 = (AppiumBy.ACCESSIBILITY_ID, "I have read the program Terms of Use and Privacy Policy.")

class UserGuideLinesScreen(Driver):
    acceptButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'I Accept'`]")
    logoutButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Log Out'`]")
    termsOfUseButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Terms of Use'`]")
    privacyPolicyButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Privacy Policy'`]")

    termsOfUseTitle = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'TERMS OF USE'`]")
    privacyPolicyTitle = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'FCA US Privacy Policy'`]")
    closeTermsOfUse = (AppiumBy.ACCESSIBILITY_ID, "icon close")
    closePrivacyPolicy = (AppiumBy.IOS_CLASS_CHAIN, " ** / XCUIElementTypeStaticText[`name == 'Done'`]")


class NavigationScreen(Driver):
    exploreTrailsTitle = (AppiumBy.ACCESSIBILITY_ID, "Explore Trails")
    exploreTrailsText = (AppiumBy.ACCESSIBILITY_ID, "Use the Badge of Honor Trail Map to discover new trails to conquer, near or far.")
    uploadPhotosTitle = (AppiumBy.ACCESSIBILITY_ID, "Upload Photos")
    uploadPhotosText = (AppiumBy.ACCESSIBILITY_ID, "Capture your trail experiences and share them with the Jeep® brand community.")
    earnPointBadgesTitle = (AppiumBy.ACCESSIBILITY_ID, "Earn Points & Badges")
    earnPointBadgesText = (AppiumBy.ACCESSIBILITY_ID, "Become a decorated trail expert by checking in at the trailhead and earning badges for your Jeep® brand vehicle.")
    learnEssentialsTitle = (AppiumBy.ACCESSIBILITY_ID, "Learn the Essentials")
    learnEssentialsText = (AppiumBy.ACCESSIBILITY_ID, "Explore Off-Roading 101 to learn the basic safety principles and maneauvers of off-roading in your Jeep® brand vehicle.")

    trailAndBadgesTitle = (AppiumBy.ACCESSIBILITY_ID, "Check Into Trails And Earn Badges")
    openMapsFromMenuTitle = (AppiumBy.ACCESSIBILITY_ID, "Open Maps from the Bottom Menu")
    openTrailTitle = (AppiumBy.ACCESSIBILITY_ID, "Open a Trail")
    earnBadgeButtonTitle = (AppiumBy.ACCESSIBILITY_ID, "Tap the Earn Badge Button")
    checkIntoTrailTitle = (AppiumBy.ACCESSIBILITY_ID, "Check Into the Trail")
    skipButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Skip'`]")
    letsGoButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Let's Go'`]")
    pageIndicatorDots = (AppiumBy.CLASS_NAME, "XCUIElementTypePageIndicator")
    closePage = (AppiumBy.ACCESSIBILITY_ID, "icon close24")

class HomeScreen(Driver):
    homeTitle = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'HOME'`]")
    featuredTopNavBar = (AppiumBy.ACCESSIBILITY_ID, "FEATURED")
    imageFeaturedTrail = (AppiumBy.ID, "com.chrysler.JeepBOH:id/imageFeaturedTrailItem")
    iconLocation = (AppiumBy.ACCESSIBILITY_ID, "icon_Check_In")
    iconTrailDetails = (AppiumBy.XPATH, "(//XCUIElementTypeImage[@name='icon-chevron'])[1]")
    trailDifficultyText = (AppiumBy.ACCESSIBILITY_ID, "TRAIL DIFFICULTY")
    currentConditionsText = (AppiumBy.ACCESSIBILITY_ID, "CURRENT CONDITIONS")
    trailForcastText = (AppiumBy.ACCESSIBILITY_ID, "TRAIL FORECAST")
    daylightRemainingText = (AppiumBy.ACCESSIBILITY_ID, "DAYLIGHT REMAINING")
    trailLeaderboardSection = (AppiumBy.ACCESSIBILITY_ID, "Trail Leaderboard")
    viewLeaderboard = (AppiumBy.ACCESSIBILITY_ID, "View Leaderboard")

    checkinTrailButton = (AppiumBy.ACCESSIBILITY_ID, "Check in to this trail")
    featuredTrailRowContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutFeaturedTrailRowOneContainer")
    featuredTrailWeatherContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutFeaturedTrailWeatherContainer")
    homeButton = (AppiumBy.ACCESSIBILITY_ID, "icon burger announcement")
    homeBSButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'icon burger announcement'`]")
    
    homeBottomNavBar = (AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='android:id/icon'])[1]")
    checkinTrailButton = (AppiumBy.ACCESSIBILITY_ID, "Check in to this trail")
    featuredTrailRowContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutFeaturedTrailRowOneContainer")
    featuredTrailWeatherContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutFeaturedTrailWeatherContainer")

class BottomNavBarScreen(Driver):
    homeBottomBar = (AppiumBy.ACCESSIBILITY_ID, "Main Feature Home")

class LoginScreen(Driver):
    logoBoH = (AppiumBy.ACCESSIBILITY_ID, "logo-boh-new")
    preprodButton = (AppiumBy.ACCESSIBILITY_ID, "preprod")
    loginSignUpButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Log In or Sign Up'`]")
    continueAsGuessButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Continue As Guest'`]")

class loginOktaScreen(Driver):
    urlField = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'URL'`]")
    loginTab =  (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Log In'`]")
    username = (AppiumBy.ACCESSIBILITY_ID, "Email")
    password = (AppiumBy.ACCESSIBILITY_ID, "Password")
    cancelButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Cancel'`]")
    loginButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Log In'`]")
    keyboardOn = (AppiumBy.ACCESSIBILITY_ID, "space")
    keyboardDone = (AppiumBy.ACCESSIBILITY_ID, "Done")

class loginAsGuest(Driver):
    continueAsGuestButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Continue As Guest'`][2]")
    dontHaveProfileTitle = (AppiumBy.ACCESSIBILITY_ID, "Don't Have a Profile?")

class ProfileScreen(Driver):
    logoutButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Log Out'`]")

class VehicleProfileScreen(Driver):
    updateProfileButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Update Vehicle Profile'`]")
    dismissProfileButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Dismiss'`]")
    closeVehicleNotification = (AppiumBy.ACCESSIBILITY_ID, "icon close24")

class MenuScreen(Driver):
    logoutButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Log Out'`]")
    guestLogOutButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Log In Or Sign Up'`]")
    termsOfUseButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Terms of Use'`]")

class LocationScreen(Driver):
    sorryLocationMessage = (AppiumBy.ACCESSIBILITY_ID, "Sorry")
    okLocationButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Ok'`]")
    checkinLocationTitle = (AppiumBy.IOS_CLASS_CHAIN, "C**/XCUIElementTypeStaticText[`name == 'CHECK-IN'`]")
    checkinButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Check-In'`]")
    closeButton = (AppiumBy.ACCESSIBILITY_ID, "icon close24")

class TrailsDetailsScreen(Driver):
    trailDetailsTitle = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'TRAIL DETAILS'`]")
    iconBackArrow = (AppiumBy.ACCESSIBILITY_ID, "icon backArrow")

class LeaderboardScreen(Driver):
    tabLeaderboardTitle = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'LEADERBOARD'`]")
    iconTrophy= (AppiumBy.ACCESSIBILITY_ID, "icon trophy circle")
    trailsList = (AppiumBy.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeButton")
    trailExplorer = (AppiumBy.ACCESSIBILITY_ID, "Trail Explorer")

class TrailsMapScreen(Driver):
    trailMapTitle = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'MAP'`]")
    trailsTopNavBar= (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'TRAILS'`]")
    mapsBottomNavBar = (AppiumBy.ACCESSIBILITY_ID, "Main Feature Maps")
    searchTextField = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeTextField[`value == 'Search by name or state'`]")
    iconSortBy = (AppiumBy.ACCESSIBILITY_ID, "icon sort")
    trailsList = (AppiumBy.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell'")
    iconPinTrailsList = (AppiumBy.IOS_CLASS_CHAIN,"**/XCUIElementTypeImage[`name == 'iconPinTrailMin'`]")
    typeMap = (AppiumBy.IOS_PREDICATE, "type == 'XCUIElementTypeMap'")

class TrailsSortByScreen(Driver):
    sorByTitle = (AppiumBy.ACCESSIBILITY_ID, "Sort By")
    byAlphabetical = (AppiumBy.NAME, "Alphabetical")
    byDifficulty = (AppiumBy.NAME, "Difficulty")
    byMostPopular = (AppiumBy.NAME, "Most Popular")
    byAverageUserRating = (AppiumBy.NAME, "Average User Rating")
    byResetResults = (AppiumBy.NAME, "Reset Results")
    closeButton = (AppiumBy.ACCESSIBILITY_ID, "icon close24")

class CheckInScreen(Driver):
    #subHeaderText = (AppiumBy.ID, "com.chrysler.JeepBOH:id/trail_checkin_subheader")
    #headerText = (AppiumBy.ID, "com.chrysler.JeepBOH:id/trail_checkin_header")
    #checkInBodyTextView = (AppiumBy.XPATH, "//*[contains(@text, 'Checking in to a trail displays on your profile so other off-roaders can follow your adventures. "
    #                              "After you check in, you can also request a hard badge, if you haven’t already.')]")
    checkInButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Check-In'`]")
    checkInTitle = (AppiumBy.IOS_CLASS_CHAIN, "C**/XCUIElementTypeStaticText[`name == 'CHECK-IN'`]")
    closeButton = (AppiumBy.ACCESSIBILITY_ID, "icon close24")
    sorryCheckInMessage = (AppiumBy.ACCESSIBILITY_ID, "Sorry")
    okCheckInButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Ok'`]")

class TermsOfUseScreen(Driver):
    termOfUseTitle = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'TERMS OF USE'`]")
    closeButton= (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'icon close'`]")
    contentBodyText = (AppiumBy.CLASS_NAME, "XCUIElementTypeTextView")

