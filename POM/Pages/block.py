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

        # -----------------------------------SIDE FORM UNDER SYLLABUS----------------------------
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

    # ----------------------------------------SIDE FORM METHODS--------------------------------------
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