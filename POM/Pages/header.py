from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with

class Header:

    def __init__(self, drive: WebDriver):
        self.list_of_five_buttons = None
        self.driver = drive

        self.popUp_close_xpath = '//*[@id="lead-form-modal1"]/span'

        self.studentPortal_id = 'student-portal'
        self.search_textbox_id = 'nav-search-string'
        self.search_btn_class = 'btn btn-outline-light order-2 my-2 my-sm-0 col-3'

        self.maslulim_byTXT = 'מסלולים'
        self.courses_byTXT = 'קורסים'
        self.courses_for_companies_by_txt = "קורסים לחברות"
        self.articles_by_txt = "מאמרים"
        self.about_us_by_txt = "אודות"
        self.declaration_of_accessibility_by_txt = "הצהרת נגישות"
        self.jobs_by_txt = "דרושים"
        # ----------------------- MASLULIM --------------------------
        self.maslulim_categories_by_xpath = "//*[@id=\"primar-menu\"]/li[7]/ul/li"
        self.maslul_real_time_by_xpath = "//*[@id=\"RT\"]"
        self.course_real_time_by_xpath = "//*[@id=\"RT\"]/ul/li"
        self.maslul_full_stack_by_xpath = "//*[@id=\"FS\"]"
        self.full_stack_courses_by_xpath = "//*[@id=\"FS\"]/ul/li"
        self.maslul_cyber_by_xpath = "//*[@id=\"Cyber\"]"
        self.cyber_courses_by_xpath = "//*[@id=\"Cyber\"]/ul/li"
        self.maslul_machine_learning_by_xpath = "//*[@id=\"ML\"]"
        self.machine_learning_courses_by_xpath = "//*[@id=\"ML\"]/ul/li"
        self.maslul_qa_by_xpath = "//*[@id=\"QA\"]"
        self.qa_courses_by_xpath = "//*[@id=\"QA\"]/ul/li"
        self.maslul_dev_ops_by_xpath = "//*[@id='QA'] /following-sibling::li[1]"
        self.dev_ops_courses_by_xpath = "//*[@id='QA'] /following-sibling::li[1]/ul/li"
        self.maslul_linux_servers_by_xpath = "//*[@id='IT']"
        self.linux_servers_courses_by_xpath = "//*[@id='IT']/ul/li"
        # ----------------------- COURSES -----------------------------
        self.courses_tab_by_xpath = "//*[@id=\"primar-menu\"]/li[6]"
        self.course_real_time_by_xpath = "//*[@id=\"Real time\"]"
        self.real_time_sub_courses_by_xpath = "//*[@id=\"Real time\"]/ul/li"

    def get_title(self) -> str:
        return self.driver.title

    def goToMaslul(self):
        self.driver.find_element(By.LINK_TEXT, self.maslulim_byTXT).click()

    def goToStudentPortal(self) -> WebDriver:
        self.driver.find_element(By.ID, self.studentPortal_id).click()
        return self.driver

    def go_to_courses_for_companies(self) -> str:
        self.driver.find_element(By.LINK_TEXT, self.courses_for_companies_by_txt).click()
        return self.get_title()

    def go_to_articles(self) -> str:
        self.driver.find_element(By.LINK_TEXT, self.articles_by_txt).click()
        return self.get_title()

    def go_to_about_us(self) -> str:
        self.driver.find_element(By.LINK_TEXT, self.about_us_by_txt).click()
        return self.get_title()

    def go_to_declaration_of_accessibility(self) -> str:
        self.driver.find_element(By.LINK_TEXT, self.declaration_of_accessibility_by_txt).click()
        return self.get_title()

    def go_to_jobs(self) -> str:
        self.driver.find_element(By.LINK_TEXT, self.jobs_by_txt).click()
        return self.get_title()

    # -------------------- Methods For Maslulim ----------------------------

    def list_of_maslulim_categories(self):
        return self.driver.find_elements(By.XPATH, self.maslulim_categories_by_xpath)

    def click_on_maslul_real_time(self):
        self.driver.find_element(By.XPATH, self.maslul_real_time_by_xpath).click()

    def list_of_courses_on_real_time(self):
        return self.driver.find_elements(By.XPATH, self.course_real_time_by_xpath)

    def click_on_maslul_full_stack(self):
        self.driver.find_element(By.XPATH, self.maslul_full_stack_by_xpath).click()

    def list_of_courses_on_full_stack(self):
        return self.driver.find_elements(By.XPATH, self.full_stack_courses_by_xpath)

    def click_on_maslul_cyber(self):
        self.driver.find_element(By.XPATH, self.maslul_cyber_by_xpath).click()

    def list_of_courses_on_cyber(self):
        return self.driver.find_elements(By.XPATH, self.cyber_courses_by_xpath)

    def click_on_maslul_machine_learning(self):
        self.driver.find_element(By.XPATH, self.maslul_machine_learning_by_xpath).click()

    def list_of_courses_on_machine_learning(self):
        return self.driver.find_elements(By.XPATH, self.machine_learning_courses_by_xpath)

    def click_on_maslul_qa(self):
        self.driver.find_element(By.XPATH, self.maslul_qa_by_xpath).click()

    def list_of_courses_on_qa(self):
        return self.driver.find_elements(By.XPATH, self.qa_courses_by_xpath)

    def click_on_maslul_dev_ops(self):
        self.driver.find_element(By.XPATH, self.maslul_dev_ops_by_xpath).click()

    def list_of_courses_on_dev_ops(self):
        return self.driver.find_elements(By.XPATH, self.dev_ops_courses_by_xpath)

    def click_on_maslul_linux_servers(self):
        self.driver.find_element(By.XPATH, self.maslul_linux_servers_by_xpath).click()

    def list_of_courses_on_linux_servers(self):
        return self.driver.find_elements(By.XPATH, self.linux_servers_courses_by_xpath)

    # ------------------------------- COURSES --------------------------------------

    def click_on_courses_tab(self):
        self.driver.find_element(By.XPATH, self.courses_tab_by_xpath).click()

    def click_on_course_real_time(self):
        self.driver.find_element(By.XPATH, self.course_real_time_by_xpath).click()

    def list_of_sub_courses_on_real_time_course(self):
        return self.driver.find_elements(By.XPATH, self.real_time_sub_courses_by_xpath)

    # def get_category_maslulim_list(self) -> list:
    #     return self.driver.find_elements(By.CLASS_NAME, self.maslulim_by_categories_by_class)

    class Validation:
        pass