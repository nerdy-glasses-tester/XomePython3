from base.webdriverFactory import WebDriverFactory
from pages.webpages.login.login_page import LoginPage
from pages.webpages.search_page import SearchPage
from utilities.teststatus import TestStatus
from utilities.excel_utils import ExcelUtils
import unittest, pytest
import utilities.custom_logger as cl
import logging
import os
import time

@pytest.mark.usefixtures("setUp")
class SearchTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    testName = ""

    @pytest.fixture(autouse=True)
    def classSetup(self, setUp):
        self.wdf = WebDriverFactory(self.browser, self.os)
        self.lp = LoginPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.excel = ExcelUtils(self.driver)

    def get_excel_data(self, testName):
        datafile = os.path.join('testdata/TestData.xlsx')
        data = self.excel.get_input_rows(datafile, testName)
        return data

    def test_loginSearch(self):
        self.log.info("++++++++++++++++++++++++++++++++++++STARTING test_loginSearch++++++++++++++++++++++++++++++++++++")
        testName = self._testMethodName
        self.log.info(testName)
        data = self.get_excel_data(testName)
        email = data.get("email")
        password = data.get("password")
        name = data.get("name")
        searchkeyword = data.get("searchkeyword")
        self.lp.clickSignInLink()
        self.lp.login(email, password, name)
        result = self.lp.verifyLoginSuccessful(name)
        assert result == True
        time.sleep(5)
        size = self.sp.search(searchkeyword)
        assert size > 0


        self.ts.markFinal("test_loginSearch", result, "Verify can search after login.")
        self.log.info("++++++++++++++++++++++++++++++++++++ENDING test_loginSearch++++++++++++++++++++++++++++++++++++")

#pytest -s -v tests/webtests/search_test.py --browser chrome --os none --html=htmlreport.html