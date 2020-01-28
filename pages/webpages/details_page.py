import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class DetailsPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _yearbuilt = (By.CSS_SELECTOR, "div#mls-yr2>span")

    def verifyYear(self, minyear, maxyear):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5)
        wait.until(EC.presence_of_element_located(DetailsPage._yearbuilt))
        morefilters = self.driver.find_element(*DetailsPage._yearbuilt)
        year = int(morefilters.text)
        if minyear<=year<=maxyear:
            return True
        else:
            return False

