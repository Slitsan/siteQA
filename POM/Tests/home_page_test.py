#   07/03/2022
#   Created By Pablik
#   Home Page Test
# ---------------------------------------------------------
import time
from datetime import datetime
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from POM.Pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


# ---------------------------------------------------------
class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
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
        cls.string_result = "-----------------------------------TESTING HOME PAGE REGISTRATION-----------------------------------------------\n"

    def string_message(self, message):
        print(message)
        self.string_result += message

    def open_file_and_append_string_message(self):
        try:
            file = open(f"../../Source/log {self.date_for_log}.txt", "a+")
            file.write(self.string_result)
            file.close()
        except FileNotFoundError:
            print("Did not found a file")

    # ---------------------------------POPUP TEST-----------------------------------------
    def popup_form(self, last_name="test", first_name="test", ending_of_mail="@test.com", phone_number="",
                   choose_maslul="yes", tick_terms_and_services="yes", send_button="yes", close_form="yes"):
        self.string_message("---Inside popup_form function---\n")
        now = datetime.now()
        current_time = now.strftime("%d%m%H%M%S")
        home_page = HomePage(self.driver)
        self.string_message("---Entering last name---\n")
        home_page.last_name_field_in_form_popup().send_keys(last_name)
        self.string_message("---Entering first name---\n")
        home_page.first_name_field_in_form_popup().send_keys(first_name)
        self.string_message("---Entering mail---\n")
        home_page.email_field_in_form_popup().send_keys(current_time + ending_of_mail)
        if phone_number == "":
            phone_number = current_time
        self.string_message("---Entering phone number---\n")
        home_page.phone_field_in_form_popup().send_keys(phone_number)
        if choose_maslul == "yes":
            self.string_message("---Choosing maslul---\n")
            home_page.choose_maslul_in_form_popup().click()
            home_page.choose_maslul_real_time_in_form_popup().click()
        if tick_terms_and_services == "yes":
            self.string_message("---Ticking the terms of agreement and services---\n")
            home_page.terms_of_agreement_field_in_form_popup().click()
        if send_button == "yes":
            self.string_message("---Clicking on the 'send' button---\n")
            home_page.send_button_in_form_popup().click()
        if close_form == "yes":
            self.string_message("---Closing the popup form---\n")
            home_page.close_button_in_popup_form().click()
        self.string_message("---Outside popup_form function---\n")

    def send_keys_to_last_name_field_in_popup(self):
        print("---Inside send_keys_to_last_name_field_in_popup function---")
        self.string_result += "---Inside send_keys_to_last_name_field_in_popup function---\n"
        home_page = HomePage(self.driver)
        home_page.last_name_field_in_form_popup().send_keys(self.test_user_last_name)
        print("---Outside send_keys_to_last_name_field_in_popup function---")
        self.string_result += "---Outside send_keys_to_last_name_field_in_popup function---\n"

    def send_keys_to_first_name_field_in_popup(self):
        print("---Inside send_keys_to_first_name_field_in_popup function---")
        self.string_result += "---Inside send_keys_to_first_name_field_in_popup function---\n"
        home_page = HomePage(self.driver)
        home_page.first_name_field_in_form_popup().send_keys(self.test_user_first_name)
        print("---Outside send_keys_to_first_name_field_in_popup function---")
        self.string_result += "---Outside send_keys_to_first_name_field_in_popup function---\n"

    def send_keys_to_mail_field_in_popup(self):
        print("---Inside send_keys_to_mail_field_in_popup function---")
        self.string_result += "---Inside send_keys_to_mail_field_in_popup function---\n"
        home_page = HomePage(self.driver)
        home_page.email_field_in_form_popup().send_keys(self.test_user_mail)
        print("---Outside send_keys_to_mail_field_in_popup function---")
        self.string_result += "---Outside send_keys_to_mail_field_in_popup function---\n"

    def send_keys_to_phone_number_field_in_popup(self):
        print("---Inside send_keys_to_phone_number_field_in_popup function---")
        self.string_result += "---Inside send_keys_to_phone_number_field_in_popup function---\n"
        home_page = HomePage(self.driver)
        home_page.phone_field_in_form_popup().send_keys(self.test_user_phone_number)
        print("---Outside send_keys_to_phone_number_field_in_popup function---")
        self.string_result += "---Outside send_keys_to_phone_number_field_in_popup function---\n"

    def choose_maslul_real_time_in_popup(self):
        print("---Inside choose_maslul_real_time_in_popup function---")
        self.string_result += "---Inside choose_maslul_real_time_in_popup function---\n"
        home_page = HomePage(self.driver)
        home_page.choose_maslul_in_form_popup().click()
        home_page.choose_maslul_real_time_in_form_popup().click()
        print("---Outside choose_maslul_real_time_in_popup function---")
        self.string_result += "---Outside choose_maslul_real_time_in_popup function---\n"

    def tick_terms_and_services_button_in_popup(self):
        print("---Inside tick_terms_and_services_button_in_popup function---")
        self.string_result += "---Inside tick_terms_and_services_button_in_popup function---\n"
        home_page = HomePage(self.driver)
        home_page.terms_of_agreement_field_in_form_popup().click()
        print("---Outside tick_terms_and_services_button_in_popup function---")
        self.string_result += "---Outside tick_terms_and_services_button_in_popup function---\n"

    def click_on_send_button_in_popup(self):
        print("---Inside click_on_send_button_in_popup function---")
        self.string_result += "---Inside click_on_send_button_in_popup function---\n"
        home_page = HomePage(self.driver)
        home_page.send_button_in_form_popup().click()
        print("---Outside click_on_send_button_in_popup function---")
        self.string_result += "---Outside click_on_send_button_in_popup function---\n"

    def close_popup(self):
        print("---Inside wait_for_popup function---")
        self.string_result += "---Inside wait_for_popup function---\n"
        home_page = HomePage(self.driver)
        time.sleep(12)
        home_page.close_button_in_popup_form().click()
        print("---Outside wait_for_popup function---")
        self.string_result += "---Outside wait_for_popup function---\n"

    # def test_popup_form(self):
    # self.popup_form()
    # self.open_file_and_append_string_message()
    # self.send_keys_to_last_name_field_in_popup()
    # self.send_keys_to_first_name_field_in_popup()
    # self.send_keys_to_mail_field_in_popup()
    # self.send_keys_to_phone_number_field_in_popup()
    # self.choose_maslul_real_time_in_popup()
    # self.tick_terms_and_services_button_in_popup()
    # self.click_on_send_button_in_popup()
    # self.close_popup()

    # -----------------------------------------MAIN FORM TEST---------------------------------------
    def main_form(self, last_name="test", first_name="test", ending_of_mail="@test.com", phone_number="",
                  choose_maslul="yes", tick_terms_and_services="yes", send_button="yes", close_button="yes"):
        self.string_message("---Inside main_form function---\n")
        now = datetime.now()
        current_time = now.strftime("%d%m%H%M%S")
        home_page = HomePage(self.driver)
        self.string_message("---Entering last name---\n")
        home_page.last_name_field_in_main_form().send_keys(last_name)
        self.string_message("---Entering first name---\n")
        home_page.first_name_field_in_main_form().send_keys(first_name)
        self.string_message("---Entering mail---\n")
        home_page.email_field_in_main_form().send_keys(current_time + ending_of_mail)
        if phone_number == "":
            phone_number = current_time
        self.string_message("---Entering phone number---\n")
        home_page.phone_number_field_in_main_form().send_keys(phone_number)
        if choose_maslul == "yes":
            self.string_message("---Choosing maslul---\n")
            home_page.choose_maslul_in_main_form().click()
            home_page.choose_maslul_real_time_in_main_form().click()
        if tick_terms_and_services == "yes":
            self.string_message("---Ticking the terms of agreement and services---\n")
            home_page.terms_of_agreement_field_in_main_form().click()
        if send_button == "yes":
            self.string_message("---Clicking on the 'send' button---\n")
            home_page.send_button_in_main_form().click()
        if close_button == "yes":
            self.string_message("---Clicking on the close button---\n")
            home_page.close_button_after_filling_the_main_form().click()
        self.string_message("---Outside main_form function---\n")

    def send_keys_to_last_name_field_in_main_form(self):
        print("---Inside send_keys_to_last_name_field_in_main_form function---")
        self.string_result += "---Inside send_keys_to_last_name_field_in_main_form function---\n"
        home_page = HomePage(self.driver)
        home_page.last_name_field_in_main_form().send_keys(self.test_user_last_name)
        print("---Outside send_keys_to_last_name_field_in_main_form function---")
        self.string_result += "---Outside send_keys_to_last_name_field_in_main_form function---\n"

    def send_keys_to_first_name_field_in_main_form(self):
        print("---Inside send_keys_to_first_name_field_in_main_form function---")
        self.string_result += "---Inside send_keys_to_first_name_field_in_main_form function---\n"
        home_page = HomePage(self.driver)
        home_page.first_name_field_in_main_form().send_keys(self.test_user_first_name)
        print("---Outside send_keys_to_first_name_field_in_main_form function---")
        self.string_result += "---Outside send_keys_to_first_name_field_in_main_form function---\n"

    def send_keys_to_mail_field_in_main_form(self):
        print("---Inside send_keys_to_mail_field_in_main_form function---")
        self.string_result += "---Inside send_keys_to_mail_field_in_main_form function---\n"
        home_page = HomePage(self.driver)
        home_page.email_field_in_main_form().send_keys(self.test_user_mail)
        print("---Outside send_keys_to_mail_field_in_main_form function---")
        self.string_result += "---Outside send_keys_to_mail_field_in_main_form function---\n"

    def send_keys_to_phone_number_field_in_main_form(self):
        print("---Inside send_keys_to_phone_number_field_in_main_form function---")
        self.string_result += "---Inside send_keys_to_phone_number_field_in_main_form function---\n"
        home_page = HomePage(self.driver)
        home_page.phone_number_field_in_main_form().send_keys(self.test_user_phone_number)
        print("---Outside send_keys_to_phone_number_field_in_main_form function---")
        self.string_result += "---Outside send_keys_to_phone_number_field_in_main_form function---\n"

    def choose_maslul_real_time_in_main_form(self):
        print("---Inside choose_maslul_real_time_in_main_form function---")
        self.string_result += "---Inside choose_maslul_real_time_in_main_form function---\n"
        home_page = HomePage(self.driver)
        home_page.choose_maslul_in_main_form().click()
        home_page.choose_maslul_real_time_in_main_form().click()
        print("---Outside choose_maslul_real_time_in_main_form function---")
        self.string_result += "---Outside choose_maslul_real_time_in_main_form function---\n"

    def tick_terms_and_services_button_in_main_form(self):
        print("---Inside tick_terms_and_services_button_in_main_form function---")
        self.string_result += "---Inside tick_terms_and_services_button_in_main_form function---\n"
        home_page = HomePage(self.driver)
        home_page.terms_of_agreement_field_in_main_form().click()
        print("---Outside tick_terms_and_services_button_in_main_form function---")
        self.string_result += "---Outside tick_terms_and_services_button_in_main_form function---\n"

    def click_on_send_button_in_main_form(self):
        print("---Inside click_on_send_button_in_main_form function---")
        self.string_result += "---Inside click_on_send_button_in_main_form function---\n"
        home_page = HomePage(self.driver)
        home_page.send_button_in_main_form().click()
        print("---Outside click_on_send_button_in_main_form function---")
        self.string_result += "---Outside click_on_send_button_in_main_form function---\n"

    # def test_main_form(self):
    #     self.close_popup()
    #     self.main_form()
    #     self.open_file_and_append_string_message()
    #     self.send_keys_to_last_name_field_in_main_form()
    #     self.send_keys_to_first_name_field_in_main_form()
    #     self.send_keys_to_mail_field_in_main_form()
    #     self.send_keys_to_phone_number_field_in_main_form()
    #     self.choose_maslul_real_time_in_main_form()
    #     self.tick_terms_and_services_button_in_main_form()
    # self.click_on_send_button_in_main_form()

    # -----------------------------------FLOATING FORM TEST-------------------------------
    # def hover_on_floating_menu(self):
    #     print("---Inside click_on_floating_menu function...---")
    #     home_page = HomePage(self.driver)
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(home_page.floating_menu()).perform()
    #     # home_page.floating_menu().click()
    #     print("---Outside click_on_floating_menu function...---")

    def floating_form(self, last_name="test", first_name="test", ending_of_mail="@test.com", phone_number="",
                  choose_maslul="yes", tick_terms_and_services="yes", send_button="yes", close_button="yes"):
        self.string_message("---Inside floating_form function---\n")
        now = datetime.now()
        current_time = now.strftime("%d%m%H%M%S")
        home_page = HomePage(self.driver)
        self.string_message("---Clicking on the floating form---\n")
        home_page.form_in_floating_menu().click()
        self.string_message("---Entering last name---\n")
        home_page.last_name_field_in_floating_form().send_keys(last_name)
        self.string_message("---Entering first name---\n")
        home_page.first_name_field_in_floating_form().send_keys(first_name)
        self.string_message("---Entering mail---\n")
        home_page.email_field_in_floating_form().send_keys(current_time + ending_of_mail)
        if phone_number == "":
            phone_number = current_time
        self.string_message("---Entering phone number---\n")
        home_page.phone_number_field_in_floating_form().send_keys(phone_number)
        if choose_maslul == "yes":
            self.string_message("---Choosing maslul---\n")
            home_page.choose_maslul_in_floating_form().click()
            home_page.choose_maslul_real_time_in_floating_form().click()
        if tick_terms_and_services == "yes":
            self.string_message("---Ticking the terms of agreement and services---\n")
            home_page.terms_of_agreement_field_in_floating_form().click()
        if send_button == "yes":
            self.string_message("---Clicking on the 'send' button---\n")
            home_page.send_button_in_floating_form().click()
        # if close_button == "yes":
        #     self.string_message("---Clicking on the close button---\n")
        #     home_page.close_button_after_filling_the_main_form().click()
        self.string_message("---Outside floating_form function---\n")


    def click_on_form_in_floating_menu(self):
        print("---Inside click_on_form_in_floating_menu function...---")
        self.string_result += "---Inside click_on_form_in_floating_menu function---\n"
        home_page = HomePage(self.driver)
        home_page.form_in_floating_menu().click()
        print("---Outside click_on_form_in_floating_menu function...---")
        self.string_result += "---Outside click_on_form_in_floating_menu function---\n"

    def send_keys_to_last_name_field_in_floating_form(self):
        print("---Inside send_keys_to_last_name_field_in_floating_form function---")
        self.string_result += "---Inside send_keys_to_last_name_field_in_floating_form function---\n"
        home_page = HomePage(self.driver)
        home_page.last_name_field_in_floating_form().send_keys(self.test_user_last_name)
        print("---Outside send_keys_to_last_name_field_in_floating_form function---")
        self.string_result += "---Outside send_keys_to_last_name_field_in_floating_form function---\n"

    def send_keys_to_first_name_field_in_floating_form(self):
        print("---Inside send_keys_to_first_name_field_in_floating_form function---")
        self.string_result += "---Inside send_keys_to_first_name_field_in_floating_form function---\n"
        home_page = HomePage(self.driver)
        home_page.first_name_field_in_floating_form().send_keys(self.test_user_first_name)
        print("---Outside send_keys_to_first_name_field_in_floating_form function---")
        self.string_result += "---Outside send_keys_to_first_name_field_in_floating_form function---\n"

    def send_keys_to_mail_field_in_floating_form(self):
        print("---Inside send_keys_to_mail_field_in_floating_form function---")
        self.string_result += "---Inside send_keys_to_mail_field_in_floating_form function---\n"
        home_page = HomePage(self.driver)
        home_page.email_field_in_floating_form().send_keys(self.test_user_mail)
        print("---Outside send_keys_to_mail_field_in_floating_form function---")
        self.string_result += "---Outside send_keys_to_mail_field_in_floating_form function---\n"

    def send_keys_to_phone_number_field_in_floating_form(self):
        print("---Inside send_keys_to_phone_number_field_in_floating_form function---")
        self.string_result += "---Inside send_keys_to_phone_number_field_in_floating_form function---\n"
        home_page = HomePage(self.driver)
        home_page.phone_number_field_in_floating_form().send_keys(self.test_user_phone_number)
        print("---Outside send_keys_to_phone_number_field_in_floating_form function---")
        self.string_result += "---Outside send_keys_to_phone_number_field_in_floating_form function---\n"

    def choose_maslul_real_time_in_floating_form(self):
        print("---Inside choose_maslul_real_time_in_floating_form function---")
        self.string_result += "---Inside choose_maslul_real_time_in_floating_form function---\n"
        home_page = HomePage(self.driver)
        home_page.choose_maslul_in_floating_form().click()
        home_page.choose_maslul_real_time_in_floating_form().click()
        print("---Outside choose_maslul_real_time_in_floating_form function---")
        self.string_result += "---Outside choose_maslul_real_time_in_floating_form function---\n"

    def tick_terms_and_services_button_in_floating_form(self):
        print("---Inside tick_terms_and_services_button_in_floating_form function---")
        self.string_result += "---Inside tick_terms_and_services_button_in_floating_form function---\n"
        home_page = HomePage(self.driver)
        home_page.terms_of_agreement_field_in_floating_form().click()
        print("---Outside tick_terms_and_services_button_in_floating_form function---")
        self.string_result += "---Outside tick_terms_and_services_button_in_floating_form function---\n"

    def click_on_send_button_in_floating_form(self):
        print("---Inside click_on_send_button_in_floating_form function---")
        self.string_result += "---Inside click_on_send_button_in_floating_form function---\n"
        home_page = HomePage(self.driver)
        home_page.send_button_in_floating_form().click()
        print("---Outside click_on_send_button_in_floating_form function---")
        self.string_result += "---Outside click_on_send_button_in_floating_form function---\n"

    def test_floating_menu(self):
        self.close_popup()
        self.floating_form()
        self.open_file_and_append_string_message()
    #     # self.hover_on_floating_menu()
    #     self.click_on_form_in_floating_menu()
    #     self.send_keys_to_last_name_field_in_floating_form()
    #     self.send_keys_to_first_name_field_in_floating_form()
    #     self.send_keys_to_mail_field_in_floating_form()
    #     self.send_keys_to_phone_number_field_in_floating_form()
    #     self.choose_maslul_real_time_in_floating_form()
    #     self.tick_terms_and_services_button_in_floating_form()
    # self.click_on_send_button_in_floating_form()
    # -----------------------------------FLOATING ABOUT US TEST----------------------------

    def click_on_about_us_in_floating_menu(self):
        print("---Inside click_on_about_us_in_floating_menu function...---")
        self.string_result += "---Inside click_on_about_us_in_floating_menu function---\n"
        home_page = HomePage(self.driver)
        home_page.about_us_in_floating_menu().click()
        print("---Outside click_on_about_us_in_floating_menu function...---")
        self.string_result += "---Outside click_on_about_us_in_floating_menu function---\n"

    # def test_floating_about_us(self):
    #     self.hover_on_floating_menu()
    #     self.click_on_about_us_in_floating_menu()


