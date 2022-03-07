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