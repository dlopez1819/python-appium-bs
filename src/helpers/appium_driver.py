import os
import time
from appium import webdriver
import pytest
from appium.options.android import UiAutomator2Options
#from appium.common.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
import requests
from settings import *
from datetime import datetime
import base64
import json

class Driver():
    driver = None

    def setUp(self):
        """
        This method instantiates the appium driver
        """
        global appiumserver
        appiumserver = self.appiumserver

        global desired_caps
        self.logger.info("Configuring desired capabilities")

        desired_caps = CONFIG[appiumserver][self.apps]
        desired_caps['apps'] = self.apps
        if self.appiumserver == "local":
            desired_caps['device'] = self.device
            desired_caps['os_version'] = self.os
        else:
            desired_caps['device'] = desired_caps['deviceName']
            desired_caps['os_version'] = desired_caps['platformVersion']
        desired_caps['name'] = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]

        if self.appiumserver == "local":
            if self.apps == "android":
                pass
        else:
            if os.environ.get('browserstack_custom_id') is not None:
                desired_caps['app'] = os.environ.get('browserstack_custom_id')
            if os.environ.get('browserstack_build_id') is not None:
                desired_caps['build'] = os.environ.get('browserstack_build_id') + "#" + self.device
            else:
                desired_caps['build'] = CONFIG['browserstack_user'] + self.device + "#" + str(time.time())

        self.logger.info(self.apps)
        self.logger.info("Initiating Appium driver")

        url = CONFIG[appiumserver]['appiumserverlocation']

        # Query the Browserstack current parallel running request
        if appiumserver == 'browserstack':
            response = requests.get(self.browserstack_requestURL('plan.json'))
            current_running_parallel = response.json()['parallel_sessions_running']
            max_running_parallel = response.json()['parallel_sessions_max_allowed']
            while current_running_parallel >= max_running_parallel:
                time.sleep(30)
                response = requests.get(self.browserstack_requestURL('plan.json'))
                current_running_parallel = response.json()['parallel_sessions_running']
                max_running_parallel = response.json()['parallel_sessions_max_allowed']

        appium_service = AppiumService()
        if self.apps == "android":
            capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        else:
            capabilities_options = XCUITestOptions().load_capabilities(desired_caps)

        if self.appiumserver == "local":
            #url = CONFIG[appiumserver]['appiumserverlocation']
            Driver.driver = webdriver.Remote(command_executor=url, options=capabilities_options)
        else:
            #remoteURL = 'https://' + CONFIG['browserstack_user'] + ':' + CONFIG['browserstack_accesskey']+ '@hub-cloud.browserstack.com/wd/hub'
            #remoteURL = 'https://diegolopez_JMV6tn:DsRBxpbCyFu1ZhLF4w3q@hub-cloud.browserstack.com/wd/hub' #"https://hub.browserstack.com/wd/hub"
            session_capabilities = capabilities_options
            Driver.driver = webdriver.Remote(command_executor=url, options=session_capabilities)
            pass
       # Driver.driver = webdriver.Remote(url, desired_caps)

    def setUp2(self):

        global appiumserver
        appiumserver = self.appiumserver

        global capabilities, session_capabilities
        self.logger.info("Configuring desired capabilities")

        if  self.appiumserver == "local":
            capabilities = dict(CONFIG[appiumserver][self.apps])
        else:
            capabilities = CONFIG_BS

        if self.appiumserver == "local":
            capabilities['device'] = self.device
            capabilities['os_version'] = self.os
            capabilities['name'] = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
            if self.apps == "android":
                if self.env == "preprod":
                    # TO DO
                    pass
                    #capabilities['app'] = '/Users/nttdata/Documents/pytestBoH/boh_mobile_appium/apps/app-boh.apk',

        self.logger.info(self.apps)
        self.logger.info("Initiating Appium driver")

        # Query the Browserstack current parallel running request
        """"""""""""""""
        if appiumserver == 'browserstack':
            response = requests.get(self.browserstack_requestURL('plan.json'))
            current_running_parallel = response.json()['parallel_sessions_running']
            max_running_parallel = response.json()['parallel_sessions_max_allowed']
            while current_running_parallel >= max_running_parallel:
                time.sleep(30)
                response = requests.get(self.browserstack_requestURL('plan.json'))
                current_running_parallel = response.json()['parallel_sessions_running']
                max_running_parallel = response.json()['parallel_sessions_max_allowed']
        """""
        appium_service = AppiumService()
        if self.apps == "android":
            capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
        else:
            capabilities_options = XCUITestOptions().load_capabilities(capabilities)

        if self.appiumserver == "local":
            url = CONFIG[appiumserver]['appiumserverlocation']
            Driver.driver = webdriver.Remote(command_executor=url, options=capabilities_options)
        else:
            remoteURL = 'https://' + CONFIG['browserstack_user'] + ':' + CONFIG['browserstack_accesskey']+ '@hub-cloud.browserstack.com/wd/hub'
            #remoteURL = 'https://diegolopez_JMV6tn:DsRBxpbCyFu1ZhLF4w3q@hub-cloud.browserstack.com/wd/hub' #"https://hub.browserstack.com/wd/hub"
            session_capabilities = capabilities_options
            Driver.driver = webdriver.Remote(command_executor=remoteURL, options=session_capabilities)

    def tearDown(self):
        if Driver.driver is not None:
            Driver.driver.quit()

    def browserstack_requestURL(self, path):
        url = 'https://' + CONFIG['browserstack_user'] + ':' + CONFIG['browserstack_accesskey'] + \
              '@api-cloud.browserstack.com/app-automate/' + path
        return url

    def retrieveBrowserstackLog(self, test_name):
        if Driver.driver is not None:
            response = requests.get(self.browserstack_requestURL('sessions/' + Driver.driver.session_id + '.json'))
            if not os.path.exists('./report/browserstacklog'):
                os.makedirs('./report/browserstacklog')
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            file = open('./report/browserstacklog/' + test_name + '_' + now + '.json', 'w')
            file.write(response.text)
            file.close()

    def updateBrowserstackStatus(self, bFail, message="notset"):
        if Driver.driver is not None:
            if bFail:
                # Case running fail
                status = "failed"
            else:
                message = "Case Running pass"
                status = "passed"
            data = '{"status": "' + status + '", "reason": "' + message + '"}'
            print(data)
            headers = {'Content-Type': 'application/json'}
            response = requests.put(self.browserstack_requestURL('sessions/' + Driver.driver.session_id + '.json'),
                                    data=data,
                                    headers=headers)
            print(response.json())

    def getBrowserstackSessionPublicURL(self):
        if appiumserver == 'browserstack':
            if Driver.driver is not None:
                response = requests.get(self.browserstack_requestURL('sessions/' + Driver.driver.session_id + '.json'))
                # automation_session.public_url
                publicURL = json.loads(response.text)["automation_session"]["public_url"]
                publicURL = "#BrowserStack Public URL: " + publicURL
                return publicURL
            else:
                return "Browserstack Driver session not created successfully!"
        return ""

    def screenshot_on_failure(self, test_name):
        if appiumserver == 'local':
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            if not os.path.exists('./report/screenshots'):
                os.makedirs('./report/screenshots')

            Driver.driver.save_screenshot(f"./report/screenshots/{test_name}_{now}.png")

    def startVideoRecording(self):
        if appiumserver == 'local':
            if self.app == 'ios':
                Driver.driver.start_recording_screen(videoType="h264")
            else:
                Driver.driver.start_recording_screen()

    def endVideoRecording(self, test_name, bSave):
        if appiumserver == 'local':
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            if not os.path.exists('./report/videos'):
                os.makedirs('./report/videos')
            record = Driver.driver.stop_recording_screen()
            if bSave:
                filepath = os.path.join("./report/videos", test_name + "_" + now + ".mp4")
                with open(filepath, 'wb') as file:
                    file.write(base64.b64decode(record))
        elif appiumserver == 'browserstack':
            # retrieve the browser stack information to report/browserstacklog for further analyzing usage
            self.retrieveBrowserstackLog(test_name)

            # update the running status back to browserstack
            if bSave:
                message = "Case running fail"
            else:
                message = "Case running pass"
            self.updateBrowserstackStatus(bSave, message)

    @pytest.fixture(autouse=True)
    #def cli(self, app, device, appiumserver, os, env, get_logger):  # local
    def cli(self, apps, device, appiumserver, os, env, get_logger):
        #self.app = app  # local
        self.apps = apps  #BS
        self.device = device
        self.os = os
        self.logger = get_logger
        self.appiumserver = appiumserver
        self.env = env
        self.setUp()
        
