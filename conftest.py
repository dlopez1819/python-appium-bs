import logging
import pytest
from src.helpers.appium_driver import Driver

@pytest.hookimpl
def pytest_addoption(parser):
    # LOCAL SETTINGS
    #parser.addoption('--apps', action='store', default="android", help="Choose App: ios or android")
    # BROWSER STACK SETTINGS
    parser.addoption('--app', action='store', default="ios", help="Choose App: ios or android")
    parser.addoption('--device', action='store', default="emulator", help="Choose Device: simulator / emulator / real" "device")
    parser.addoption('--appiumServer', action='store', default="browserstack",
                     help="Choose Appium Server: local / browserstack / lambaTest")
    parser.addoption('--os', action='store', default="17",
                     help="Choose OS version: 13 / 17")

    parser.addoption('--env', action='store', default="preprod",
                     help="Choose environment: preprod / production")


@pytest.fixture(scope="session")
def apps(request):
    #return request.config.getoption("--apps") # local
    return request.config.getoption("--app")  #Browserstack


@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")


@pytest.fixture(scope="session")
def os(request):
    return request.config.getoption("--os")


@pytest.fixture(scope="session")
def appiumserver(request):
    return request.config.getoption("--appiumServer")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    test_name = rep.nodeid.replace(rep.fspath, "").replace("::", "__")
    if rep.when == "setup":
        if item.rep_setup.failed:
            Driver().retrieveBrowserstackLog(test_name)
            Driver().updateBrowserstackStatus(True, "setup running fail")
    if rep.when == "call":
        if item.rep_setup.passed and item.rep_call.failed:
            Driver().screenshot_on_failure(test_name)
            Driver().endVideoRecording(test_name, True)

    if rep.when == "teardown":
        if item.rep_setup.passed and item.rep_call.passed:
            if item.rep_teardown.failed:
                Driver().retrieveBrowserstackLog(test_name)
                Driver().updateBrowserstackStatus(True, "teardown running fail")
            else:
                Driver().endVideoRecording(test_name, False)

@pytest.fixture(scope='session')
def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.FileHandler(r'app.log', mode='w')
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', '%m/%d/%Y %I:%M:%S %p')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
