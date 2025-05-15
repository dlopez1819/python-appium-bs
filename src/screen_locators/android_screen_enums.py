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
    #bohAuthAlert=  (AppiumBy.IOS_CLASS_CHAIN, "** / XCUIElementTypeStaticText[`name == '“BadgeOfHonor” Wants to Use “auth0.com” to Sign In'`]")
    #authContinueButton = (AppiumBy.ACCESSIBILITY_ID, "Continue")
    bohSendNotificationAlert = (AppiumBy.XPATH, "//*[contains(@text, 'Allow Badge of Honor to send you notifications?')]")
    allowButton = (AppiumBy.XPATH, "//*[contains(@text, 'Allow')]")

class HeadsUpScreen(Driver):
    #headsUpTitle = (AppiumBy.ACCESSIBILITY_ID, "Heads Up")
    #headsUpText = (AppiumBy.ACCESSIBILITY_ID, "Some services are down on our end and functionality might be limited. "
                                              #"You can continue to explore Badge of Honor but may experience bumps along the way.")
    #continueButton = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'OK'`]")
    warningTitle = (AppiumBy.XPATH, '//*[contains(@text, "Warning Before We Begin")]')
    warningText = (AppiumBy.XPATH, "//*[contains(@text, 'Rock crawling and off-road driving are inherently dangerous activities. "
                                   "By experiencing the Badge of Honor program, users assume the risk of off-road driving. "
                                   "Always take proper precautions and exercise discretion before attempting off-road driving. "
                                   "Including, without limitation, driving within your ability and experience, "
                                   "using appropriate harnessing devices and having proper safety gear ready.')]")
    ackContinueButton = (AppiumBy.XPATH, "//*[contains(@text, 'Acknowledge & Continue')]")

    headsUpUserContentTitle = (AppiumBy.XPATH, '//*[contains(@text, "USER CONTENT GUIDELINES")]')
    headsUpUserContentText = (AppiumBy.XPATH, '//*[contains(@text, "The user generated content policies for Jeep® Badge of Honor are designed to help ensure that everyone viewing contributed content has a positive experience. '
                                              'In order to use Badge of Honor as a registered user, please accept the following guidelines:")]')
    headsUpGuidelines1 = (AppiumBy.XPATH, '//*[contains(@text, "I represent and warrant that the content I post is not threatening, abusive, harmful, harassing, defamatory, vulgar, obscene, indecent, '
                                          'pornographic, invasive of another’s privacy, or racially, ethnically, unlawful, or otherwise unlawful or objectionable.")]')

    headsUpGuidelines2 = (AppiumBy.XPATH, '//*[contains(@text, "I have read the program Terms of Use and Privacy Policy.")]')
    acceptButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonUgcPrimary")
    logoutButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textUgcLogOutButton")
    termsOfUse = (AppiumBy.XPATH, '//*[contains(@text, "Terms of Use")]')
    privacyPolicy = (AppiumBy.XPATH, '//*[contains(@text, "Privacy Policy")]')

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
    #pageIndicatorDots = (AppiumBy.CLASS_NAME, "XCUIElementTypePageIndicator")

class HomeScreen(Driver):
    featuredTopNavBar = (AppiumBy.ACCESSIBILITY_ID, "FEATURED")
    imageFeaturedTrail = (AppiumBy.ID, "com.chrysler.JeepBOH:id/imageFeaturedTrailItem")
    homeBottomNavBar = (AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='android:id/icon'])[1]")
    checkinTrailButton = (AppiumBy.ACCESSIBILITY_ID, "Check in to this trail")
    featuredTrailRowContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutFeaturedTrailRowOneContainer")
    featuredTrailWeatherContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutFeaturedTrailWeatherContainer")

class LoginScreen(Driver):
    #jeepBOHImage = (AppiumBy.XPATH, "//*[@resource-id='com.chrysler.JeepBOH:id/layoutLogInContent']/android.widget.ImageView[2]")
    logoBoH = (AppiumBy.XPATH, "//*/android.widget.ImageView[2]")
    loginSignUpButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonLoginLogin") #com.chrysler.JeepBOH:id/buttonLoginLogin
    continueAsGuessButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonLoginSkip")
    alertAllowLocation = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_message")
    whileUsingAppButton = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")

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
