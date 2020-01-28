from base.webdriverFactory import WebDriverFactory
from pages.webpages.search_page import SearchPage
from pages.webpages.morefilters_page import MoreFiltersPage
from pages.webpages.results_page import ResultsPage
from utilities.teststatus import TestStatus
from utilities.excel_utils import ExcelUtils
import unittest, pytest
import utilities.custom_logger as cl
import logging
import os
import time


@pytest.mark.usefixtures("setUp")
class FilterResultsBySqFeetTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    testName = ""

    @pytest.fixture(autouse=True)
    def classSetup(self, setUp):
        self.wdf = WebDriverFactory(self.browser, self.os)
        self.sp = SearchPage(self.driver)
        self.mfp = MoreFiltersPage(self.driver)
        self.rp = ResultsPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.excel = ExcelUtils(self.driver)

    def get_excel_data(self, testName):
        datafile = os.path.join('testdata/TestData.xlsx')
        data = self.excel.get_input_rows(datafile, testName)
        return data

    def test_filterResultsBySqFeet(self):
        self.log.info("++++++++++++++++++++++++++++++++++++STARTING test_loginSearch++++++++++++++++++++++++++++++++++++")
        testName = self._testMethodName
        self.log.info(testName)
        data = self.get_excel_data(testName)
        searchkeyword = data.get("searchkeyword")
        minsqft = data.get("minsqfeet")
        maxsqft = data.get("maxsqfeet")
        searchresult = self.sp.search(searchkeyword)
        self.mfp.filterBySqFt(minsqft, maxsqft)
        result = self.rp.verifySqFt(minsqft, maxsqft)
        self.ts.markFinal("test_filterResultsBySqFeet", result, "Verify can filter by sq feet.")
        self.log.info("++++++++++++++++++++++++++++++++++++ENDING test_loginSearch++++++++++++++++++++++++++++++++++++")

#pytest -s -v tests/webtests/filterResultsBySqFeet_test.py --browser chrome --os none --html=htmlreport.html