from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _searchfield = (By.ID, "homepage-search-field")
    _searchbtn = (By.CSS_SELECTOR, "button.call-to-action.search-field-button")
    _searchresultsaddresses = (By.CSS_SELECTOR, "h1.address-line-1")

    def search(self, searchkeyword):

        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(SearchPage._searchfield))
        element = self.driver.find_element(*SearchPage._searchfield)
        element.send_keys(searchkeyword)
        self.log.info("Enter search keyword")
        wait.until(EC.element_to_be_clickable(SearchPage._searchbtn))
        button = self.driver.find_element(*SearchPage._searchbtn)
        button.click()
        time.sleep(3)
        wait.until(EC.presence_of_all_elements_located(SearchPage._searchresultsaddresses))
        searchresults = self.driver.find_elements(*SearchPage._searchresultsaddresses)
        size = len(searchresults)
        if size > 0:
            return True
        else:
            return False





