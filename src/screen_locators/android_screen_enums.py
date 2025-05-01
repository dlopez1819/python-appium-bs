from appium.webdriver.common.appiumby import AppiumBy
from src.helpers.appium_driver import Driver

class SplashScreen(Driver):
    splashLogo= (AppiumBy.XPATH, "//*[ends-with(@resource-id, 'id/com.chrysler.JeepBOH:id/imageSplashLogo')]")
    warningBeforeBegin = (AppiumBy.ID, "com.chrysler.JeepBOH:id/textOnboardingTitle")
    continueButton= (AppiumBy.XPATH, "//*[ends-with(@resource-id, 'id/com.chrysler.JeepBOH:id/imageSplashLogo')]")
    alertNotification = (AppiumBy.XPATH, "//*[ends-with(@resource-id, 'id/com.chrysler.JeepBOH:id/iAcceptButton')]")
    allowButton = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")

class ExploreTrails(Driver):
    exploreTrailView = (AppiumBy.XPATH, "//*[@text='Explore Trails']")
    uploadPhotosView = (AppiumBy.XPATH, "//*[@text='Upload Photos']")
    earnPointsBadgesView = (AppiumBy.XPATH, "//*[@text='Earn Points & Badges']")
    learnEssentialsView = (AppiumBy.XPATH, "//*[@text='Learn the Essentials']")
    letsGoButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonOnboardingEssentialsGo")
    skipButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonOnboardingExploreTrailsSkip")

class HomeScreen(Driver):
    featuredTopNavBar = (AppiumBy.ACCESSIBILITY_ID, "FEATURED")
    imageFeaturedTrail = (AppiumBy.ID, "com.chrysler.JeepBOH:id/imageFeaturedTrailItem")
    homeBottomNavBar = (AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='android:id/icon'])[1]")
    checkinTrailButton = (AppiumBy.ACCESSIBILITY_ID, "Check in to this trail")
    featuredTrailRowContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutFeaturedTrailRowOneContainer")
    featuredTrailWeatherContainer = (AppiumBy.ID, "com.chrysler.JeepBOH:id/layoutFeaturedTrailWeatherContainer")

class LoginScreen(Driver):
    jeepBOHImage = (AppiumBy.XPATH, "//*[@resource-id='com.chrysler.JeepBOH:id/layoutLogInContent']/android.widget.ImageView[2]")
    loginSignUpButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonLoginLogin")
    continueAsGuessButton = (AppiumBy.ID, "com.chrysler.JeepBOH:id/buttonLoginSkip")
    alertAllowLocation = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_message")
    whileUsingAppButton = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")

class loginOktaScreen(Driver):
    bohText = (AppiumBy.XPATH, "//android.widget.TextView[@text='Badge of Honor - Android']")
    loginTab = (AppiumBy.XPATH, "//android.view.View[@text='Log In']")
    username = (AppiumBy.XPATH, "*//android.widget.EditText[@hint='Email']")
    password = (AppiumBy.XPATH, "*//android.widget.EditText[@hint='Password']")
    loginButton = (AppiumBy.XPATH, "//android.widget.Button[@text='Log In']")
    forgotPassword = (AppiumBy.XPATH, "//android.widget.TextView[@text='Don't remember your password?']")