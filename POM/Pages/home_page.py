from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class HomePage:
    def __init__(self, drive: WebDriver):
        self.driver = drive
        # -------------------------------POPUP----------------------------------------------------------------------
        self.popup_form_by_xpath = "//*[@id=\"rt-leads-form-1\"]"
        self.close_button_in_popup_form_by_xpath = "//*[@id=\"lead-form-modal1\"]/span"
        self.last_name_field_in_form_popup_by_xpath = "//*[@id='rt-leads-form-1'] /descendant::input[2]"
        self.first_name_field_in_form_popup_by_xpath = "//*[@id='rt-leads-form-1'] /descendant::input[1]"
        self.email_field_in_form_popup_by_xpath = "//*[@id='rt-leads-form-1'] /descendant::input[3]"
        self.phone_field_in_form_popup_by_xpath = "//*[@id='rt-leads-form-1'] /descendant::input[4]"
        self.choose_maslul_in_form_popup_by_xpath = "//*[@id='rt-leads-form-1'] /descendant::select"
        self.maslul_real_time_in_form_popup_by_xpath = "//*[@id='rt-leads-form-1'] /descendant::select/option[2]"
        self.terms_of_agreement_field_in_form_popup_by_xpath = "//*[@id='rt-leads-form-1'] /descendant::input[5]"
        self.send_button_in_form_popup_by_xpath = "//*[@id='rt-leads-form-1'] /descendant::button"
        # -------------------------------------------MAIN FORM-------------------------------------------------------
        self.last_name_field_in_main_form_by_xpath = "//*[@id='rt-leads-form-2'] /descendant::input[2]"
        self.first_name_field_in_main_form_by_xpath = "//*[@id='rt-leads-form-2'] /descendant::input[1]"
        self.phone_number_field_in_main_form_by_xpath = "//*[@id='rt-leads-form-2'] /descendant::input[4]"
        self.email_field_in_main_form_by_xpath = "//*[@id='rt-leads-form-2'] /descendant::input[3]"
        self.terms_of_agreement_field_in_main_form_by_xpath = "//*[@id='rt-leads-form-2'] /descendant::input[5]"
        self.choose_maslul_in_main_form_by_xpath = "//*[@id='rt-leads-form-2'] /descendant::select"
        self.maslul_real_time_in_main_form_by_xpath = "//*[@id='rt-leads-form-2'] /descendant::select/option[2]"
        self.send_button_in_main_form_by_xpath = "//*[@id='rt-leads-form-2'] /descendant::button"
        self.close_button_after_filling_the_main_form_by_xpath = "//*[@id=\"modal-2\"]/div/span"
        # -----------------------------------------FLOATING FORM---------------------------------------------------
        self.floating_menu_by_xpath = "//*[@id=\"floating-form\"]"
        self.whatsup_link_in_floating_menu_by_xpath = "//*[@id='floating-form'] /descendant::div[1]"
        self.about_us_in_floating_menu_by_xpath = "//*[@id='floating-form'] /descendant::div[2]"
        self.form_in_floating_menu_by_xpath = "//*[@id='floating-form'] /descendant::div[3]"
        self.last_name_in_floating_form_by_xpath = "//*[@id=\"lead-form-modal\"] /descendant::input[@id='lname']"
        self.first_name_in_floating_form_by_xpath = "//*[@id=\"lead-form-modal\"] /descendant::input[@id='fname']"
        self.phone_number_in_floating_form_by_xpath = "//*[@id=\"lead-form-modal\"] /descendant::input[@id='phone']"
        self.email_in_floating_form_by_xpath = "//*[@id=\"lead-form-modal\"] /descendant::input[@id='email']"
        self.choose_maslul_in_floating_form_by_xpath = "//*[@id=\"lead-form-modal\"] /descendant::select"
        self.choose_maslul_real_time_in_floating_form_by_xpath = "//*[@id=\"lead-form-modal\"] /descendant::option[2]"
        self.terms_of_agreement_in_floating_form_by_xpath = "//*[@id=\"lead-form-modal\"] /descendant::input[@class='px-2']"
        self.send_button_in_floating_form_by_xpath = "//*[@id=\"lead-form-modal\"] /descendant::button"
        # ----------------------------TRAINING AND PLACEMENT TRACKS FOR HIGH-TECH PROFESSIONS------------------------
        self.training_and_placement_tracks_for_high_tech_professions_by_xpath = "//*[@id='all-categories-cards'] /descendant::a"
        self.real_time_embedded_on_home_page_by_xpath = "//*[@id='all-categories-card-0'] /descendant::a"
        self.cyber_security_on_home_page_by_xpath = "//*[@id='all-categories-card-1'] /descendant::a"
        self.full_stack_development_on_home_page_by_xpath = "//*[@id='all-categories-card-2'] /descendant::a"
        self.devops_on_home_page_by_xpath = "//*[@id='all-categories-card-3'] /descendant::a"
        self.automation_and_qa_on_home_page_by_xpath = "//*[@id='all-categories-card-4'] /descendant::a"
        self.machine_learning_on_home_page_by_xpath = "//*[@id='all-categories-card-5'] /descendant::a"
        # ------------------------------------LIST OF COURSES ON MASLULIM ON HOME PAGE--------------------------------
        self.list_of_courses_on_bootcamp_real_time_on_home_page_by_xpath = "//*[@id='all-paths-item-0'] /descendant::div/a[@class='text-dark']"
        self.list_of_courses_on_bootcamp_fullstack_on_home_page_by_xpath = "//*[@id='all-paths-item-1'] /descendant::div/a[@class='text-dark']"
        self.list_of_courses_on_bootcamp_qa_on_home_page_by_xpath = "//*[@id='all-paths-item-2'] /descendant::div/a[@class='text-dark']"
        self.list_of_courses_on_bootcamp_cyber_security_on_home_page_by_xpath = "//*[@id='all-paths-item-3'] /descendant::div/a[@class='text-dark']"
        self.list_of_courses_on_bootcamp_machine_learning_on_home_page_by_xpath = "//*[@id='all-paths-item-4'] /descendant::div/a[@class='text-dark']"
        # -------------------------------------DEPARTMENT BUTTONS ------------------------------------------------------
        self.development_apartment_by_xpath = "//*[local-name()='svg' and @class='mx-auto'] //*[local-name()='a'][1]"
        self.teaching_apartment_by_xpath = "//*[local-name()='svg' and @class='mx-auto'] //*[local-name()='a'][2]"
        self.hr_apartment_by_xpath = "//*[local-name()='svg' and @class='mx-auto'] //*[local-name()='a'][3]"

    # --------------------------------POPUP METHODS---------------------------------------------------
    def popup_form(self):
        return self.driver.find_element(By.XPATH, self.popup_form_by_xpath)

    def close_button_in_popup_form(self):
        return self.driver.find_element(By.XPATH, self.close_button_in_popup_form_by_xpath)

    def last_name_field_in_form_popup(self):
        return self.driver.find_element(By.XPATH, self.last_name_field_in_form_popup_by_xpath)

    def first_name_field_in_form_popup(self):
        return self.driver.find_element(By.XPATH, self.first_name_field_in_form_popup_by_xpath)

    def email_field_in_form_popup(self):
        return self.driver.find_element(By.XPATH, self.email_field_in_form_popup_by_xpath)

    def phone_field_in_form_popup(self):
        return self.driver.find_element(By.XPATH, self.phone_field_in_form_popup_by_xpath)

    def choose_maslul_in_form_popup(self):
        return self.driver.find_element(By.XPATH, self.choose_maslul_in_form_popup_by_xpath)

    def choose_maslul_real_time_in_form_popup(self):
        return self.driver.find_element(By.XPATH, self.maslul_real_time_in_form_popup_by_xpath)

    def terms_of_agreement_field_in_form_popup(self):
        return self.driver.find_element(By.XPATH, self.terms_of_agreement_field_in_form_popup_by_xpath)

    def send_button_in_form_popup(self):
        return self.driver.find_element(By.XPATH, self.send_button_in_form_popup_by_xpath)

    # -----------------------------------------MAIN FORM METHODS------------------------------------------
    def last_name_field_in_main_form(self):
        return self.driver.find_element(By.XPATH, self.last_name_field_in_main_form_by_xpath)

    def first_name_field_in_main_form(self):
        return self.driver.find_element(By.XPATH, self.first_name_field_in_main_form_by_xpath)

    def phone_number_field_in_main_form(self):
        return self.driver.find_element(By.XPATH, self.phone_number_field_in_main_form_by_xpath)

    def email_field_in_main_form(self):
        return self.driver.find_element(By.XPATH, self.email_field_in_main_form_by_xpath)

    def choose_maslul_in_main_form(self):
        return self.driver.find_element(By.XPATH, self.choose_maslul_in_main_form_by_xpath)

    def choose_maslul_real_time_in_main_form(self):
        return self.driver.find_element(By.XPATH, self.maslul_real_time_in_main_form_by_xpath)

    def terms_of_agreement_field_in_main_form(self):
        return self.driver.find_element(By.XPATH, self.terms_of_agreement_field_in_main_form_by_xpath)

    def send_button_in_main_form(self):
        return self.driver.find_element(By.XPATH, self.send_button_in_main_form_by_xpath)

    def close_button_after_filling_the_main_form(self):
        return self.driver.find_element(By.XPATH, self.close_button_after_filling_the_main_form_by_xpath)

    # --------------------------------------FLOATING FORM METHODS-----------------------------------------
    def floating_menu(self):
        return self.driver.find_element(By.XPATH, self.floating_menu_by_xpath)

    def about_us_in_floating_menu(self):
        return self.driver.find_element(By.XPATH, self.about_us_in_floating_menu_by_xpath)

    def whatsup_link_in_floating_menu(self):
        return self.driver.find_element(By.XPATH, self.whatsup_link_in_floating_menu_by_xpath)

    def form_in_floating_menu(self):
        return self.driver.find_element(By.XPATH, self.form_in_floating_menu_by_xpath)

    def last_name_field_in_floating_form(self):
        return self.driver.find_element(By.XPATH, self.last_name_in_floating_form_by_xpath)

    def first_name_field_in_floating_form(self):
        return self.driver.find_element(By.XPATH, self.first_name_in_floating_form_by_xpath)

    def phone_number_field_in_floating_form(self):
        return self.driver.find_element(By.XPATH, self.phone_number_in_floating_form_by_xpath)

    def email_field_in_floating_form(self):
        return self.driver.find_element(By.XPATH, self.email_in_floating_form_by_xpath)

    def choose_maslul_in_floating_form(self):
        return self.driver.find_element(By.XPATH, self.choose_maslul_in_floating_form_by_xpath)

    def choose_maslul_real_time_in_floating_form(self):
        return self.driver.find_element(By.XPATH, self.choose_maslul_real_time_in_floating_form_by_xpath)

    def terms_of_agreement_field_in_floating_form(self):
        return self.driver.find_element(By.XPATH, self.terms_of_agreement_in_floating_form_by_xpath)

    def send_button_in_floating_form(self):
        return self.driver.find_element(By.XPATH, self.send_button_in_floating_form_by_xpath)

    # ----------------------------TRAINING AND PLACEMENT TRACKS FOR HIGH-TECH PROFESSIONS METHOD------------------------
    def training_and_placement_tracks_for_high_tech_professions(self):
        return self.driver.find_elements(By.XPATH,
                                         self.training_and_placement_tracks_for_high_tech_professions_by_xpath)

    def real_time_embedded_on_home_page(self):
        return self.driver.find_element(By.XPATH, self.real_time_embedded_on_home_page_by_xpath)

    def cyber_security_on_home_page(self):
        return self.driver.find_element(By.XPATH, self.cyber_security_on_home_page_by_xpath)

    def full_stack_development_on_home_page(self):
        return self.driver.find_element(By.XPATH, self.full_stack_development_on_home_page_by_xpath)

    def devops_on_home_page(self):
        return self.driver.find_element(By.XPATH, self.devops_on_home_page_by_xpath)

    def automation_and_qa_on_home_page(self):
        return self.driver.find_element(By.XPATH, self.automation_and_qa_on_home_page_by_xpath)

    def machine_learning_on_home_page(self):
        return self.driver.find_element(By.XPATH, self.machine_learning_on_home_page_by_xpath)

    # ------------------------------------LIST OF COURSES ON MASLULIM ON HOME PAGE METHOD-------------------------------
    def list_of_courses_on_bootcamp_real_time_on_home_page(self):
        return self.driver.find_elements(By.XPATH, self.list_of_courses_on_bootcamp_real_time_on_home_page_by_xpath)

    def list_of_courses_on_bootcamp_fullstack_on_home_page(self):
        return self.driver.find_elements(By.XPATH, self.list_of_courses_on_bootcamp_fullstack_on_home_page_by_xpath)

    def list_of_courses_on_bootcamp_qa_on_home_page(self):
        return self.driver.find_elements(By.XPATH, self.list_of_courses_on_bootcamp_qa_on_home_page_by_xpath)

    def list_of_courses_on_bootcamp_cyber_security_on_home_page(self):
        return self.driver.find_elements(By.XPATH, self.list_of_courses_on_bootcamp_cyber_security_on_home_page_by_xpath)

    def list_of_courses_on_bootcamp_machine_learning_on_home_page(self):
        return self.driver.find_elements(By.XPATH, self.list_of_courses_on_bootcamp_machine_learning_on_home_page_by_xpath)

    # -------------------------------------DEPARTMENT BUTTONS METHODS---------------------------------------------------
    def development_apartment(self):
        return self.driver.find_element(By.XPATH, self.development_apartment_by_xpath)

    def teaching_apartment(self):
        return self.driver.find_element(By.XPATH, self.teaching_apartment_by_xpath)

    def hr_apartment(self):
        return self.driver.find_element(By.XPATH, self.hr_apartment_by_xpath)