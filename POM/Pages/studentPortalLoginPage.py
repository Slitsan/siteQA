from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class StudentPortal():

    def __init__(self, drive: WebDriver):
        self.driver = drive
        self.username_textbox_ID = 'mat-input-0'
        self.password_textbox_ID = 'mat-input-1'
        self.loginBtn_TXT = 'Login'
        print('-----  End of INIT  StudentPortal  -----')

    def enterUserName(self, username):
        self.driver.find_element(By.ID, self.username_textbox_ID).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.ID, self.password_textbox_ID).send_keys(password)

    def logIn(self):
        self.driver.find_element(By.LINK_TEXT, self.loginBtn_TXT).click()