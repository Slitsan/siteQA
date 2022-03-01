#        28_2_2022
#      created by Dima
#   Header test
# --------------------------------------------------------------------------------------
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from POM.Pages.header import Header
from POM.Pages.studentPortalLoginPage import StudentPortal

# -------------------------------------
correctUserName = 'dagula74@yahoo.com'
correctPassword = '310870969'
studentPortalTitle = 'Students Portal RT-ED'
popUp_close_XPATH = '//*[@id="lead-form-modal1"]/span'
#


class HeaderTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver: WebDriver = webdriver.Chrome(
            'C:\\Users\\Dima\\Documents\\PROJECTs\\siteQA\\drivers\\chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        cls.driver.set_page_load_timeout(30)
        cls.driver.get('https://rt-ed.co.il/')
        time.sleep(17)
        cls.driver.find_element(By.XPATH, popUp_close_XPATH).click()


    def test_legalEnter_studentPortal_fromHeader(self):
        header = Header(self.driver)
        titleStr = header.goToStudentPortal()
        time.sleep(4)
        print('-----  TITLE     -----' + titleStr)
        if titleStr == studentPortalTitle:
            stPortal = StudentPortal(self.driver)
            stPortal.enterUserName(correctUserName)
            stPortal.enterPassword(correctPassword)
            stPortal.logIn()
        else:
            print('-----  WRONG StPortal TITle     -----')


