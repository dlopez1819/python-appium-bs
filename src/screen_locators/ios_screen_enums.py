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
    acceptButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'I Accept'`]")
    logoutButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Log Out'`]")
    termsOfUse = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Terms of Use'`]")
    privacyPolicy = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Privacy Policy'`]")


class NavigationScreen(Driver):
    exploreTrailsTitle = (AppiumBy.ACCESSIBILITY_ID, "Explore Trails")
    exploreTrailsText = (AppiumBy.ACCESSIBILITY_ID, "Use the Badge of Honor Trail Map to discover new trails to conquer, near or far.")
    uploadPhotosTitle = (AppiumBy.ACCESSIBILITY_ID, "Upload Photos")
    uploadPhotosText = (AppiumBy.ACCESSIBILITY_ID, "Capture your trail experiences and share them with the Jeep® brand community.")
    earnPointBadgesTitle = (AppiumBy.ACCESSIBILITY_ID, "Earn Points & Badges")
    earnPointBadgesText = (AppiumBy.ACCESSIBILITY_ID, "Become a decorated trail expert by checking in at the trailhead and earning badges for your Jeep® brand vehicle.")
    learnEssentialsTitle = (AppiumBy.ACCESSIBILITY_ID, "Learn the Essentials")
    learnEssentialsText = (AppiumBy.ACCESSIBILITY_ID, "Explore Off-Roading 101 to learn the basic safety principles and maneauvers of off-roading in your Jeep® brand vehicle.")

    skipButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Skip'`]")
    letsGoButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Let's Go'`]")
    pageIndicatorDots = (AppiumBy.CLASS_NAME, "XCUIElementTypePageIndicator")

class HomeScreen(Driver):
    featuredTopNavBar = (AppiumBy.ACCESSIBILITY_ID, "FEATURED")
    imageFeaturedTrail = (AppiumBy.ID, "com.chrysler.JeepBOH:id/imageFeaturedTrailItem")
    homeBottomNavBar = (AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='android:id/icon'])[1]")
    checkinTrailButton = (AppiumBy.ACCESSIBILITY_ID, "Check in to this trail")
    featuredTrailRowContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutFeaturedTrailRowOneContainer")
    featuredTrailWeatherContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutFeaturedTrailWeatherContainer")

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
