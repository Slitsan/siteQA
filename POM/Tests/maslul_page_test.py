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

    # Compares the syllabus url with a given url inside the 'maslul functions'
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

    # Filling the form that pops ups after clicking on the 'download syllabus'
    def filling_form_after_clicking_on_syllabus(self, maslul_page):
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

    # --------------------------------------Maslul Functions---------------------------------------------
    def maslul_real_time(self):
        print("-----Inside maslul_real_time function-----")
        self.string_result += "-----Inside maslul_real_time function-----\n"
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        index = 0
        index_of_dict = 0
        dict_of_urls_of_syllabus = {"Bootcamp Real Time (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/RT/Real_Time_Emb_Linux_Complete_Path.pdf",
                                    "Embedded Systems (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/RT/Embedded_Systems_Complete_Path.pdf",
                                    "Real Time Embedded Linux (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/RT/Real_Time_Emb_Linux_Complete_Path.pdf",
                                    "Embedded Linux (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/RT/Embedded_Linux_Complete_Path.pdf"}
        running = True

        while running:
            for length in range(len(header.list_of_courses_on_real_time())): # Loops according to the courses in Maslul
                header.maslul().click()
                header.maslul_real_time().click()
                header.list_of_courses_on_real_time()[index].click()
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed(): # Checks if a form appears after clicking on 'download syllabus'
                    self.filling_form_after_clicking_on_syllabus(maslul_page)
                    if maslul_page.choose_language_of_syllabus().is_displayed():  # Checks if a window of choosing a language for the syllabus appears
                        index_of_languages = 0
                        for lan in maslul_page.languages_of_syllabus():
                            print(f"--Choosing The {lan.text} Version Of The Syllabus--")
                            self.string_result += f"--Choosing The {lan.text} Version Of The Syllabus--\n"
                            lan.click()
                            tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
                            self.driver.switch_to.window(tabs[1])
                            main_tab = tabs.pop(0)
                            url_of_tab_syllabus = self.driver.current_url
                            expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                            self.compare_title_pages(expected_url, url_of_tab_syllabus,
                                                     list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                            for tab in tabs:  # Closes the syllabus tab after comparing the URLs
                                self.driver.switch_to.window(tab)
                                self.driver.close()
                            self.driver.switch_to.window(main_tab)
                            index_of_dict += 1
                            index_of_languages += 1
                            maslul_page.close_button_for_not_filling_in_details_in_form().click()
                            maslul_page.send_button_in_side_form_after_clicking_on_syllabus().click()
                            if index_of_languages >= len(maslul_page.languages_of_syllabus()):
                                maslul_page.close_button_of_choosing_languange_of_syllabus().click()
                                maslul_page.close_button_for_not_filling_in_details_in_form().click()
                                maslul_page.close_button_of_form_after_syllabus().click()
                    else:
                        maslul_page.close_button_for_not_filling_in_details_in_form().click()
                        tabs = self.driver.window_handles
                        self.driver.switch_to.window(tabs[1])
                        main_tab = tabs.pop(0)
                        url_of_tab_syllabus = self.driver.current_url
                        expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                        self.compare_title_pages(expected_url, url_of_tab_syllabus,
                                                 list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                        for tab in tabs:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                        self.driver.switch_to.window(main_tab)
                        index_of_dict += 1
                        maslul_page.close_button_of_form_after_syllabus().click()
                index += 1
            running = False
        print("-----Outside maslul_real_time function-----")
        self.string_result += "-----Outside maslul_real_time function-----\n"

    def maslul_full_stack(self):
        print("-----Inside maslul_full_stack function-----")
        self.string_result += "-----Inside maslul_full_stack function-----\n"
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        index = 0
        index_of_dict = 0
        dict_of_urls_of_syllabus = {"Full Stack (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/FS/Full_Stack_Complete_Track.pdf",
                                    "Full Stack (HEB)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/FS/Full_Stack_Complete_Track-HE.pdf"}
        running = True

        while running:
            for length in range(len(header.list_of_courses_on_full_stack())): # Loops according to the courses in Maslul
                header.maslul().click()
                header.maslul_full_stack().click()
                header.list_of_courses_on_full_stack()[index].click()
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed(): # Checks if a form appears after clicking on 'download syllabus'
                    self.filling_form_after_clicking_on_syllabus(maslul_page)
                    if maslul_page.choose_language_of_syllabus().is_displayed():  # Checks if a window of choosing a language for the syllabus appears
                        index_of_languages = 0
                        for lan in maslul_page.languages_of_syllabus():
                            print(f"--Choosing The {lan.text} Version Of The Syllabus--")
                            self.string_result += f"--Choosing The {lan.text} Version Of The Syllabus--\n"
                            lan.click()
                            tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
                            self.driver.switch_to.window(tabs[1])
                            main_tab = tabs.pop(0)
                            url_of_tab_syllabus = self.driver.current_url
                            expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                            self.compare_title_pages(expected_url, url_of_tab_syllabus,
                                                     list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                            for tab in tabs:  # Closes the syllabus tab after comparing the URLs
                                self.driver.switch_to.window(tab)
                                self.driver.close()
                            self.driver.switch_to.window(main_tab)
                            index_of_dict += 1
                            index_of_languages += 1
                            maslul_page.close_button_for_not_filling_in_details_in_form().click()
                            maslul_page.send_button_in_side_form_after_clicking_on_syllabus().click()
                            if index_of_languages >= len(maslul_page.languages_of_syllabus()):
                                maslul_page.close_button_of_choosing_languange_of_syllabus().click()
                                maslul_page.close_button_for_not_filling_in_details_in_form().click()
                                maslul_page.close_button_of_form_after_syllabus().click()
                    else:
                        maslul_page.close_button_for_not_filling_in_details_in_form().click()
                        tabs = self.driver.window_handles
                        self.driver.switch_to.window(tabs[1])
                        main_tab = tabs.pop(0)
                        url_of_tab_syllabus = self.driver.current_url
                        expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                        self.compare_title_pages(expected_url, url_of_tab_syllabus,
                                                 list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                        for tab in tabs:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                        self.driver.switch_to.window(main_tab)
                        index_of_dict += 1
                        maslul_page.close_button_of_form_after_syllabus().click()
                index += 1
            running = False
        print("-----Outside maslul_full_stack function-----")
        self.string_result += "-----Outside maslul_full_stack function-----\n"

    def maslul_cyber(self):
        print("-----Inside maslul_cyber function-----")
        self.string_result += "-----Inside maslul_cyber function-----\n"
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        index = 0
        index_of_dict = 0
        dict_of_urls_of_syllabus = {"Cyber (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/Cyber/Cyber_Security_Complete_Track_EN.pdf",
                                    "Cyber (HEB)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/Cyber/Cyber_Security_Complete_Track.pdf"}
        running = True

        while running:
            for length in range(len(header.list_of_courses_on_cyber())): # Loops according to the courses in Maslul
                header.maslul().click()
                header.maslul_cyber().click()
                header.list_of_courses_on_cyber()[index].click()
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed(): # Checks if a form appears after clicking on 'download syllabus'
                    self.filling_form_after_clicking_on_syllabus(maslul_page)
                    if maslul_page.choose_language_of_syllabus().is_displayed():  # Checks if a window of choosing a language for the syllabus appears
                        index_of_languages = 0
                        for lan in maslul_page.languages_of_syllabus():
                            print(f"--Choosing The {lan.text} Version Of The Syllabus--")
                            self.string_result += f"--Choosing The {lan.text} Version Of The Syllabus--\n"
                            lan.click()
                            tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
                            self.driver.switch_to.window(tabs[1])
                            main_tab = tabs.pop(0)
                            url_of_tab_syllabus = self.driver.current_url
                            expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                            self.compare_title_pages(expected_url, url_of_tab_syllabus,
                                                     list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                            for tab in tabs:  # Closes the syllabus tab after comparing the URLs
                                self.driver.switch_to.window(tab)
                                self.driver.close()
                            self.driver.switch_to.window(main_tab)
                            index_of_dict += 1
                            index_of_languages += 1
                            maslul_page.close_button_for_not_filling_in_details_in_form().click()
                            maslul_page.send_button_in_side_form_after_clicking_on_syllabus().click()
                            if index_of_languages >= len(maslul_page.languages_of_syllabus()):
                                maslul_page.close_button_of_choosing_languange_of_syllabus().click()
                                maslul_page.close_button_for_not_filling_in_details_in_form().click()
                                maslul_page.close_button_of_form_after_syllabus().click()
                    else:
                        maslul_page.close_button_for_not_filling_in_details_in_form().click()
                        tabs = self.driver.window_handles
                        self.driver.switch_to.window(tabs[1])
                        main_tab = tabs.pop(0)
                        url_of_tab_syllabus = self.driver.current_url
                        expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                        self.compare_title_pages(expected_url, url_of_tab_syllabus,
                                                 list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                        for tab in tabs:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                        self.driver.switch_to.window(main_tab)
                        index_of_dict += 1
                        maslul_page.close_button_of_form_after_syllabus().click()
                index += 1
            running = False
        print("-----Outside maslul_cyber function-----")
        self.string_result += "-----Outside maslul_cyber function-----\n"

    def maslul_machine_learning(self):
        print("-----Inside maslul_machine_learning function-----")
        self.string_result += "-----Inside maslul_machine_learning function-----\n"
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        index = 0
        index_of_dict = 0
        dict_of_urls_of_syllabus = {
            "Data Analyst (EN)": "currently no syllabus",
            "Machine Learning & Data Science (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/ML/Data_Science_Machine_Learning_Complete_Path.pdf",
            "Image Processing (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/ML/Computer_Vision_Complete_Track.pdf"}
        running = True

        while running:
            for length in range(len(header.list_of_courses_on_machine_learning())):  # Loops according to the courses in Maslul
                header.maslul().click()
                header.maslul_machine_learning().click()
                header.list_of_courses_on_machine_learning()[index].click()
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed():  # Checks if a form appears after clicking on 'download syllabus'
                    self.filling_form_after_clicking_on_syllabus(maslul_page)
                    if maslul_page.choose_language_of_syllabus().is_displayed():  # Checks if a window of choosing a language for the syllabus appears
                        index_of_languages = 0
                        for lan in maslul_page.languages_of_syllabus():
                            print(f"--Choosing The {lan.text} Version Of The Syllabus--")
                            self.string_result += f"--Choosing The {lan.text} Version Of The Syllabus--\n"
                            lan.click()
                            tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
                            self.driver.switch_to.window(tabs[1])
                            main_tab = tabs.pop(0)
                            url_of_tab_syllabus = self.driver.current_url
                            expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                            self.compare_title_pages(expected_url, url_of_tab_syllabus,
                                                     list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                            for tab in tabs:  # Closes the syllabus tab after comparing the URLs
                                self.driver.switch_to.window(tab)
                                self.driver.close()
                            self.driver.switch_to.window(main_tab)
                            index_of_dict += 1
                            index_of_languages += 1
                            maslul_page.close_button_for_not_filling_in_details_in_form().click()
                            maslul_page.send_button_in_side_form_after_clicking_on_syllabus().click()
                            if index_of_languages >= len(maslul_page.languages_of_syllabus()):
                                maslul_page.close_button_of_choosing_languange_of_syllabus().click()
                                maslul_page.close_button_for_not_filling_in_details_in_form().click()
                                maslul_page.close_button_of_form_after_syllabus().click()
                    else:
                        maslul_page.close_button_for_not_filling_in_details_in_form().click()
                        tabs = self.driver.window_handles
                        self.driver.switch_to.window(tabs[1])
                        main_tab = tabs.pop(0)
                        url_of_tab_syllabus = self.driver.current_url
                        expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                        self.compare_title_pages(expected_url, url_of_tab_syllabus,
                                                 list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                        for tab in tabs:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                        self.driver.switch_to.window(main_tab)
                        index_of_dict += 1
                        maslul_page.close_button_of_form_after_syllabus().click()
                index += 1
            running = False
        print("-----Outside maslul_machine_learning function-----")
        self.string_result += "-----Outside maslul_machine_learning function-----\n"

    def maslul_qa(self):
        print("-----Inside maslul_qa function-----")
        self.string_result += "-----Inside maslul_qa function-----\n"
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        index = 0
        index_of_dict = 0
        dict_of_urls_of_syllabus = {
            "Automation (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/QA/QA-Automation-Complete-Track_EN.pdf",
            "Automation (HEB)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/QA/Automation_Complete_Track.pdf",
            "Software Tester (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/QA/QA-Automation-Complete-Track_EN.pdf",
            "Software Tester (HEB)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/QA/QA-Automation_Complete_Track.pdf"}
        running = True

        while running:
            for length in range(
                    len(header.list_of_courses_on_qa())):  # Loops according to the courses in Maslul
                header.maslul().click()
                header.maslul_qa().click()
                header.list_of_courses_on_qa()[index].click()
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed():  # Checks if a form appears after clicking on 'download syllabus'
                    self.filling_form_after_clicking_on_syllabus(maslul_page)
                    if maslul_page.choose_language_of_syllabus().is_displayed():  # Checks if a window of choosing a language for the syllabus appears
                        index_of_languages = 0
                        for lan in maslul_page.languages_of_syllabus():
                            print(f"--Choosing The {lan.text} Version Of The Syllabus--")
                            self.string_result += f"--Choosing The {lan.text} Version Of The Syllabus--\n"
                            lan.click()
                            tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
                            self.driver.switch_to.window(tabs[1])
                            main_tab = tabs.pop(0)
                            url_of_tab_syllabus = self.driver.current_url
                            expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                            self.compare_title_pages(expected_url, url_of_tab_syllabus,
                                                     list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                            for tab in tabs:  # Closes the syllabus tab after comparing the URLs
                                self.driver.switch_to.window(tab)
                                self.driver.close()
                            self.driver.switch_to.window(main_tab)
                            index_of_dict += 1
                            index_of_languages += 1
                            maslul_page.close_button_for_not_filling_in_details_in_form().click()
                            maslul_page.send_button_in_side_form_after_clicking_on_syllabus().click()
                            if index_of_languages >= len(maslul_page.languages_of_syllabus()):
                                maslul_page.close_button_of_choosing_languange_of_syllabus().click()
                                maslul_page.close_button_for_not_filling_in_details_in_form().click()
                                maslul_page.close_button_of_form_after_syllabus().click()
                    else:
                        maslul_page.close_button_for_not_filling_in_details_in_form().click()
                        tabs = self.driver.window_handles
                        self.driver.switch_to.window(tabs[1])
                        main_tab = tabs.pop(0)
                        url_of_tab_syllabus = self.driver.current_url
                        expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                        self.compare_title_pages(expected_url, url_of_tab_syllabus,
                                                 list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                        for tab in tabs:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                        self.driver.switch_to.window(main_tab)
                        index_of_dict += 1
                        maslul_page.close_button_of_form_after_syllabus().click()
                index += 1
            running = False
        print("-----Outside maslul_qa function-----")
        self.string_result += "-----Outside maslul_qa function-----\n"

    def maslul_dev_ops(self):
        print("-----Inside maslul_dev_ops function-----")
        self.string_result += "-----Inside maslul_dev_ops function-----\n"
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        index = 0
        index_of_dict = 0
        dict_of_urls_of_syllabus = {
            "DevOps (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/Devops/DevOps_Complete_Track.pdf"}
        running = True

        while running:
            for length in range(
                    len(header.list_of_courses_on_dev_ops())):  # Loops according to the courses in Maslul
                header.maslul().click()
                header.maslul_dev_ops().click()
                header.list_of_courses_on_dev_ops()[index].click()
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed():  # Checks if a form appears after clicking on 'download syllabus'
                    self.filling_form_after_clicking_on_syllabus(maslul_page)
                    if maslul_page.choose_language_of_syllabus().is_displayed():  # Checks if a window of choosing a language for the syllabus appears
                        index_of_languages = 0
                        for lan in maslul_page.languages_of_syllabus():
                            print(f"--Choosing The {lan.text} Version Of The Syllabus--")
                            self.string_result += f"--Choosing The {lan.text} Version Of The Syllabus--\n"
                            lan.click()
                            tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
                            self.driver.switch_to.window(tabs[1])
                            main_tab = tabs.pop(0)
                            url_of_tab_syllabus = self.driver.current_url
                            expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                            self.compare_title_pages(expected_url, url_of_tab_syllabus,
                                                     list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                            for tab in tabs:  # Closes the syllabus tab after comparing the URLs
                                self.driver.switch_to.window(tab)
                                self.driver.close()
                            self.driver.switch_to.window(main_tab)
                            index_of_dict += 1
                            index_of_languages += 1
                            maslul_page.close_button_for_not_filling_in_details_in_form().click()
                            maslul_page.send_button_in_side_form_after_clicking_on_syllabus().click()
                            if index_of_languages >= len(maslul_page.languages_of_syllabus()):
                                maslul_page.close_button_of_choosing_languange_of_syllabus().click()
                                maslul_page.close_button_for_not_filling_in_details_in_form().click()
                                maslul_page.close_button_of_form_after_syllabus().click()
                    else:
                        maslul_page.close_button_for_not_filling_in_details_in_form().click()
                        tabs = self.driver.window_handles
                        self.driver.switch_to.window(tabs[1])
                        main_tab = tabs.pop(0)
                        url_of_tab_syllabus = self.driver.current_url
                        expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                        self.compare_title_pages(expected_url, url_of_tab_syllabus,
                                                 list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                        for tab in tabs:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                        self.driver.switch_to.window(main_tab)
                        index_of_dict += 1
                        maslul_page.close_button_of_form_after_syllabus().click()
                index += 1
            running = False
        print("-----Outside maslul_dev_ops function-----")
        self.string_result += "-----Outside maslul_dev_ops function-----\n"

    def maslul_linux_servers(self):
        print("-----Inside maslul_linux_servers function-----")
        self.string_result += "-----Inside maslul_linux_servers function-----\n"
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        index = 0
        index_of_dict = 0
        dict_of_urls_of_syllabus = {
            "Linux Servers (EN)": "Currently No Syllabus"}
        running = True

        while running:
            for length in range(
                    len(header.list_of_courses_on_linux_servers())):  # Loops according to the courses in Maslul
                header.maslul().click()
                header.maslul_linux_servers().click()
                header.list_of_courses_on_linux_servers()[index].click()
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed():  # Checks if a form appears after clicking on 'download syllabus'
                    self.filling_form_after_clicking_on_syllabus(maslul_page)
                    if maslul_page.choose_language_of_syllabus().is_displayed():  # Checks if a window of choosing a language for the syllabus appears
                        index_of_languages = 0
                        for lan in maslul_page.languages_of_syllabus():
                            print(f"--Choosing The {lan.text} Version Of The Syllabus--")
                            self.string_result += f"--Choosing The {lan.text} Version Of The Syllabus--\n"
                            lan.click()
                            tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
                            self.driver.switch_to.window(tabs[1])
                            main_tab = tabs.pop(0)
                            url_of_tab_syllabus = self.driver.current_url
                            expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                            self.compare_title_pages(expected_url, url_of_tab_syllabus,
                                                     list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                            for tab in tabs:  # Closes the syllabus tab after comparing the URLs
                                self.driver.switch_to.window(tab)
                                self.driver.close()
                            self.driver.switch_to.window(main_tab)
                            index_of_dict += 1
                            index_of_languages += 1
                            maslul_page.close_button_for_not_filling_in_details_in_form().click()
                            maslul_page.send_button_in_side_form_after_clicking_on_syllabus().click()
                            if index_of_languages >= len(maslul_page.languages_of_syllabus()):
                                maslul_page.close_button_of_choosing_languange_of_syllabus().click()
                                maslul_page.close_button_for_not_filling_in_details_in_form().click()
                                maslul_page.close_button_of_form_after_syllabus().click()
                    else:
                        maslul_page.close_button_for_not_filling_in_details_in_form().click()
                        tabs = self.driver.window_handles
                        self.driver.switch_to.window(tabs[1])
                        main_tab = tabs.pop(0)
                        url_of_tab_syllabus = self.driver.current_url
                        expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                        self.compare_title_pages(expected_url, url_of_tab_syllabus,
                                                 list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                        for tab in tabs:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                        self.driver.switch_to.window(main_tab)
                        index_of_dict += 1
                        maslul_page.close_button_of_form_after_syllabus().click()
                index += 1
            running = False
        print("-----Outside maslul_linux_servers function-----")
        self.string_result += "-----Outside maslul_linux_servers function-----\n"

    def test_run_maslulim(self):
        self.maslul_real_time()
        self.maslul_full_stack()
        self.maslul_cyber()
        self.maslul_machine_learning()
        self.maslul_qa()
        self.maslul_dev_ops()
        self.maslul_linux_servers()

        try:
            file = open(f"../../Source/log {self.date_for_log}.txt", "a+")
            file.write(self.string_result)
            file.close()
        except FileNotFoundError:
            print("Did not found a file")