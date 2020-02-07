import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException, \
    ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy

class MLoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    pkgresrid= "com.xome.android:id"
    pkgresridandroid="android:id"
    _permission_at_startup= (MobileBy.ID,"com.android.packageinstaller:id/permission_allow_button")
    #_permission_at_startup=".//android.widget.Button[contains(text(), 'ALLOW')]"
    _hamburger_icon = (MobileBy.CLASS_NAME, "android.widget.ImageButton")
    _sign_in= (MobileBy.ID, pkgresrid+"/cont_title") #has text SIGN IN
    _email_field= (MobileBy.ID, pkgresrid+"/edittext_login_email")
    _password_field= (MobileBy.ID, pkgresrid+"/textview_login_password")
    _login_btn= (MobileBy.ID, pkgresrid+"/button_login") #has text Sign In
    _closesigninbox = (MobileBy.XPATH, ".//android.widget.LinearLayout[@resource-id='com.xome.android:id/root_layout']/android.view.ViewGroup/android.widget.ImageButton[@index='0']")
    _searchbox = (MobileBy.ID, pkgresrid+"/tvSearch")

    _myxomeheader= (MobileBy.XPATH, ".//*[@resource-id='com.xome.android:id/cont_title' and @index='0' and @text='MY XOME']")
    _welcomeusertext = (MobileBy.XPATH, ".//android.widget.TextView[@resource-id='com.xome.android:id/cont_title' and @index='0' and @text='Welcome Automation']")

    _myxomesignout= (MobileBy.ID, pkgresrid+"/nav_sign_out") #has text Sign Out
    _signout_popup= (MobileBy.ID, pkgresridandroid+"/button1") #has text YES

    _error_msg= (MobileBy.ID, pkgresridandroid+"/alertTitle") #has text Error Message
    _emailreq_msg= (MobileBy.ID, pkgresridandroid+"/message") #has text email is required
    _error_ok_btn= (MobileBy.ID, pkgresridandroid+"/button1") #has text OK

    #_error_msg= (MobileBy.ID, pkgresridandroid+"/alertTitle") #has text Error Message #same as above
    _invalidcreds_msg= (MobileBy.ID, pkgresridandroid+"/message") #has text Invalid credentials provided
    #_error_ok_btn= (MobileBy.ID, pkgresridandroid+"/button1") #has text OK #same as above



    def clickPermissionAtStartup(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MLoginPage._permission_at_startup))
        element=self.driver.find_element(*MLoginPage._permission_at_startup)
        element.click()

    def clickHamburgerMenu(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MLoginPage._hamburger_icon))
        element = self.driver.find_element(*MLoginPage._hamburger_icon)
        element.click()
        self.log.info("Click hamburger menu")

    def clickSignIn(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MLoginPage._sign_in))
        element = self.driver.find_element(*MLoginPage._sign_in)
        element.click()
        time.sleep(3)
        self.log.info("Click sign in")

    def enterEmail(self, email):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MLoginPage._email_field))
        element = self.driver.find_element(*MLoginPage._email_field)
        element.send_keys(email)
        self.log.info("Enter email")

    def enterPassword(self, password):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MLoginPage._password_field))
        element = self.driver.find_element(*MLoginPage._password_field)
        element.send_keys(password)
        self.log.info("Enter password")

    def clickLoginButton(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MLoginPage._login_btn))
        element = self.driver.find_element(*MLoginPage._login_btn)
        element.click()
        self.log.info("Click login button")

    def clearFields(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MLoginPage._email_field))
        emailField = self.driver.find_element(*MLoginPage._email_field)
        emailField.clear()
        wait.until(EC.element_to_be_clickable(MLoginPage._password_field))
        passwordField = self.driver.find_element(*MLoginPage._password_field)
        passwordField.clear()
        self.log.info("Clear fields")

    def closeSignInfBox(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MLoginPage._closesigninbox))
        closesigninbox = self.driver.find_element(*MLoginPage._closesigninbox)
        closesigninbox.click()
        self.log.info("Closed signin box.")

    def dismissMenuByClickingSearchbox(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MLoginPage._searchbox))
        element = self.driver.find_element(*MLoginPage._searchbox)
        element.click()
        self.log.info("Dismiss menu by clicking on search box")

    def clickMyXomeHeader(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MLoginPage._myxomeheader))
        myxomeheader = self.driver.find_element(*MLoginPage._myxomeheader)
        myxomeheader.click()
        time.sleep(2)
        self.log.info("Open MyXome header")

    def firstlogin(self, email, password, name):
        self.clickHamburgerMenu()
        self.clickSignIn()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(3)
        self.log.info("Completed Login")

    def login(self, email, password, name):
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(3)
        self.log.info("Completed Login")

    def blankLogin(self):
        self.clickHamburgerMenu()
        self.clickSignIn()
        self.clickLoginButton()
        self.log.info("Just completed the blankLogin method")

    def wrongLogin(self, email="", password=""):
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.log.info("Just completed the wrongLogin method")
        time.sleep(3)

    def verifyLoginSuccessful(self, name):
        self.clickHamburgerMenu()
        time.sleep(3)
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MLoginPage._welcomeusertext))
        element = self.driver.find_element(*MLoginPage._welcomeusertext)
        self.log.info("Found welcomeusertext element.")
        result = element.text
        self.log.info("Welcome user text is: "+result)
        if result==name:
            self.log.info("***VERIFIED SUCCESSFUL LOGIN.***")
            return True
        else:
            self.log.error("***FAILED TO LOGIN. DID NOT FIND WELCOME USER TEXT.***")
            return False

    def verifyBlankLogin(self):
        error = self.driver.switch_to.alert
        element = error.text
        self.log.info("errormsg is: "+element)
        error.accept()
        time.sleep(2)
        if "email is required" in element:
            self.log.info("TEST PASS: Verified email is required error.")
            return True
        else:
            self.log.error(
                "TEST FAIL: Can't find email is required error message.")
            return False

    def verifyWrongLogin(self):
        error = self.driver.switch_to.alert
        element = error.text
        self.log.info("errormsg is: "+element)
        error.accept()
        time.sleep(3)
        if "Sign In Failed" in element:
            self.log.info("TEST PASS: Verified invalid credentials provided error.")
            return True
        else:
            self.log.error("TEST FAIL: Can't find invalid credentials provided error message.")
            return False

    def logout(self):
        self.clickHamburgerMenu()
        self.clickMyXomeHeader()
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MLoginPage._myxomesignout))
        myxomesignout = self.driver.find_element(*MLoginPage._myxomesignout)
        myxomesignout.click()
        time.sleep(2)
        wait.until(EC.element_to_be_clickable(MLoginPage._signout_popup))
        signoutpopup = self.driver.find_element(*MLoginPage._signout_popup)
        signoutpopup.click()
        time.sleep(3)

    def verifyLogoutSuccessful(self):
        self.clickHamburgerMenu()
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(MLoginPage._sign_in))
        element = self.driver.find_element(*MLoginPage._sign_in)
        self.log.info("Found signin element after signed out.")
        if element is not None:
            self.log.info("***SUCCESSFULLY LOGGED OUT.***")
            return True
        else:
            self.log.error("***FAILED TO LOG OUT.***")
            return False