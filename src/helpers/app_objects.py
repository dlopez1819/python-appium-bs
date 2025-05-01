from selenium.webdriver.support.wait import WebDriverWait
from src.helpers.appium_driver import Driver
from selenium.webdriver.common.action_chains import ActionChains
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time
import base64

def keyword_check(kwargs):
    kc = {}
    if 'index' in kwargs: kc['index'] = 'elements'
    if 'index' not in kwargs: kc['index'] = 'element'
    return ''.join(kc.values())


class BoH(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def element(self, locator, parent_element=None, n=1):
        x = iter(CustomCall())
        while n > 0:
            try:
                BoH.wait_until_appear(self, locator)
                if parent_element:
                    return parent_element.find_element(*locator)
                else:
                    return self.driver.find_element(*locator)
            except Exception as e:
                self.logger.error(f"element failed attempt {next(x)} - {locator}")
                n -= 1
                if n == 0:
                    #self.logger.error("Current page source is: %s" % str(self.driver.page_source))
                    raise NoSuchElementException("Could not locate element with value: %s" % str(locator))

    def elements(self, locator, parent_element=None, n=1):
        wait = WebDriverWait(self.driver, 2)

        x = iter(CustomCall())
        while n > 0:
            try:
                wait.until(EC.visibility_of_any_elements_located(locator))
                if parent_element:
                    return parent_element.find_elements(*locator)
                else:
                    return self.driver.find_elements(*locator)

            except Exception as e:
                self.logger.error(f"element list failed attempt {next(x)} - {locator}")
                n -= 1
                if n == 0:
                    #self.logger.error("Current page source is: %s" % str(self.driver.page_source))
                    raise NoSuchElementException("Could not locate element list with value: %s" % str(locator))

    def is_displayed(self, locator, expected=True, n=1, **kwargs):
        wait = WebDriverWait(self.driver, 2)

        x = iter(CustomCall())
        while n > 0:
            try:
                if len(kwargs) == 0:
                    BoH.wait_until_appear(self, locator)
                    assert BoH.element(self, locator).is_displayed() == expected, \
                                                                     f'The is_displayed does not match for : {locator}.'\
                                                                     f'Expected: {expected}' \
                                                                     f'Current:{BoH.element(self, locator).is_displayed()}'
                else:
                    isdisplayed = BoH.elements(self, locator)[kwargs['index']].is_displayed()
                    assert BoH.elements(self, locator)[kwargs['index']].is_displayed() == expected, \
                                                                    f'The is_displayed does not match for : {locator}.'\
                                                                    f'Expected: {expected}' \
                                                                    f'Current:{isdisplayed}'
                break
            except Exception as e:
                print(f'is_displayed failed attempt {next(x)}- {locator}')
                self.logger.error(f'is_displayed failed attempt {next(x)}- {locator}')
                time.sleep(0.5)
                n -= 1
                if len(kwargs) == 0:
                    if n == 0:
                        assert BoH.element(self, locator).is_displayed() == expected, \
                                                            f'The is_displayed does not match for : {locator}.' \
                                                            f'Expected: {expected}' \
                                                            f'Current:{BoH.element(self, locator).is_displayed()}'
                else:
                    if n == 0:
                        isdisplayed = BoH.elements(self, locator)[kwargs['index']].is_displayed()
                        assert BoH.elements(self, locator)[kwargs['index']].is_displayed() == expected, \
                                                            f'The is_displayed does not match for : {locator}.' \
                                                            f'Expected: {expected}' \
                                                            f'Current:{isdisplayed}'

    def is_exist(self, locator, expected=True, n=1, **kwargs):
        while n > 0:
            try:
                if len(kwargs) == 0 and BoH.element(self, locator).is_displayed() == expected:
                    return True
                elif BoH.elements(self, locator)[kwargs['index']].is_displayed() == expected:
                    return True

            except Exception as e:
                n -= 1
                if n == 0: return False

    def tap(self, locator, **kwargs):
        BoH.is_displayed(self, locator, True, **kwargs)

        actions = ActionChains(self.driver)
        return {
            'element': lambda x: actions.tap(BoH.element(self, locator)).perform(),
            'elements': lambda x: actions.tap(BoH.elements(self, locator)[kwargs['index']]).perform()
        }[keyword_check(kwargs)]('x')

    def longpress_by_coordinate(self, x, y, duration = 2000):
        action = ActionChains(self.driver)
        action.w3c_actions.long_press(x=x, y=y, duration=duration).release().perform()

    def double_tap(self, locator, n=1, **kwargs):
        BoH.is_displayed(self, locator, True, n=n, **kwargs)
        actions = ActionChains(self.driver)
        return {
            'element': lambda x: actions.click(BoH.element(self, locator), count=2).perform(),
            'elements': lambda x: actions.click(BoH.elements(self, locator)[kwargs['index']], count=2).perform()
        }[keyword_check(kwargs)]('x')

    def click(self, locator, n=3, **kwargs):
        time.sleep(1)
        BoH.is_displayed(self, locator, True, n=n, **kwargs)

        return {
            'element': lambda x: BoH.element(self, locator).click(),
            'elements': lambda x: BoH.elements(self, locator)[kwargs['index']].click()
        }[keyword_check(kwargs)]('x')

    def wait_until_disappear(self, locator, timeout=2):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.invisibility_of_element_located(locator), f'Element not disappear {locator}')
        except Exception as e:
            print(f'Element not disappear {locator}')
            self.logger.error(f'Element not disappear {locator}')

    def wait_until_appear(self, locator, timeout=2):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator), f'Element not appear {locator}')
        except Exception as e:
            print(f'Element not appear {locator}')
            self.logger.error(f'Element not appear {locator}')

    def send_keys(self, locator, text='', bcheckinput=True, **kwargs):
        n = 3
        bsuccess = False
        while n > 1 and bsuccess == False:
            try:
                BoH.is_displayed(self, locator, True, **kwargs)
                action = {
                'element': lambda text: BoH.element(self, locator).clear() and BoH.element(self, locator).send_keys(text),
                }[keyword_check(kwargs)](text)

                if bcheckinput:
                    if len(kwargs) == 0:
                        if BoH.element(self, locator).text == text:
                            bsuccess = True
                            break
                    else:
                        if BoH.elements(self, locator)[kwargs['index']].text == text:
                            bsuccess = True
                            break
                else:
                    bsuccess = True
                    break
                n -= 1
            except Exception as e:
                print(f'Element sendkeys fail for {locator}')
                self.logger.error(f'Element sendkeys fail for {locator}')
                n -= 1
                if n == 1: bsuccess = False

    def get_screen_size(self):
        return self.driver.get_window_size()

    def back(self):
        self.driver.back()

    def close(self):
        self.driver.close_app()

    def reset(self):
        self.driver.reset()

    def launch_app(self):
        self.driver.launch_app()

    def install_app(self, path):
        self.driver.install_app(path)

    def activate_app(self, app_package):
        self.driver.activate_app(app_package)

    def remove_app(self, app_package):
        self.driver.remove_app(app_package)

    def terminate_app(self, app_package):
        self.driver.terminate_app(app_package)

    def start_activity(self, app_package, app_activity):
        try:
            self.driver.start_activity(app_package, app_activity)
        except Exception as e:
            self.logger.error(f"app_activity not found  - {app_package} and/ or  attribute not found {app_activity}")

    def swipe(self, start, dest):
        if type(start[1]) is not int:
            source_element = BoH.element(self, start)
        else:
            source_element = BoH.elements(self, start[0])[int(start[1])]

        if type(dest[1]) is not int:
            target_element = BoH.element(self, dest)
        else:
            target_element = BoH.elements(self, dest[0])[int(dest[1])]

        self.driver.scroll(source_element, target_element)

    def tap_by_coordinates(self, x, y, element=None, wait_time=0):
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(wait_time)

    def double_tap_by_coordinates(self, x, y):
        time.sleep(1)
        actions = ActionChains(self.driver)
        actions.press(x=x, y=y).wait(50).release().perform().press(x=x, y=y).release().perform()

    def get_list_elements(self, locator):
        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(EC.visibility_of_any_elements_located(locator))
            return self.driver.find_elements(*locator)
        except Exception as e:
            self.logger.error(f"element not found  - {locator}")

    def move_to_element(self, source):
        actions = ActionChains(self.driver)
        actions.move_to_element(source).release().perform()

    def scroll_by_coordinates(self, x, y, x1, y1):
        try:
            BoH.move_to_coordinates(self, x, y, x1, y1)
        except Exception as e:
            self.logger.error(f"coordinates not found - {x}{y}")

    def get_attribute(self, locator, attribute):
        _attribute = None
        try:
            _attribute = self.driver.find_element(*locator).get_attribute(attribute)
            return _attribute
        except Exception as e:
            self.logger.error(f"element not found  - {locator} and/ or  attribute not found {attribute}")

    def press_key_code(self, code):
        try:
            self.driver.press_keycode(code)
        except Exception as e:
            self.logger.error(f"keycode not found  - {code}")

    def hideKeyboard(self, locator, x, y):
        if BoH.is_exist(self, locator, True):
            BoH.tap_by_coordinates(self, x, y)

    def get_device_orientation(self):
        try:
            return self.driver.orientation
        except Exception as e:
            self.logger.error(f"unable to get device orientation")

    def get_screen_dimension(self):
        width = BoH.get_screen_size(self)['width']
        height = BoH.get_screen_size(self)['height']
        return  width , height

    def set_device_orientation(self, orientation):
        try:
            self.driver.orientation = orientation
        except Exception as e:
            self.logger.error(f"unable to set device orientation")

    def background_app(self, timeout):
        try:
            time.sleep(1)
            return self.driver.background_app(timeout)
        except Exception as e:
            self.logger.error(f"bundle id app not recognized")

    def get_session_capabilities(self):
        try:
            return self.driver.capabilities
        except Exception as e:
            self.logger.error(f"capability not found")

    def swipe_by_coordinates(self, start_x, start_y, end_x, end_y, duration):
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def get_element_location(self, locator):
        return BoH.element(self, locator, n= 1).location

    # need refactor on condition
    def assert_text(self, locator, text, n=20, **kwargs):
        BoH.is_displayed(self, locator, True)

        x = iter(CustomCall())
        while n > 1:
            try:
                if len(kwargs) == 0:
                    assert BoH.element(self, locator).text == text, f'The assert_text does not match for : {locator}.'\
                                                                     f'Expected: {text}' \
                                                                     f'Current:{BoH.element(self, locator).text}'
                else:
                    element_text = BoH.elements(self, locator)[kwargs['index']].text
                    assert element_text == text, f'The assert_text does not match for : {locator}.'\
                                                 f'Expected: {text}' \
                                                 f'Current:{element_text}'
                break
            except Exception as e:
                self.logger.error(f'assert_text failed attempt {next(x)}- {locator}')
                time.sleep(0.5)
                n -= 1
                if len(kwargs) == 0:
                    if n == 1:
                        assert BoH.element(self, locator).text == text, f'The assert_text does not match for : {locator}.'\
                                                                     f'Expected: {text}' \
                                                                     f'Current:{BoH.element(self, locator).text}'
                else:
                    if n == 1:
                        element_text = BoH.elements(self, locator)[kwargs['index']].text
                        assert element_text == text, f'The assert_text does not match for : {locator}.'\
                                                     f'Expected: {text}' \
                                                     f'Current:{element_text}'

    def assert_size(self, locator, param):
        BoH.is_displayed(self, locator, True, index=0)

        case = param.rsplit(None, 1)[0]
        value = int(param.rsplit(None, 1)[1])

        if case in ['more than', 'greater than', 'above', '>']:
            assert BoH.elements(self, locator).__len__() > value, f'The assert_size does not match for : {locator}.'\
                                                     f'Expected: {BoH.elements(self, locator).__len__()}' \
                                                     f'Case: {case}' \
                                                     f'Value:{value}'
        elif case in ['less than', 'below', '<']:
            assert BoH.elements(self, locator).__len__() < value, f'The assert_size does not match for : {locator}.'\
                                                     f'Expected: {BoH.elements(self, locator).__len__()}' \
                                                     f'Case: {case}' \
                                                     f'Value:{value}'
        elif case in ['equal to', '==']:
            assert BoH.elements(self, locator).__len__() == value, f'The assert_size does not match for : {locator}.'\
                                                     f'Expected: {BoH.elements(self, locator).__len__()}' \
                                                     f'Case: {case}' \
                                                     f'Value:{value}'

    def swipe_until(self, locator, start_x=100, start_y=200, end_x=0, end_y=0, duration=0, count=10):
        self.driver.implicitly_wait(0.5)  # waits half a second
        if locator:
            for i in range(count):
                try:
                    BoH.element(self, locator).is_displayed()
                    break
                except Exception as e:
                    self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        else:
            time.sleep(2)
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        self.driver.implicitly_wait(5)  # waits 5 seconds

    def assert_equal(self, actual, expected, n=5):
        x = iter(CustomCall())
        while n > 1:
            try:
                assert actual == expected, f'The assert_equal does not match.'\
                                                     f'Expected: {expected}' \
                                                     f'Current:{actual}'
                break
            except Exception as e:
                self.logger.error(f"assert equal attempt {next(x)} - {actual} not matching {expected}")
                time.sleep(2)
                n -= 1
                if n == 1: assert actual == expected, f'The assert_equal does not match.'\
                                                      f'Expected: {expected}' \
                                                      f'Current:{actual}'

    def assert_equal_ab(self, actual, expected_a, expected_b, n=5):
        x = iter(CustomCall())
        while n > 1:
            try:
                try:
                    assert actual == expected_a, f'The assert_equal_ab does not match for a.'\
                                                      f'Expected a: {expected_a}' \
                                                      f'Current:{actual}'
                except Exception as e:
                    assert actual == expected_b, f'The assert_equal_ab does not match for b.'\
                                                      f'Expected b: {expected_b}' \
                                                      f'Current:{actual}'
                break
            except Exception as e:
                self.logger.error(f"assert equal attempt {next(x)} - {actual} not matching {expected_a} or {expected_b}")
                time.sleep(2)
                n -= 1
                if n == 1: assert actual == expected_a, f'The assert_equal_ab does not match for a.'\
                                                        f'Expected a: {expected_a}' \
                                                        f'Current:{actual}'

    def is_small_screen(self):
        width = BoH.get_screen_size(self)['width']
        height = BoH.get_screen_size(self)['height']
        square = width * height
        if self.apps == 'android':
            if square < 2266 * 1488:
                return True
            else:
                return False
        else:
            if square < 768 * 1026:
                return True
            else:
                return False

    @staticmethod
    def assert_boolean(actual, expected=True):
        assert actual == expected, f'The assert_boolean does not match.'\
                                                      f'Expected b: {expected}' \
                                                      f'Current:{actual}'

    def key_code_convert(self, num):

        ascii_1 = ord('1')
        ascii_a = ord('a')
        ascii_char = ord(num)
        if num.isdigit():
            return ascii_char-ascii_1+8
        elif num.isalpha():
            low_char = ord(num.lower())
            if ascii_char >= 97:
                # return key_code of lowercase letters
                return low_char-ascii_a+29
            else:
                # return key_code of capital letter
                key_code = (low_char-ascii_a+29, 64, 59)
                return key_code
        else:
            other_char_dict = {
                '@': 77, '.': 158
            }
            return other_char_dict[num]

    def set_orientation(self, orient):
        self.driver.orientation = orient

class CustomCall:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        k = self.a
        self.a += 1
        return k