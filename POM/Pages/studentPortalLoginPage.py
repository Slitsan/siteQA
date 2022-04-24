from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class StudentPortal():

    def __init__(self, drive: WebDriver):
        self.driver = drive
        self.pageUrl = 'https://rt-crm.com/portal/#/login'
        self.username_textbox_ID = 'mat-input-0'
        self.password_textbox_ID = 'mat-input-1'
        # self.loginBtn_TXT = 'Login'
        # self.loginBTN_Attribute = 'div[class ="mat-ripple mat-button-ripple"]'
        self.loginBTN_XPATH = '/html/body/app-root/div[1]/div[2]/login-cmp/div/div/div/div/div/div[2]/button'
        self.driver.get(self.pageUrl)
        print('-----  End of INIT  StudentPortal  -----')

    def enterUserName(self, username):
        self.driver.find_element(By.ID, self.username_textbox_ID).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.ID, self.password_textbox_ID).send_keys(password)

    def logIn(self):
        self.driver.find_element(By.XPATH, self.loginBTN_XPATH).click()
