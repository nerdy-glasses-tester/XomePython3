from base.webdriverFactory import WebDriverFactory
from pages.webpages.search_page import SearchPage
from pages.webpages.morefilters_page import MoreFiltersPage
from pages.webpages.results_page import ResultsPage
from pages.webpages.details_page import DetailsPage
from utilities.teststatus import TestStatus
from utilities.excel_utils import ExcelUtils
import unittest, pytest
import utilities.custom_logger as cl
import logging
import os
import time


@pytest.mark.usefixtures("setUp")
class FilterResultsByYearTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    testName = ""

    @pytest.fixture(autouse=True)
    def classSetup(self, setUp):
        self.wdf = WebDriverFactory(self.browser, self.os)
        self.sp = SearchPage(self.driver)
        self.mfp = MoreFiltersPage(self.driver)
        self.rp = ResultsPage(self.driver)
        self.dp = DetailsPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.excel = ExcelUtils(self.driver)

    def get_excel_data(self, testName):
        datafile = os.path.join('testdata/TestData.xlsx')
        data = self.excel.get_input_rows(datafile, testName)
        return data

    def test_filterResultsByYear(self):
        self.log.info("++++++++++++++++++++++++++++++++++++STARTING test_loginSearch++++++++++++++++++++++++++++++++++++")
        testName = self._testMethodName
        self.log.info(testName)
        data = self.get_excel_data(testName)
        searchkeyword = data.get("searchkeyword")
        minyear = data.get("minyear")
        maxyear = data.get("maxyear")
        searchresult = self.sp.search(searchkeyword)
        self.mfp.filterByYear(minyear, maxyear)
        self.rp.click1stimage()
        result = self.dp.verifyYear(minyear, maxyear)
        self.ts.markFinal("test_filterResultsBySqFeet", result, "Verify can filter by sq feet.")
        self.log.info("++++++++++++++++++++++++++++++++++++ENDING test_loginSearch++++++++++++++++++++++++++++++++++++")

#pytest -s -v tests/webtests/filterResultsByYear_test.py --browser chrome --os none --html=htmlreport.html