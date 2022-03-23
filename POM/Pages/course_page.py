from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from POM.Pages.block import Block


class CoursePage(Block):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(driver)
        # --------------------------------------NAVIGATION BUTTONS-----------------------------------
        self.list_of_buttons_in_navigation_by_xpath = "//*[@id='nav-secondary-course']/div/a"
        self.about_the_course_button_by_xpath = "//*[@id=\"nav-secondary-0\"]/a"
        self.subjects_button_by_xpath = "//*[@id=\"nav-secondary-1\"]/a"
        self.target_audience_and_prior_requirements_button_by_xpath = "//*[@id=\"nav-secondary-2\"]/a"
        self.continous_courses_button_by_xpath = "//*[@id=\"nav-secondary-3\"]/a"
        self.student_opinion_button_by_xpath = "//*[@id=\"nav-secondary-4\"]/a"
        self.articles_button_by_xpath = "//*[@id=\"nav-secondary-5\"]/a"
        # -------------------------------------NAVIGATION BLOCK-------------------------------------
        self.about_block_by_xpath = "//*[@id='about']"
        self.course_topics_block_by_xpath = "//*[@id='course-topics']"
        self.target_audience_block_by_xpath = "//*[@id='target-audience']"
        self.follow_up_courses_block_by_xpath = "//*[@id='followup-courses1']"
        self.videos_block_by_xpath = "//*[@id='videos']"
        self.articles_block_by_xpath = "//*[@id='related-articles']"

    # -------------------------------------NAVIGATION BUTTONS METHODS----------------------------------
    def list_of_buttons_in_navigation(self):
        return self.driver.find_elements(By.XPATH, self.list_of_buttons_in_navigation_by_xpath)

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

    # -------------------------------------NAVIGATION BLOCK METHODS-------------------------------------
    def about_block(self):
        return self.driver.find_element(By.XPATH, self.about_block_by_xpath)

    def course_topics_block(self):
        return self.driver.find_element(By.XPATH, self.course_topics_block_by_xpath)

    def target_audience_block(self):
        return self.driver.find_element(By.XPATH, self.target_audience_block_by_xpath)

    def follow_up_courses_block(self):
        return self.driver.find_element(By.XPATH, self.follow_up_courses_block_by_xpath)

    def videos_block(self):
        return self.driver.find_element(By.XPATH, self.videos_block_by_xpath)

    def articles_block(self):
        return self.driver.find_element(By.XPATH, self.articles_block_by_xpath)