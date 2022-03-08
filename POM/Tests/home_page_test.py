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
        cls.test_user_last_name = "test"
        cls.test_user_first_name = "test"
        cls.test_user_mail = current_time + "@test.com"
        cls.test_user_phone_number = current_time

    # ---------------------------------POPUP TEST-----------------------------------------
    def send_keys_to_last_name_field_in_popup(self):
        print("---Inside send_keys_to_last_name_field_in_popup function---")
        home_page = HomePage(self.driver)
        home_page.last_name_field_in_form_popup().send_keys(self.test_user_last_name)
        print("---Outside send_keys_to_last_name_field_in_popup function---")

    def send_keys_to_first_name_field_in_popup(self):
        print("---Inside send_keys_to_first_name_field_in_popup function---")
        home_page = HomePage(self.driver)
        home_page.first_name_field_in_form_popup().send_keys(self.test_user_first_name)
        print("---Outside send_keys_to_first_name_field_in_popup function---")

    def send_keys_to_mail_field_in_popup(self):
        print("---Inside send_keys_to_mail_field_in_popup function---")
        home_page = HomePage(self.driver)
        home_page.email_field_in_form_popup().send_keys(self.test_user_mail)
        print("---Outside send_keys_to_mail_field_in_popup function---")

    def send_keys_to_phone_number_field_in_popup(self):
        print("---Inside send_keys_to_phone_number_field_in_popup function---")
        home_page = HomePage(self.driver)
        home_page.phone_field_in_form_popup().send_keys(self.test_user_phone_number)
        print("---Outside send_keys_to_phone_number_field_in_popup function---")

    def choose_maslul_real_time_in_popup(self):
        print("---Inside choose_maslul_real_time_in_popup function---")
        home_page = HomePage(self.driver)
        home_page.choose_maslul_in_form_popup().click()
        home_page.choose_maslul_real_time_in_form_popup().click()
        print("---Outside choose_maslul_real_time_in_popup function---")

    def tick_terms_and_services_button_in_popup(self):
        print("---Inside tick_terms_and_services_button_in_popup function---")
        home_page = HomePage(self.driver)
        home_page.terms_of_agreement_field_in_form_popup().click()
        print("---Outside tick_terms_and_services_button_in_popup function---")

    def click_on_send_button_in_popup(self):
        print("---Inside click_on_send_button_in_popup function---")
        home_page = HomePage(self.driver)
        home_page.send_button_in_form_popup().click()
        print("---Outside click_on_send_button_in_popup function---")

    def close_popup(self):
        print("---Inside wait_for_popup function---")
        home_page = HomePage(self.driver)
        time.sleep(12)
        home_page.close_button_in_popup_form().click()
        print("---Outside wait_for_popup function---")

    # def test_popup_form(self):
    # self.send_keys_to_last_name_field_in_popup()
    # self.send_keys_to_first_name_field_in_popup()
    # self.send_keys_to_mail_field_in_popup()
    # self.send_keys_to_phone_number_field_in_popup()
    # self.choose_maslul_real_time_in_popup()
    # self.tick_terms_and_services_button_in_popup()
    # self.click_on_send_button_in_popup()
    # self.close_popup()

    # -----------------------------------------MAIN FORM TEST---------------------------------------
    def send_keys_to_last_name_field_in_main_form(self):
        print("---Inside send_keys_to_last_name_field_in_main_form function---")
        home_page = HomePage(self.driver)
        home_page.last_name_field_in_main_form().send_keys(self.test_user_last_name)
        print("---Outside send_keys_to_last_name_field_in_main_form function---")

    def send_keys_to_first_name_field_in_main_form(self):
        print("---Inside send_keys_to_first_name_field_in_main_form function---")
        home_page = HomePage(self.driver)
        home_page.first_name_field_in_main_form().send_keys(self.test_user_first_name)
        print("---Outside send_keys_to_first_name_field_in_main_form function---")

    def send_keys_to_mail_field_in_main_form(self):
        print("---Inside send_keys_to_mail_field_in_main_form function---")
        home_page = HomePage(self.driver)
        home_page.email_field_in_main_form().send_keys(self.test_user_mail)
        print("---Outside send_keys_to_mail_field_in_main_form function---")

    def send_keys_to_phone_number_field_in_main_form(self):
        print("---Inside send_keys_to_phone_number_field_in_main_form function---")
        home_page = HomePage(self.driver)
        home_page.phone_number_field_in_main_form().send_keys(self.test_user_phone_number)
        print("---Outside send_keys_to_phone_number_field_in_main_form function---")

    def choose_maslul_real_time_in_main_form(self):
        print("---Inside choose_maslul_real_time_in_main_form function---")
        home_page = HomePage(self.driver)
        home_page.choose_maslul_in_main_form().click()
        home_page.choose_maslul_real_time_in_main_form().click()
        print("---Outside choose_maslul_real_time_in_main_form function---")

    def tick_terms_and_services_button_in_main_form(self):
        print("---Inside tick_terms_and_services_button_in_main_form function---")
        home_page = HomePage(self.driver)
        home_page.terms_of_agreement_field_in_main_form().click()
        print("---Outside tick_terms_and_services_button_in_main_form function---")

    def click_on_send_button_in_main_form(self):
        print("---Inside click_on_send_button_in_main_form function---")
        home_page = HomePage(self.driver)
        home_page.send_button_in_main_form().click()
        print("---Outside click_on_send_button_in_main_form function---")

    # def test_main_form(self):
    #     self.close_popup()
    #     self.send_keys_to_last_name_field_in_main_form()
    #     self.send_keys_to_first_name_field_in_main_form()
    #     self.send_keys_to_mail_field_in_main_form()
    #     self.send_keys_to_phone_number_field_in_main_form()
    #     self.choose_maslul_real_time_in_main_form()
    #     self.tick_terms_and_services_button_in_main_form()
    #     self.click_on_send_button_in_main_form()
    # -----------------------------------FLOATING FORM TEST-------------------------------

    def hover_on_floating_menu(self):
        print("---Inside click_on_floating_menu function...---")
        home_page = HomePage(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.floating_menu()).perform()
        # home_page.floating_menu().click()
        print("---Outside click_on_floating_menu function...---")

    def click_on_form_in_floating_menu(self):
        print("---Inside click_on_form_in_floating_menu function...---")
        home_page = HomePage(self.driver)
        home_page.form_in_floating_menu().click()
        print("---Outside click_on_form_in_floating_menu function...---")

    def send_keys_to_last_name_field_in_floating_form(self):
        print("---Inside send_keys_to_last_name_field_in_floating_form function---")
        home_page = HomePage(self.driver)
        home_page.last_name_field_in_floating_form().send_keys(self.test_user_last_name)
        print("---Outside send_keys_to_last_name_field_in_floating_form function---")

    def send_keys_to_first_name_field_in_floating_form(self):
        print("---Inside send_keys_to_first_name_field_in_floating_form function---")
        home_page = HomePage(self.driver)
        home_page.first_name_field_in_floating_form().send_keys(self.test_user_first_name)
        print("---Outside send_keys_to_first_name_field_in_floating_form function---")

    def send_keys_to_mail_field_in_floating_form(self):
        print("---Inside send_keys_to_mail_field_in_floating_form function---")
        home_page = HomePage(self.driver)
        home_page.email_field_in_floating_form().send_keys(self.test_user_mail)
        print("---Outside send_keys_to_mail_field_in_floating_form function---")

    def send_keys_to_phone_number_field_in_floating_form(self):
        print("---Inside send_keys_to_phone_number_field_in_floating_form function---")
        home_page = HomePage(self.driver)
        home_page.phone_number_field_in_floating_form().send_keys(self.test_user_phone_number)
        print("---Outside send_keys_to_phone_number_field_in_floating_form function---")

    def choose_maslul_real_time_in_floating_form(self):
        print("---Inside choose_maslul_real_time_in_floating_form function---")
        home_page = HomePage(self.driver)
        home_page.choose_maslul_in_floating_form().click()
        home_page.choose_maslul_real_time_in_floating_form().click()
        print("---Outside choose_maslul_real_time_in_floating_form function---")

    def tick_terms_and_services_button_in_floating_form(self):
        print("---Inside tick_terms_and_services_button_in_floating_form function---")
        home_page = HomePage(self.driver)
        home_page.terms_of_agreement_field_in_floating_form().click()
        print("---Outside tick_terms_and_services_button_in_floating_form function---")

    def click_on_send_button_in_floating_form(self):
        print("---Inside click_on_send_button_in_floating_form function---")
        home_page = HomePage(self.driver)
        home_page.send_button_in_floating_form().click()
        print("---Outside click_on_send_button_in_floating_form function---")

    # def test_floating_menu(self):
    #     self.hover_on_floating_menu()
    #     self.click_on_form_in_floating_menu()
    #     self.send_keys_to_last_name_field_in_floating_form()
    #     self.send_keys_to_first_name_field_in_floating_form()
    #     self.send_keys_to_mail_field_in_floating_form()
    #     self.send_keys_to_phone_number_field_in_floating_form()
    #     self.choose_maslul_real_time_in_floating_form()
    #     self.tick_terms_and_services_button_in_floating_form()
        #self.click_on_send_button_in_floating_form()
    # -----------------------------------FLOATING ABOUT US TEST----------------------------

    def click_on_about_us_in_floating_menu(self):
        print("---Inside click_on_about_us_in_floating_menu function...---")
        home_page = HomePage(self.driver)
        home_page.about_us_in_floating_menu().click()
        print("---Outside click_on_about_us_in_floating_menu function...---")

    # def test_floating_about_us(self):
    #     self.hover_on_floating_menu()
    #     self.click_on_about_us_in_floating_menu()


if __name__ == '__main__':
    unittest.main()
