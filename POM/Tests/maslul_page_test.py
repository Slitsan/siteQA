#   09/03/2022
#   Created By Pablik
#   Maslul Page Test
# -----------------------------------------------------
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from POM.Pages.header import Header
from datetime import datetime

# --------------------------------------------
from POM.Pages.maslul_page import MaslulPage


class MaslulPageTest(unittest.TestCase):
    def __init__(self, init_driver):
        super().__init__()
        self.driver = init_driver
        now = datetime.now()
        current_time = now.strftime("%d%m%H%M%S")
        self.date_for_log = now.strftime("%d %m %Y")
        self.test_user_last_name = "test"
        self.test_user_first_name = "test"
        self.test_user_mail = current_time + "@test.com"
        self.test_user_phone_number = current_time
        self.string_result = "*-----------------------------------TESTING MASLUL PAGES-----------------------------------------------\n"

    # Appends the message parameter to the string_result
    def string_message(self, message):
        print(message)
        self.string_result += message

    # Opens a new file if there is not one. Appends the string to it
    def open_file_and_append_string_message(self):
        try:
            file = open(f"./Source/log {self.date_for_log}.txt", "a+")
            file.write(self.string_result)
            file.close()
        except FileNotFoundError:
            print("Did not found a file")

    # Compares the syllabus url with a given url inside the 'maslul functions'
    def compare_syllabus_url(self, title: str, actual_page_title: str, button_name: str):
        actual_title_of_page = actual_page_title
        self.string_message(f"---Checking The {button_name} Syllabus---\n")
        if title == actual_title_of_page:
            self.string_message("---The syllabus is correct---\n")
            return True
        else:
            self.string_message("!------Not the right syllabus------!\n")
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

    # Prepares a dictionary of nav buttons according to page
    def prepares_dictionary_of_div_block(self, maslul_page):
        dict_of_nav_buttons_blocks = {}
        for div in range(len(maslul_page.list_of_buttons_in_navigation())):
            if div == 0:
                try:
                    dict_of_nav_buttons_blocks["אודות המסלול"] = maslul_page.about_block()
                except NoSuchElementException:
                    self.string_message("!------The button 'אודות המסלול' does not work------!\n")
                    continue
            if div == 1:
                try:
                    dict_of_nav_buttons_blocks["מבנה המסלול"] = maslul_page.structure_of_maslul_block()
                except NoSuchElementException:
                    self.string_message("!------The button 'מבנה המסלול' does not work------!\n")
                    continue
            if div == 2:
                try:
                    dict_of_nav_buttons_blocks[
                        "קהל יעד ודרישות קודם"] = maslul_page.target_audience_and_prior_requirements_block()
                except NoSuchElementException:
                    self.string_message("!------The button 'קהל יעד ודרישות קודם' does not work------!\n")
                    continue
            if div == 3:
                try:
                    dict_of_nav_buttons_blocks["ללמוד אצלנו"] = maslul_page.to_study_with_us_block()
                except NoSuchElementException:
                    self.string_message("!------The button 'ללמוד אצלנו' does not work------!\n")
                    continue
            if div == 4:
                try:
                    dict_of_nav_buttons_blocks["תעודת גמר"] = maslul_page.graduate_diploma_block()
                except NoSuchElementException:
                    self.string_message("!------The button 'תעודת גמר' does not work------!\n")
                    continue
            if div == 5:
                try:
                    dict_of_nav_buttons_blocks["שאלות ותשובות"] = maslul_page.questions_and_answers_block()
                except NoSuchElementException:
                    self.string_message("!------The button 'שאלות ותשובות' does not work------!\n")
                    continue
        return dict_of_nav_buttons_blocks

    # Click on each nav button in the navigation bar
    def click_on_each_nav_button_and_verifies_the_block(self, actions, index_of_btn, maslul_page):
        dict_of_nav_buttons_blocks = self.prepares_dictionary_of_div_block(
            maslul_page)  # Prepares a dictionary with maslul page div blocks
        for btn in maslul_page.list_of_buttons_in_navigation():  # Loops through the buttons in navigation
            if index_of_btn == len(
                    dict_of_nav_buttons_blocks):  # If index equals to the length of the dictionary(which contains the nav buttons) -> it breaks the loop
                break
            if btn.text == list(dict_of_nav_buttons_blocks.keys())[
                index_of_btn]:  # Checks if the current nav button equals to the key in the dictionary
                try:
                    actions.move_to_element(btn).click().perform()  # Click on the current nav button
                    btn_id_split = btn.get_attribute("href").split("#")  # Splits the href of the nav button
                    btn_id = str(btn_id_split[
                                     -1])  # Takes the last element in the splited list -> which is the id of the div block
                    block = list(dict_of_nav_buttons_blocks.values())[
                        index_of_btn]  # Contains the div block in the dictionary according to the place of the index
                    block_key = list(dict_of_nav_buttons_blocks.keys())[
                        index_of_btn]  # Contains the key in the dictionary according to the place of the index
                    block_id = block.get_attribute("id")  # Contains the id of the div block
                    self.string_message(
                        f"---Comparing Between The '{btn.text}' Nav Button And The '{block_key}' Div Block---\n")
                    if btn.text == "תעודת גמר":  # Checks if the button equals to 'תעודת גמר'
                        if maslul_page.diploma_image().get_attribute(
                                "src") is None:  # Checks if there is no image for the diploma
                            self.string_message("!------No picture for diploma------!\n")
                    # if btn.text == "שאלות ותשובות":  # Checks if the button equals 'שאלות ותשובות'
                    #     for question in maslul_page.list_of_div_blocks_in_faq():  # Loops through the questions in the FAQ div block
                    #         self.string_message(
                    #             f"---Clicked on question {question.text}---\n")  # Prints each question that was clicked
                    #         actions.move_to_element(question).click().perform()  # Clicks on each question
                    if btn_id == block_id:  # Checks if the current button id equals to the div block id
                        self.string_message("---Element Matches---\n")
                except ElementNotVisibleException:
                    self.string_message("!------Element Not Found------!\n")
                except IndexError:
                    print("Out of bounds")
                index_of_btn += 1

    # Fills the form under the syllabus
    def form_under_syllabus(self, driver: WebDriver, last_name="test", first_name="test", ending_of_mail="@test.com",
                            phone_number="",
                            choose_maslul="yes", tick_terms_and_services="yes", send_button="yes",
                            close_button="yes"):
        self.string_message("--Inside form_under_syllabus function--\n")
        now = datetime.now()
        current_time = now.strftime("%d%m%H%M%S")
        maslul_page = MaslulPage(self.driver)
        self.string_message("---Entering last name---\n")
        maslul_page.last_name_field_in_form_under_syllabus().send_keys(last_name)
        self.string_message("---Entering first name---\n")
        maslul_page.first_name_field_in_form_under_syllabus().send_keys(first_name)
        self.string_message("---Entering mail---\n")
        maslul_page.email_field_in_form_under_syllabus().send_keys(current_time + ending_of_mail)
        if phone_number == "":
            phone_number = current_time
        self.string_message("---Entering phone number---\n")
        maslul_page.phone_field_in_form_under_syllabus().send_keys(phone_number)
        if choose_maslul == "yes":
            self.string_message("---Choosing maslul---\n")
            maslul_page.choose_maslul_field_in_form_under_syllabus().click()
            maslul_page.choose_maslul_real_time_field_in_form_under_syllabus().click()
        if tick_terms_and_services == "yes":
            self.string_message("---Ticking the terms of agreement and services---\n")
            maslul_page.agreement_of_terms_and_services_field_in_form_under_syllabus().click()
        if send_button == "yes":
            self.string_message("---Clicking on the 'send' button---\n")
            maslul_page.send_button_in_form_under_syllabus().click()
        if close_button == "yes":
            self.string_message("---Clicking on the close button---\n")
            maslul_page.close_button_after_filling_details_in_form_under_syllabus().click()
            tabs = driver.window_handles
            driver.switch_to.window(tabs[1])
            driver.close()
            driver.switch_to.window(tabs[0])
        self.string_message("--Outside form_under_syllabus function--\n")

    # Checks if the salary block in the page is presented, and if it IS. Confirms that it is not empty
    def checks_if_salary_block_is_presented_and_if_it_has_content(self, maslul_page):
        try:
            if maslul_page.salary_block().is_displayed():
                self.string_message("---Salary Block is presented---\n")
                if maslul_page.table_list_of_salary_block() or maslul_page.list_of_p_blocks_in_salary_block():
                    self.string_message("---There is content in Salary Block---\n")
                else:
                    self.string_message("!------No content in Salary Block------!\n")
        except NoSuchElementException:
            self.string_message("!------Element Not Found------!\n")

    # Checks if the FAQ block in presented on the page and if it IS. Clicks on every question
    def checks_if_faq_block_is_presented_and_clicks_on_every_question_in_it(self, actions, maslul_page):
        try:
            if maslul_page.maslul_faq_block().is_displayed():
                self.string_message("---FAQ Block is presented---\n")
                for question in maslul_page.list_of_div_blocks_in_faq():
                    self.string_message(f"Clicked on question -> {question.text}\n")
                    actions.move_to_element(question).click().perform()
        except NoSuchElementException:
            self.string_message("!------Element Not Found------!\n")

    # --------------------------------------MASLUL'S METHODS---------------------------------------------
    def maslul_real_time(self):
        self.string_message("@Inside Maslul Real-Time function---\n")
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        index_of_dict = 0
        dict_of_urls_of_syllabus = {
            "Bootcamp Real Time (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/RT/Real_Time_Emb_Linux_Complete_Path.pdf",
            "Embedded Systems (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/RT/Embedded_Systems_Complete_Path.pdf",
            "Real Time Embedded Linux (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/RT/Real_Time_Emb_Linux_Complete_Path.pdf",
            "Embedded Linux (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/RT/Embedded_Linux_Complete_Path.pdf"}
        running = True

        while running:
            for length in range(len(header.list_of_courses_on_real_time())):  # Loops according to the courses in Maslul
                header.maslul().click()
                header.maslul_real_time().click()
                self.string_message(f"@@Inside course {header.list_of_courses_on_real_time()[index].text}\n")
                header.list_of_courses_on_real_time()[index].click()
                index_of_btn = 0
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed():  # Checks if a form appears after clicking on 'download syllabus'
                    self.filling_form_after_clicking_on_syllabus(maslul_page)
                    if maslul_page.choose_language_of_syllabus().is_displayed():  # Checks if a window of choosing a language for the syllabus appears
                        index_of_languages = 0
                        for lan in maslul_page.languages_of_syllabus():
                            self.string_message(f"--Choosing The {lan.text} Version Of The Syllabus--\n")
                            lan.click()
                            tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
                            self.driver.switch_to.window(tabs[1])
                            main_tab = tabs.pop(0)
                            url_of_tab_syllabus = self.driver.current_url
                            expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                            self.compare_syllabus_url(expected_url, url_of_tab_syllabus,
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
                        self.compare_syllabus_url(expected_url, url_of_tab_syllabus,
                                                  list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                        for tab in tabs:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                        self.driver.switch_to.window(main_tab)
                        index_of_dict += 1
                        maslul_page.close_button_of_form_after_syllabus().click()
                self.click_on_each_nav_button_and_verifies_the_block(actions, index_of_btn, maslul_page)
                self.checks_if_salary_block_is_presented_and_if_it_has_content(maslul_page)
                self.checks_if_faq_block_is_presented_and_clicks_on_every_question_in_it(actions, maslul_page)
                # self.form_under_syllabus(self.driver)
                index += 1
            running = False
        self.string_message("@Outside Maslul Real-Time function---\n")

    def maslul_full_stack(self):
        self.string_message("@Inside Maslul Full-Stack function---\n")
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        index_of_dict = 0
        dict_of_urls_of_syllabus = {
            "Full Stack (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/FS/Full_Stack_Complete_Track.pdf",
            "Full Stack (HEB)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/FS/Full_Stack_Complete_Track-HE.pdf"}
        running = True

        while running:
            for length in range(
                    len(header.list_of_courses_on_full_stack())):  # Loops according to the courses in Maslul
                header.maslul().click()
                header.maslul_full_stack().click()
                self.string_message(f"@@Inside course {header.list_of_courses_on_full_stack()[index].text}\n")
                header.list_of_courses_on_full_stack()[index].click()
                index_of_btn = 0
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed():  # Checks if a form appears after clicking on 'download syllabus'
                    self.filling_form_after_clicking_on_syllabus(maslul_page)
                    if maslul_page.choose_language_of_syllabus().is_displayed():  # Checks if a window of choosing a language for the syllabus appears
                        index_of_languages = 0
                        for lan in maslul_page.languages_of_syllabus():
                            self.string_message(f"--Choosing The {lan.text} Version Of The Syllabus--\n")
                            lan.click()
                            tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
                            self.driver.switch_to.window(tabs[1])
                            main_tab = tabs.pop(0)
                            url_of_tab_syllabus = self.driver.current_url
                            expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                            self.compare_syllabus_url(expected_url, url_of_tab_syllabus,
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
                        self.compare_syllabus_url(expected_url, url_of_tab_syllabus,
                                                  list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                        for tab in tabs:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                        self.driver.switch_to.window(main_tab)
                        index_of_dict += 1
                        maslul_page.close_button_of_form_after_syllabus().click()
                self.click_on_each_nav_button_and_verifies_the_block(actions, index_of_btn, maslul_page)
                self.checks_if_salary_block_is_presented_and_if_it_has_content(maslul_page)
                self.checks_if_faq_block_is_presented_and_clicks_on_every_question_in_it(actions, maslul_page)
                # self.form_under_syllabus(self.driver)
                index += 1
            running = False
        self.string_message("@Outside Maslul Full-Stack function---\n")

    def maslul_cyber(self):
        self.string_message("@Inside Maslul Cyber function---\n")
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        index_of_dict = 0
        dict_of_urls_of_syllabus = {
            "Cyber (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/Cyber/Cyber_Security_Complete_Track_EN.pdf",
            "Cyber (HEB)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/Cyber/Cyber_Security_Complete_Track.pdf"}
        running = True

        while running:
            for length in range(len(header.list_of_courses_on_cyber())):  # Loops according to the courses in Maslul
                header.maslul().click()
                header.maslul_cyber().click()
                self.string_message(f"@@Inside course {header.list_of_courses_on_cyber()[index].text}\n")
                header.list_of_courses_on_cyber()[index].click()
                index_of_btn = 0
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed():  # Checks if a form appears after clicking on 'download syllabus'
                    self.filling_form_after_clicking_on_syllabus(maslul_page)
                    if maslul_page.choose_language_of_syllabus().is_displayed():  # Checks if a window of choosing a language for the syllabus appears
                        index_of_languages = 0
                        for lan in maslul_page.languages_of_syllabus():
                            self.string_message(f"--Choosing The {lan.text} Version Of The Syllabus--\n")
                            lan.click()
                            tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
                            self.driver.switch_to.window(tabs[1])
                            main_tab = tabs.pop(0)
                            url_of_tab_syllabus = self.driver.current_url
                            expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                            self.compare_syllabus_url(expected_url, url_of_tab_syllabus,
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
                        self.compare_syllabus_url(expected_url, url_of_tab_syllabus,
                                                  list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                        for tab in tabs:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                        self.driver.switch_to.window(main_tab)
                        index_of_dict += 1
                        maslul_page.close_button_of_form_after_syllabus().click()
                self.click_on_each_nav_button_and_verifies_the_block(actions, index_of_btn, maslul_page)
                self.checks_if_salary_block_is_presented_and_if_it_has_content(maslul_page)
                self.checks_if_faq_block_is_presented_and_clicks_on_every_question_in_it(actions, maslul_page)
                # self.form_under_syllabus(self.driver)
                index += 1
            running = False
        self.string_message("@Outside Maslul Cyber function---\n")

    def maslul_machine_learning(self):
        self.string_message("@Inside Maslul Machine Learning function---\n")
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        index_of_dict = 0
        dict_of_urls_of_syllabus = {
            "Data Analyst (EN)": "currently no syllabus",
            "Machine Learning & Data Science (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/ML/Data_Science_Machine_Learning_Complete_Path.pdf",
            "Image Processing (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Tracks/ML/Computer_Vision_Complete_Track.pdf"}
        running = True
        has_diploma_picture = False

        while running:
            for length in range(
                    len(header.list_of_courses_on_machine_learning())):  # Loops according to the courses in Maslul
                header.maslul().click()
                header.maslul_machine_learning().click()
                self.string_message(f"@@Inside course {header.list_of_courses_on_machine_learning()[index].text}\n")
                header.list_of_courses_on_machine_learning()[index].click()
                index_of_btn = 0
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed():  # Checks if a form appears after clicking on 'download syllabus'
                    self.filling_form_after_clicking_on_syllabus(maslul_page)
                    if maslul_page.choose_language_of_syllabus().is_displayed():  # Checks if a window of choosing a language for the syllabus appears
                        index_of_languages = 0
                        for lan in maslul_page.languages_of_syllabus():
                            self.string_message(f"--Choosing The {lan.text} Version Of The Syllabus--\n")
                            lan.click()
                            tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
                            self.driver.switch_to.window(tabs[1])
                            main_tab = tabs.pop(0)
                            url_of_tab_syllabus = self.driver.current_url
                            expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                            self.compare_syllabus_url(expected_url, url_of_tab_syllabus,
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
                        self.compare_syllabus_url(expected_url, url_of_tab_syllabus,
                                                  list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                        for tab in tabs:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                        self.driver.switch_to.window(main_tab)
                        index_of_dict += 1
                        maslul_page.close_button_of_form_after_syllabus().click()
                self.click_on_each_nav_button_and_verifies_the_block(actions, index_of_btn, maslul_page)
                self.checks_if_salary_block_is_presented_and_if_it_has_content(maslul_page)
                self.checks_if_faq_block_is_presented_and_clicks_on_every_question_in_it(actions, maslul_page)
                # self.form_under_syllabus(self.driver)
                index += 1
            running = False
        self.string_message("@Outside Maslul Machine Learning function---\n")

    def maslul_qa(self):
        self.string_message("@Inside Maslul QA function---\n")
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        actions = ActionChains(self.driver)
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
                self.string_message(f"@@Inside course {header.list_of_courses_on_qa()[index].text}\n")
                header.list_of_courses_on_qa()[index].click()
                index_of_btn = 0
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed():  # Checks if a form appears after clicking on 'download syllabus'
                    self.filling_form_after_clicking_on_syllabus(maslul_page)
                    if maslul_page.choose_language_of_syllabus().is_displayed():  # Checks if a window of choosing a language for the syllabus appears
                        index_of_languages = 0
                        for lan in maslul_page.languages_of_syllabus():
                            self.string_message(f"--Choosing The {lan.text} Version Of The Syllabus--\n")
                            lan.click()
                            tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
                            self.driver.switch_to.window(tabs[1])
                            main_tab = tabs.pop(0)
                            url_of_tab_syllabus = self.driver.current_url
                            expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                            self.compare_syllabus_url(expected_url, url_of_tab_syllabus,
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
                        self.compare_syllabus_url(expected_url, url_of_tab_syllabus,
                                                  list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                        for tab in tabs:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                        self.driver.switch_to.window(main_tab)
                        index_of_dict += 1
                        maslul_page.close_button_of_form_after_syllabus().click()
                self.click_on_each_nav_button_and_verifies_the_block(actions, index_of_btn, maslul_page)
                self.checks_if_salary_block_is_presented_and_if_it_has_content(maslul_page)
                self.checks_if_faq_block_is_presented_and_clicks_on_every_question_in_it(actions, maslul_page)
                # self.form_under_syllabus(self.driver)
                index += 1
            running = False
        self.string_message("@Outside Maslul QA function---\n")

    def maslul_dev_ops(self):
        self.string_message("@Inside Maslul DevOps function---\n")
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        actions = ActionChains(self.driver)
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
                self.string_message(f"@@Inside course {header.list_of_courses_on_dev_ops()[index].text}\n")
                header.list_of_courses_on_dev_ops()[index].click()
                index_of_btn = 0
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed():  # Checks if a form appears after clicking on 'download syllabus'
                    self.filling_form_after_clicking_on_syllabus(maslul_page)
                    if maslul_page.choose_language_of_syllabus().is_displayed():  # Checks if a window of choosing a language for the syllabus appears
                        index_of_languages = 0
                        for lan in maslul_page.languages_of_syllabus():
                            self.string_message(f"--Choosing The {lan.text} Version Of The Syllabus--\n")
                            lan.click()
                            tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
                            self.driver.switch_to.window(tabs[1])
                            main_tab = tabs.pop(0)
                            url_of_tab_syllabus = self.driver.current_url
                            expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                            self.compare_syllabus_url(expected_url, url_of_tab_syllabus,
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
                        self.compare_syllabus_url(expected_url, url_of_tab_syllabus,
                                                  list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                        for tab in tabs:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                        self.driver.switch_to.window(main_tab)
                        index_of_dict += 1
                        maslul_page.close_button_of_form_after_syllabus().click()
                self.click_on_each_nav_button_and_verifies_the_block(actions, index_of_btn, maslul_page)
                self.checks_if_salary_block_is_presented_and_if_it_has_content(maslul_page)
                self.checks_if_faq_block_is_presented_and_clicks_on_every_question_in_it(actions, maslul_page)
                # self.form_under_syllabus(self.driver)
                index += 1
            running = False
        self.string_message("@Outside Maslul DevOps function---\n")

    def maslul_linux_servers(self):
        self.string_message("@Inside Maslul Linux Servers function---\n")
        header = Header(self.driver)
        maslul_page = MaslulPage(self.driver)
        actions = ActionChains(self.driver)
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
                self.string_message(f"@@Inside course {header.list_of_courses_on_linux_servers()[index].text}\n")
                header.list_of_courses_on_linux_servers()[index].click()
                index_of_btn = 0
                maslul_page.download_syllabus().click()
                if maslul_page.form_after_clicking_on_syllabus().is_displayed():  # Checks if a form appears after clicking on 'download syllabus'
                    self.filling_form_after_clicking_on_syllabus(maslul_page)
                    if maslul_page.choose_language_of_syllabus().is_displayed():  # Checks if a window of choosing a language for the syllabus appears
                        index_of_languages = 0
                        for lan in maslul_page.languages_of_syllabus():
                            self.string_message(f"--Choosing The {lan.text} Version Of The Syllabus--\n")
                            lan.click()
                            tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
                            self.driver.switch_to.window(tabs[1])
                            main_tab = tabs.pop(0)
                            url_of_tab_syllabus = self.driver.current_url
                            expected_url = list(dict_of_urls_of_syllabus.values())[index_of_dict]
                            self.compare_syllabus_url(expected_url, url_of_tab_syllabus,
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
                        self.compare_syllabus_url(expected_url, url_of_tab_syllabus,
                                                  list(dict_of_urls_of_syllabus.keys())[index_of_dict])
                        for tab in tabs:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                        self.driver.switch_to.window(main_tab)
                        index_of_dict += 1
                        maslul_page.close_button_of_form_after_syllabus().click()
                self.click_on_each_nav_button_and_verifies_the_block(actions, index_of_btn, maslul_page)
                self.checks_if_salary_block_is_presented_and_if_it_has_content(maslul_page)
                self.checks_if_faq_block_is_presented_and_clicks_on_every_question_in_it(actions, maslul_page)
                # self.form_under_syllabus(self.driver)
                index += 1
            running = False
        self.string_message("@Outside Maslul Linux Servers function---\n")

    # ----------------------------------------------------TEST------------------------------------------

    def test_run_maslulim(self):
        self.maslul_real_time()
        self.maslul_full_stack()
        self.maslul_cyber()
        self.maslul_machine_learning()
        self.maslul_qa()
        self.maslul_dev_ops()
        self.maslul_linux_servers()
        self.open_file_and_append_string_message()
