from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.select import Select
import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class MoreFiltersPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _morefilters = (By.CSS_SELECTOR, "div#ddbtn-label-filters>span.dd-info")
    _openminsqft = (By.CSS_SELECTOR, "button[data-id='filters-sqftmin']")
    _openmaxsqft = (By.CSS_SELECTOR, "button[data-id='filters-sqftmax']")
    _openminyear = (By.CSS_SELECTOR, "button[data-id='filters-minyearbuilt']")
    _openmaxyear = (By.CSS_SELECTOR, "button[data-id='filters-maxyearbuilt']")
    _applyfiltersbtn = (By.CSS_SELECTOR, "button#filters-submit>span#desktop-apply")

    def clickMoreFilters(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MoreFiltersPage._morefilters))
        morefilters = self.driver.find_element(*MoreFiltersPage._morefilters)
        morefilters.click()

    def filterByYear(self, minyear, maxyear):
        MoreFiltersPage.clickMoreFilters(self)
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MoreFiltersPage._openminyear))
        openminyear = self.driver.find_element(*MoreFiltersPage._openminyear)
        openminyear.click()

        minyearelement = self.driver.find_element(By.XPATH, ".//select[@id='filters-minyearbuilt']/option[@value='%s']"%minyear)
        minyearelement.click()
        time.sleep(2)

        wait.until(EC.element_to_be_clickable(MoreFiltersPage._openmaxyear))
        openmaxyear = self.driver.find_element(*MoreFiltersPage._openmaxyear)
        openmaxyear.click()

        maxyearelement = self.driver.find_element(By.XPATH, ".//select[@id='filters-maxyearbuilt']/option[@value='%s']"%maxyear)
        maxyearelement.click()
        time.sleep(2)

        wait.until(EC.element_to_be_clickable(MoreFiltersPage._applyfiltersbtn))
        applybtn = self.driver.find_element(*MoreFiltersPage._applyfiltersbtn)
        applybtn.click()
        time.sleep(2)

    def filterBySqFt(self, minsqft, maxsqft):
        MoreFiltersPage.clickMoreFilters(self)
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MoreFiltersPage._openminsqft))
        openminsqft = self.driver.find_element(*MoreFiltersPage._openminsqft)
        openminsqft.click()

        minsqftelement = self.driver.find_element(By.XPATH, ".//select[@id='filters-sqftmin']/option[@value='%s']"%minsqft)
        minsqftelement.click()
        time.sleep(2)
        #wait.until(EC.element_to_be_clickable(MoreFiltersPage._minsqftdrpdown))
        #select = Select(self.driver.find_element(*MoreFiltersPage._minsqftdrpdown))
        #select.select_by_value(minsqft)

        wait.until(EC.element_to_be_clickable(MoreFiltersPage._openmaxsqft))
        openmaxsqft = self.driver.find_element(*MoreFiltersPage._openmaxsqft)
        openmaxsqft.click()

        maxsqftelement = self.driver.find_element(By.XPATH, ".//select[@id='filters-sqftmax']/option[@value='%s']"%maxsqft)
        maxsqftelement.click()
        time.sleep(2)
        #wait.until(EC.element_to_be_clickable(MoreFiltersPage._maxsqftdrpdown))
        #select = Select(self.driver.find_element(*MoreFiltersPage._maxsqftdrpdown))
        #select.select_by_value(maxsqft)

        wait.until(EC.element_to_be_clickable(MoreFiltersPage._applyfiltersbtn))
        applybtn = self.driver.find_element(*MoreFiltersPage._applyfiltersbtn)
        applybtn.click()
        time.sleep(2)