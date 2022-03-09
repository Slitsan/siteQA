from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from POM.Pages.block import Block


class CoursePage(Block):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(driver)
        # --------------------------------------NAVIGATION BUTTONS-----------------------------------
        self.about_the_course_button_by_xpath = "//*[@id=\"nav-secondary-0\"]/a"
        self.subjects_button_by_xpath = "//*[@id=\"nav-secondary-1\"]/a"
        self.target_audience_and_prior_requirements_button_by_xpath = "//*[@id=\"nav-secondary-2\"]/a"
        self.continous_courses_button_by_xpath = "//*[@id=\"nav-secondary-3\"]/a"
        self.student_opinion_button_by_xpath = "//*[@id=\"nav-secondary-4\"]/a"
        self.articles_button_by_xpath = "//*[@id=\"nav-secondary-5\"]/a"

    # -------------------------------------NAVIGATION BUTTONS METHODS----------------------------------
    def about_the_course_button_in_nav_bar(self):
        return self.driver.find_element(By.XPATH, self.about_the_course_button_by_xpath)

    def subjects_button_in_nav_bar(self):
        return self.driver.find_element(By.XPATH, self.subjects_button_by_xpath)

    def target_audience_and_prior_requirements_button_in_nav_bar(self):
        return self.driver.find_element(By.XPATH, self.target_audience_and_prior_requirements_button_by_xpath)

    def continous_courses_button_in_nav_bar(self):
        return self.driver.find_element(By.XPATH, self.continous_courses_button_by_xpath)

    def student_opinion_button_in_nav_bar(self):
        return self.driver.find_element(By.XPATH, self.student_opinion_button_by_xpath)

    def articles_button_in_nav_bar(self):
        return self.driver.find_element(By.XPATH, self.articles_button_by_xpath)