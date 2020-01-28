import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class ResultsPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _sqftresults = (By.XPATH, ".//span[contains(text(), 'sq. ft')]/preceding-sibling::span")

    def verifySqFt(self, minsqft, maxsqft):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5)
        wait.until(EC.presence_of_all_elements_located(ResultsPage._sqftresults))
        sqftresults = self.driver.find_elements(*ResultsPage._sqftresults)
        sqftresult1  = int(sqftresults[0].text.replace(",", ""))
        sqftresult2 = int(sqftresults[1].text.replace(",", ""))
        sqftresult3 = int(sqftresults[2].text.replace(",", ""))
        if minsqft <= sqftresult1 <= maxsqft and minsqft <= sqftresult2 <= maxsqft and minsqft <= sqftresult3 <= maxsqft:
            return True
        else:
            return False

