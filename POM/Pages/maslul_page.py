from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from POM.Pages.block import Block


class MaslulPage(Block):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(driver)
        # -------------------------------NAVIGATION BUTTONS-----------------------------------
        self.about_the_course_button_by_xpath = "//*[@id=\"nav-secondary-0\"]/a"
        self.structure_of_maslul_by_xpath = "//*[@id=\"nav-secondary-1\"]/a"
        self.target_audience_and_prior_requirements_by_xpath = "//*[@id=\"nav-secondary-2\"]/a"
        self.to_study_with_us_by_xpath = "//*[@id=\"nav-secondary-3\"]/a"
        self.graduate_diploma_by_xpath = "//*[@id=\"nav-secondary-4\"]/a"
        self.questions_and_answers_by_xpath = "//*[@id=\"nav-secondary-5\"]/a"

    # -------------------------------------NAVIGATION BUTTONS METHODS--------------------------------
    def about_the_course_button_in_nav_bar(self):
        self.driver.find_element(By.XPATH, self.about_the_course_button_by_xpath)

    def structure_of_maslul_button_in_nav_bar(self):
        self.driver.find_element(By.XPATH, self.structure_of_maslul_by_xpath)

    def target_audience_and_prior_requirements_button_in_nav_bar(self):
        self.driver.find_element(By.XPATH, self.target_audience_and_prior_requirements_by_xpath)

    def to_study_with_us_button_in_nav_bar(self):
        self.driver.find_element(By.XPATH, self.to_study_with_us_by_xpath)

    def graduate_diploma_button_in_nav_bar(self):
        self.driver.find_element(By.XPATH, self.graduate_diploma_by_xpath)

    def questions_and_answers_button_in_nav_bar(self):
        self.driver.find_element(By.XPATH, self.questions_and_answers_by_xpath)
