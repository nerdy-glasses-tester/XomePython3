from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _signin_link = (By.CSS_SELECTOR, "div.user-section>a.LinkButton.btn.btn-secondary")
    _login_iframe = (By.CLASS_NAME, "login-iframe")
    _email_field = (By.ID, "security_loginname")
    _password_field = (By.ID, "security_password")
    _login_btn = (By.ID, "submit-button")
    _loggedin_username = (By.CSS_SELECTOR, "div#uniqid-NavSubmenu-button-15>span.NavItem.top-level.user-menu>span")
    _signout_link = (By.XPATH, ".//a[@class='NavItem user-nav-item link' and contains(text(), 'Sign Out')]")
    _wrong_pwd_email_error = (By.XPATH, ".//div[@class='row-fluid errorMessageBox errorMessageBoxServerSide']/ul/li")
    _sign_in_header = (By.XPATH, ".//h2[contains(text(), 'Sign In')]")

    def clickSignInLink(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(LoginPage._signin_link))
        element = self.driver.find_element(*LoginPage._signin_link)
        element.click()
        wait.until(EC.element_to_be_clickable(LoginPage._login_iframe))
        frame = self.driver.find_element(*LoginPage._login_iframe)
        self.driver.switch_to.frame(frame)
        self.log.info("Click SignIn Link")

    def enterEmail(self, email):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(LoginPage._email_field))
        element = self.driver.find_element(*LoginPage._email_field)
        element.click()
        element.send_keys(email)
        self.log.info("Enter Email")

    def enterPassword(self, password):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(LoginPage._password_field))
        element = self.driver.find_element(*LoginPage._password_field)
        element.click()
        element.send_keys(password)
        self.log.info("Enter Password")

    def clickLoginButton(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(LoginPage._login_btn))
        element = self.driver.find_element(*LoginPage._login_btn)
        element.click()
        self.log.info("Click Login Button")

    def clearFields(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(LoginPage._email_field))
        emailField = self.driver.find_element(*LoginPage._email_field)
        emailField.clear()
        wait.until(EC.element_to_be_clickable(LoginPage._password_field))
        passwordField = self.driver.find_element(*LoginPage._password_field)
        passwordField.clear()
        self.log.info("Clear fields")

    def firstlogin(self, email, password, name):
        self.clickSignInLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.log.info("Just completed the first login")

    def login(self, email, password, name):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.log.info("Just completed the login method")
        time.sleep(3)

    def blankLogin(self):
        self.clickLoginButton()
        self.log.info("Just completed the blankLogin method")

    def wrongLogin(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.log.info("Just completed the wrongLogin method")

    def verifyWrongLogin(self, testbrowser=""):
        self.log.info("browser: "+testbrowser)
        if testbrowser =="safari":
            time.sleep(1)
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.presence_of_element_located(LoginPage._wrong_pwd_email_error))
        element = self.driver.find_element(*LoginPage._wrong_pwd_email_error)
        error = element.get_attribute("innerText")
        self.log.info("Error text found on page is: "+error)
        if error == "This combination of email or password is invalid.":
            self.log.info("TEST PASS: Verified error for wrong login. Oops, the e-mail or password doesn't match.")
            return True
        else:
            self.log.error("TEST FAIL: Failed to verify the error for wrong login - Oops, the e-mail or password doesn't match.")
            return False

    def verifyBlankLogin(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.presence_of_element_located(LoginPage._sign_in_header))
        signin_header = self.driver.find_element(*LoginPage._sign_in_header)
        if signin_header is not None:
            self.log.info("TEST PASS: Verified signin header is still present for blank login.")
            return True
        else:
            self.log.error("TEST FAIL: Did not find signin header. Can't confirm blank login did not allow you to login and still stay on signin screen.")
            return False

    def verifyLoginSuccessful(self, name):
        self.driver.switch_to.default_content()
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.presence_of_element_located(LoginPage._loggedin_username))
        element = self.driver.find_element(*LoginPage._loggedin_username)
        if element is not None:
            self.log.info("Element was found. Now getting its text.")
            username = element.text
            self.log.info("Username is "+username)
            self.log.info("***VERIFIED SUCCESSFUL LOGIN.***")
            print("Signed in Username: " + username.upper() +" Signed in Expected Username: "+name)
            return username.upper() == name
        else:
            self.log.error("***FAILED TO LOGIN. DID NOT FIND LOGGED IN USER.***")
            return False

    def logout(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.presence_of_element_located(LoginPage._loggedin_username))
        loginusername_element = self.driver.find_element(*LoginPage._loggedin_username)
        actions = ActionChains(self.driver)
        actions.move_to_element(loginusername_element).perform()
        wait.until(EC.element_to_be_clickable(LoginPage._signout_link))
        signout_element = self.driver.find_element(*LoginPage._signout_link)
        signout_element.click()
        self.log.info("Just completed the logout method")
        time.sleep(3)

    def verifyLogoutSuccessful(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                             )
        wait.until(EC.element_to_be_clickable(LoginPage._signin_link))
        element = self.driver.find_element(*LoginPage._signin_link)
        if element is not None:
            self.log.info("***SUCCESSFULLY LOGGED OUT.***")
            return True
        else:
            self.log.error("***FAILED TO LOG OUT.***")
            return False