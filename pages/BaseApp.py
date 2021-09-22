
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logger import logger
from settings import GO_TO_SITE

log = logger.get_logger(__name__)


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = GO_TO_SITE

    def find_element(self, locator, time=120):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=120):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        log.info("go to site")
        self.driver.get(self.base_url)
        self.driver.set_window_size(1920, 1080)

    def go_to_custom_url(self, custom):
        log.info("go to site")
        return self.driver.get(custom)

    def ajax(self):
        WebDriverWait(self.driver, 120).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete')

    def ajaxBack(self):
        # WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "subscription-status")))
        WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@ng-controller='SubscribersCtrl']")))
        # time.sleep(10);

    def scroll_shim(self, object):
        x = object.location['x']
        y = object.location['y']
        scroll_by_coord = 'window.scrollTo(%s,%s);' % (
            x,
            y
        )
        scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
        self.driver.execute_script(scroll_by_coord)
        self.driver.execute_script(scroll_nav_out_of_way)
        pass

    def hover(self, xpath):
        if 'firefox' in self.driver.capabilities['browserName']:
            self.scroll_shim(self.driver.find_element_by_xpath(xpath))
        element_to_hover_over = self.driver.find_element_by_xpath(xpath)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        pass