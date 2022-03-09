#   09/03/2022
#   Created By Pablik
#   Maslul Page Test
# -----------------------------------------------------
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from POM.Pages.header import Header
from datetime import datetime

# --------------------------------------------
from POM.Pages.maslul_page import MaslulPage


class MaslulPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver: WebDriver = webdriver.Chrome(executable_path=
                                                 'C:\\Users\Public\\Documents\\GitHub Projects\\Python\\siteQA\\drivers\\chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(20)
        cls.driver.set_page_load_timeout(30)
        cls.driver.get('https://rt-ed.co.il/')
        now = datetime.now()
        current_time = now.strftime("%d%m%H%M%S")
        cls.date_for_log = now.strftime("%d %m %Y")
        cls.test_user_last_name = "test"
        cls.test_user_first_name = "test"
        cls.test_user_mail = current_time + "@test.com"
        cls.test_user_phone_number = current_time
        cls.string_result = "-----------------------------------TESTING SYLLABUS-----------------------------------------------\n"

    def compare_title_pages(self, title: str, actual_page_title: str, button_name: str):
        actual_title_of_page = actual_page_title
        print(f"---Checking The {button_name} Syllabus...---")
        self.string_result += f"---Checking The {button_name} Syllabus...---\n"
        if title == actual_title_of_page:
            print("---The syllabus is correct---")
            self.string_result += "---The syllabus is correct---\n"
            return True
        else:
            print("---Not the right syllabus---")
            self.string_result += "---Not the right syllabus---\n"
            return False

    # --------------------------------------Maslul Functions---------------------------------------------
    def maslul_real_time(self):
        print("-----Inside maslul_real_time function-----")
        self.string_result += "-----Inside maslul_real_time function-----\n"
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        index = 0
        dict_of_urls_of_syllabus = {"Bootcamp Real Time": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/RT/Real_Time_Emb_Linux_Complete_Path.pdf",
                                    "Embedded Systems": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/RT/Embedded_Systems_Complete_Path.pdf",
                                    "Real Time Embedded Linux": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/RT/Real_Time_Emb_Linux_Complete_Path.pdf",
                                    "Embedded Linux": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/RT/Embedded_Linux_Complete_Path.pdf"}
        running = True

        while running:
            for length in range(len(header.list_of_courses_on_real_time())):
                header.maslul().click()
                header.click_on_maslul_real_time().click()
                header.list_of_courses_on_real_time()[index].click()
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed():
                    # maslul_page.last_name_field_in_side_form_after_clicking_on_syllabus().send_keys(
                    #     self.test_user_last_name)
                    # maslul_page.first_name_field_in_side_form_after_clicking_on_syllabus().send_keys(
                    #     self.test_user_first_name)
                    # maslul_page.email_field_in_side_form_after_clicking_on_syllabus().send_keys(self.test_user_mail)
                    # maslul_page.phone_number_field_in_side_form_after_clicking_on_syllabus().send_keys(
                    #     self.test_user_phone_number)
                    # maslul_page.choose_maslul_field_in_side_form_after_clicking_on_syllabus().click()
                    # maslul_page.choose_maslul_real_time_in_side_form_after_clicking_on_syllabus().click()
                    # maslul_page.tick_terms_of_agreement_in_side_form_after_clicking_on_syllabus().click()
                    maslul_page.send_button_in_side_form_after_clicking_on_syllabus().click()
                    maslul_page.close_button_for_not_filling_in_details_in_form().click()

                self.driver.switch_to.window(self.driver.window_handles[index + 1])
                url_of_tab_syllabus = self.driver.current_url
                expected_url = list(dict_of_urls_of_syllabus.values())[index]
                self.compare_title_pages(expected_url, url_of_tab_syllabus, list(dict_of_urls_of_syllabus.keys())[index])
                index += 1
                #time.sleep(3)
                self.driver.switch_to.window(self.driver.window_handles[0])
                maslul_page.close_button_of_form_after_syllabus().click()
            running = False
        print("-----Outside maslul_real_time function-----")
        self.string_result += "-----Outside maslul_real_time function-----\n"

    def test_run_maslulim(self):
        self.maslul_real_time()
        try:
            file = open(f"../../Source/log {self.date_for_log}.txt", "a+")
            file.write(self.string_result)
            file.close()
        except FileNotFoundError:
            print("Did not found a file")