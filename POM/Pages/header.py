import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys


class Header():

    def __init__(self, drive: WebDriver):
        self.driver = drive

        self.popUp_close_xpath = '//*[@id="lead-form-modal1"]/span'
        self.studentPortal_id = 'student-portal'
        self.search_textbox_id = 'nav-search-string'
        self.search_btn_class = 'btn btn-outline-light order-2 my-2 my-sm-0 col-3'

        self.maslulim_byTXT = 'מסלולים'
        self.courses_byTXT = 'קורסים'
        self.companiesTXT = 'קורסים לחברות'

    def goToMaslul(self, name):
        self.driver.find_element(By.LINK_TEXT, self.maslulim_byTXT).click()

    def goToStudentPortal(self) -> str:
        self.driver.find_element(By.ID, self.studentPortal_id).click()
        self.driver.get('https://rt-crm.com/portal/#/login')
        return self.driver.title
