from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Block:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # ------------------------------------DOWNLOAD SYLLABUS BUTTON--------------------------------------
        self.download_syllabus_button_by_xpath = "//*[contains(text(), 'להורדת הסילבוס')]"
        self.choose_language_of_syllabus_by_xpath = "//*[@id=\"choose-language\"]/div"
        self.languages_of_syllabus_by_xpath = "//*[@id=\"choose-language\"]/div/div[2]/button"
        self.close_button_of_choosing_languange_of_syllabus_by_xpath = "//*[@id=\"choose-language\"]/span"

        # -----------------------------------FORM AFTER CLICKING ON SYLLABUS----------------------------
        self.form_after_clicking_on_syllabus_by_xpath = "//*[@id=\"lead-form-modal\"]/div/div[2]"
        self.last_name_field_in_form_after_syllabus_by_path = "//*[@id=\"lead-form-modal\"] /descendant::input[@id='lname']"
        self.first_name_field_in_form_after_syllabus_by_path = "//*[@id=\"lead-form-modal\"] /descendant::input[@id='fname']"
        self.email_field_in_form_after_syllabus_by_path = "//*[@id=\"lead-form-modal\"] /descendant::input[@id='email']"
        self.phone_number_field_in_form_after_syllabus_by_path = "//*[@id=\"lead-form-modal\"] /descendant::input[@id='phone']"
        self.choose_maslul_field_in_form_after_syllabus_by_path = "//*[@id=\"lead-form-modal\"] /descendant::select"
        self.choose_maslul_real_time_in_form_after_syllabus_by_path = "//*[@id=\"lead-form-modal\"] /descendant::option[2]"
        self.terms_of_agreement_in_form_after_syllabus_by_xpath = "//*[@id=\"lead-form-modal\"] /descendant::input[@class='px-2']"
        self.send_button_in_form_after_syllabus_by_xpath = "//*[@id=\"lead-form-modal\"] /descendant::button"
        self.close_button_for_not_filling_in_details_in_form_by_xpath = "//*[@id=\"modal-0\"]/div/span"
        self.close_button_of_form_after_syllabus_by_xpath = "//*[@id=\"lead-form-modal\"]/span"

        # ----------------------------------SIDE FORM UNDER SYLLABUS-------------------------------
        self.last_name_field_in_form_under_syllabus_by_xpath = "//*[@class='pr-3 bluee-color'] /descendant::input[@id='lname']"
        self.first_name_field_in_form_under_syllabus_by_xpath = "//*[@class='pr-3 bluee-color'] /descendant::input[@id='fname']"
        self.email_field_in_form_under_syllabus_by_xpath = "//*[@class='pr-3 bluee-color'] /descendant::input[@id='email']"
        self.phone_field_in_form_under_syllabus_by_xpath = "//*[@class='pr-3 bluee-color'] /descendant::input[@id='phone']"
        self.choose_maslul_field_in_form_under_syllabus_by_xpath = "//*[@class='pr-3 bluee-color'] /descendant::select"
        self.choose_maslul_real_time_field_in_form_under_syllabus_by_xpath = "//*[@class='pr-3 bluee-color'] /descendant::option[2]"
        self.agreement_of_terms_and_services_field_in_form_under_syllabus_by_xpath = "//*[@class='pr-3 bluee-color'] /descendant::input[@type='checkbox']"
        self.send_button_in_form_under_syllabus_by_xpath = "//*[@class='pr-3 bluee-color'] /descendant::button"
        self.close_button_after_filling_details_in_form_under_syllabus_by_xpath = "//*[@class='pr-3 bluee-color'] /descendant::span"

        # -------------------------------------------DIV BLOCKS---------------------------------------
        self.salary_block_by_xpath = "//*[@id='salary-selector-target']"
        self.table_list_of_salary_block_by_xpath = "//*[@id='salary-selector-target'] /descendant::tbody/tr"
        self.list_of_p_blocks_in_salary_block_by_xpath = "//*[@id='salary-selector-target'] /descendant::p"
        self.faq_block_by_xpath = "//*[@id='faq-selector']"
        self.list_of_div_blocks_in_faq_by_xpath = "//*[@id='faq_accordion'] //div[@class='card-header']/span"

    # ----------------------------------------FORM AFTER CLICKING ON SYLLABUS METHODS--------------------------------------
    def form_after_clicking_on_syllabus(self):
        return self.driver.find_element(By.XPATH, self.form_after_clicking_on_syllabus_by_xpath)

    def last_name_field_in_side_form_after_clicking_on_syllabus(self):
        return self.driver.find_element(By.XPATH, self.last_name_field_in_form_after_syllabus_by_path)

    def first_name_field_in_side_form_after_clicking_on_syllabus(self):
        return self.driver.find_element(By.XPATH, self.first_name_field_in_form_after_syllabus_by_path)

    def email_field_in_side_form_after_clicking_on_syllabus(self):
        return self.driver.find_element(By.XPATH, self.email_field_in_form_after_syllabus_by_path)

    def phone_number_field_in_side_form_after_clicking_on_syllabus(self):
        return self.driver.find_element(By.XPATH, self.phone_number_field_in_form_after_syllabus_by_path)

    def choose_maslul_field_in_side_form_after_clicking_on_syllabus(self):
        return self.driver.find_element(By.XPATH, self.choose_maslul_field_in_form_after_syllabus_by_path)

    def choose_maslul_real_time_in_side_form_after_clicking_on_syllabus(self):
        return self.driver.find_element(By.XPATH, self.choose_maslul_real_time_in_form_after_syllabus_by_path)

    def tick_terms_of_agreement_in_side_form_after_clicking_on_syllabus(self):
        return self.driver.find_element(By.XPATH, self.terms_of_agreement_in_form_after_syllabus_by_xpath)

    def send_button_in_side_form_after_clicking_on_syllabus(self):
        return self.driver.find_element(By.XPATH, self.send_button_in_form_after_syllabus_by_xpath)

    def close_button_for_not_filling_in_details_in_form(self):
        return self.driver.find_element(By.XPATH, self.close_button_for_not_filling_in_details_in_form_by_xpath)

    def close_button_of_form_after_syllabus(self):
        return self.driver.find_element(By.XPATH, self.close_button_of_form_after_syllabus_by_xpath)

    # --------------------------------------------SYLLABUS METHODS---------------------------------
    def download_syllabus(self):
        return self.driver.find_element(By.XPATH, self.download_syllabus_button_by_xpath)

    def choose_language_of_syllabus(self):
        return self.driver.find_element(By.XPATH, self.choose_language_of_syllabus_by_xpath)

    def languages_of_syllabus(self):
        return self.driver.find_elements(By.XPATH, self.languages_of_syllabus_by_xpath)

    def close_button_of_choosing_languange_of_syllabus(self):
        return self.driver.find_element(By.XPATH, self.close_button_of_choosing_languange_of_syllabus_by_xpath)

    # ------------------------------------SIDE FORM UNDER SYLLABUS METHODS-----------------------------
    def last_name_field_in_form_under_syllabus(self):
        return self.driver.find_element(By.XPATH, self.last_name_field_in_form_under_syllabus_by_xpath)

    def first_name_field_in_form_under_syllabus(self):
        return self.driver.find_element(By.XPATH, self.first_name_field_in_form_under_syllabus_by_xpath)

    def email_field_in_form_under_syllabus(self):
        return self.driver.find_element(By.XPATH, self.email_field_in_form_under_syllabus_by_xpath)

    def phone_field_in_form_under_syllabus(self):
        return self.driver.find_element(By.XPATH, self.phone_field_in_form_under_syllabus_by_xpath)

    def choose_maslul_field_in_form_under_syllabus(self):
        return self.driver.find_element(By.XPATH, self.choose_maslul_field_in_form_under_syllabus_by_xpath)

    def choose_maslul_real_time_field_in_form_under_syllabus(self):
        return self.driver.find_element(By.XPATH, self.choose_maslul_real_time_field_in_form_under_syllabus_by_xpath)

    def agreement_of_terms_and_services_field_in_form_under_syllabus(self):
        return self.driver.find_element(By.XPATH, self.agreement_of_terms_and_services_field_in_form_under_syllabus_by_xpath)

    def send_button_in_form_under_syllabus(self):
        return self.driver.find_element(By.XPATH, self.send_button_in_form_under_syllabus_by_xpath)

    def close_button_after_filling_details_in_form_under_syllabus(self):
        return self.driver.find_element(By.XPATH, self.close_button_after_filling_details_in_form_under_syllabus_by_xpath)

    # -------------------------------------------DIV BLOCKS METHODS---------------------------------------
    def salary_block(self):
        return self.driver.find_element(By.XPATH, self.salary_block_by_xpath)

    def table_list_of_salary_block(self):
        return self.driver.find_elements(By.XPATH, self.table_list_of_salary_block_by_xpath)

    def list_of_p_blocks_in_salary_block(self):
        return self.driver.find_elements(By.XPATH, self.list_of_p_blocks_in_salary_block_by_xpath)

    def faq_block(self):
        return self.driver.find_element(By.XPATH, self.faq_block_by_xpath)

    def list_of_div_blocks_in_faq(self):
        return self.driver.find_elements(By.XPATH, self.list_of_div_blocks_in_faq_by_xpath)