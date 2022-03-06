#        28_2_2022
#      created by Dima
#   Header test
# --------------------------------------------------------------------------------------
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from POM.Pages.header import Header
from POM.Pages.studentPortalLoginPage import StudentPortal

# -------------------------------------
correctUserName = 'dagula74@yahoo.com'
correctPassword = '310870969'


#


class HeaderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:

        cls.driver: WebDriver = webdriver.Chrome(executable_path=
                                                 'C:\\Users\\Public\\Documents\\GitHub Projects\\Python\\siteQA\\drivers\\chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(20)
        cls.driver.set_page_load_timeout(30)
        cls.driver.get('https://rt-ed.co.il/')
        print('-----  BEFORE SLEEP  -----')
        time.sleep(12)
        print('-----  AFTER SLEEP  -----')
        cls.driver.find_element(By.XPATH, '//*[@id="lead-form-modal1"]/span').click()
        print('-----  END OF CLS  -----')

    # def test_legalEnter_studentPortal_fromHeader(self):
    #     print('-----  START test_studentPortal_fromHeader  -----')
    #     header = Header(self.driver)
    #     print('-----  after init Header test_studentPortal_fromHeader  -----')
    #     header.goToStudentPortal()
    #
    #     stPortal = StudentPortal(self.driver)
    #     stPortal.enterUserName(correctUserName)
    #     stPortal.enterPassword(correctPassword)
    #     stPortal.logIn()

    def compare_title_pages(self, title: str, actual_page_title: str, button_name: str):
        actual_title_of_page = actual_page_title
        print(f"---Checking The {button_name} Page...---")
        if title == actual_title_of_page:
            print("---The page is correct---")
        else:
            print("---Not the right page---")

    def maslul_real_time(self):
        print("---Inside maslul_real_time function---")
        header = Header(self.driver)
        index = 0
        running = True
        #list_of_titles = ["Bootcamp Real Time", "Embedded Systems", "Real Time Embedded Linux", "Embedded Linux"]
        dict_of_titles = {"Bootcamp Real Time": "קורס Real-Time Bootcamp | הכשרה מקוצרת לפיתוח מערכות משובצות מחשב", "Embedded Systems": "קורס Embedded Systems | מסלול הכשרה והשמה בפיתוח bare board", "Real Time Embedded Linux": "קורס Real Time Embedded Linux » Real Time College", "Embedded Linux": "מסלול Embedded Linux | פיתוח מערכות משובצות » Real Time Group"}
        while running:
            for length in range(len(header.list_of_courses_on_real_time())):
                header.goToMaslul()
                header.click_on_maslul_real_time()
                header.list_of_courses_on_real_time()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
                # time.sleep(3)
            running = False

        print("---Outside maslul_real_time function---")

    def maslul_full_stack(self):
        print("---Inside maslul_full_stack function---")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {"Full Stack": "קורס Full Stack | לימודי Full Stack | קורס Web Development"}

        while running:
            for length in range(len(header.list_of_courses_on_full_stack())):
                header.goToMaslul()
                header.click_on_maslul_full_stack()
                header.list_of_courses_on_full_stack()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        print("---Outside maslul_full_stack function---")

    def maslul_cyber(self):
        print("---Inside maslul_cyber function---")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {" סייבר ואבטחת מידע | cyber security": "קורס Cyber אבטחת מידע וסייבר | Cyber Security » Real Time Group"}

        while running:
            for length in range(len(header.list_of_courses_on_cyber())):
                header.goToMaslul()
                header.click_on_maslul_cyber()
                header.list_of_courses_on_cyber()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        print("---Outside maslul_cyber function---")

    def maslul_machine_learning(self):
        print("---Inside maslul_machine_learning function---")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {
            "Data Analyst": "Data Analyst » Real Time College", "Machine Learning & Data Science": "קורס machine learning | הכשרה והשמה :Real Time Group", "Image Processing": "קורס עיבוד תמונה Image Processing | השתלבות בחזית העשייה החדשנית"}

        while running:
            for length in range(len(header.list_of_courses_on_machine_learning())):
                header.goToMaslul()
                header.click_on_maslul_machine_learning()
                header.list_of_courses_on_machine_learning()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        print("---Outside maslul_machine_learning function---")

    def maslul_qa(self):
        print("---Inside maslul_qa function---")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {
            "אוטומציה": "קורס אוטומציה QA | לימודי המשך לקורס QA ואוטומציה » Real Time College",
            " QA |  בדיקות תוכנה": "קורס QA | קורס בודק תוכנה - כולל סטאז' מעשי » Real Time College"}

        while running:
            for length in range(len(header.list_of_courses_on_qa())):
                header.goToMaslul()
                header.click_on_maslul_qa()
                header.list_of_courses_on_qa()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        print("---Outside maslul_qa function---")

    def maslul_dev_ops(self):
        print("---Inside maslul_dev_ops function---")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {
            "DevOps": "קורס DevOps | קורס דאבאופס ניהול פרויקטים בפיתוח » Real Time Group"}

        while running:
            for length in range(len(header.list_of_courses_on_dev_ops())):
                header.goToMaslul()
                header.click_on_maslul_dev_ops()
                header.list_of_courses_on_dev_ops()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        print("---Outside maslul_dev_ops function---")

    def maslul_linux_servers(self):
        print("---Inside maslul_linux_servers function---")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {
            " לינוקס - ניהול שרתי Linux": "קורס לינוקס | לימודי ניהול שרתים בענן (Linux) | קורס לימודי IT / AWS >>>"}

        while running:
            for length in range(len(header.list_of_courses_on_linux_servers())):
                header.goToMaslul()
                header.click_on_maslul_linux_servers()
                header.list_of_courses_on_linux_servers()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        print("---Outside maslul_linux_servers function---")

    def course_real_time(self):
        print("---Inside course_real_time function---")
        header = Header(self.driver)
        index = 0
        running = True
        list_pressed_buttons = []
        dict_of_titles = {
            " FreeRTOS": "קורס Free Rtos - ללמוד איזה תכנית תזכה במעבד בכל נקודת זמן",
            " שפת ++C": "קורס שפת C למתחילים / שפת C ++ למתקדמים | ללמוד » Real Time College",
            "Yocto Programming": "YOCTO programming | מערכות Embedded Linux » Real Time College",
            " Embedded Linux": "קורס Embedded Linux | פיתוח מערכות משובצות מחשב » Real Time Group",
            " RT Concepts": "קורס RT Concepts | מבוא למערכות משובצות מחשב » Real Time Group",
            " שפת C": "קורס שפת C | לימודים שפת | C למתחילים :Real Time Group",
            " Linux Kernel And Device Drivers": "קורס Linux Kernel and Device Drivers | מערכות משובצות מחשב בסביבת לינוקס",
            " ARM - Embedded Systems": "קורס Arm - Embedded Systems | פיתוח תוכנה - Real Time College",
            " Internet Of Things": "קורס Internet Of Things | מה זה IOT ואיך זה יכול לשנות על חיינו?"}

        while running:
            for length in range(len(header.list_of_sub_courses_on_real_time_course())):
                header.click_on_courses_tab()
                header.click_on_course_real_time()
                header.list_of_sub_courses_on_real_time_course()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        print("---Outside course_real_time function---")

    #def test_run_maslulim(self):
        #self.maslul_real_time()
        #self.maslul_full_stack()
        #self.maslul_cyber()
        #self.maslul_machine_learning()
        #self.maslul_qa()
        #self.maslul_dev_ops()
        #self.maslul_linux_servers()

    def test_run_courses(self):
        self.course_real_time()

    # def go_to_page_courses_for_companies(self):
    #     print("---Inside go_to_page_courses_for_companies function---")
    #     header = Header(self.driver)
    #     title = header.go_to_courses_for_companies()
    #     actual_page_title = "Real Time College » Real Time Group's Training Center"
    #     button_name = 'Courses For Companies'
    #     self.compare_title_pages(title, actual_page_title, button_name)
    #     print("---Outside go_to_page_courses_for_companies function---")
    #
    # def go_to_page_articles(self):
    #     print("---Inside go_to_page_articles function---")
    #     header = Header(self.driver)
    #     title = header.go_to_articles()
    #     actual_page_title = "Realtime Group - מאמרים"
    #     button_name = 'Articles'
    #     self.compare_title_pages(title, actual_page_title, button_name)
    #     print("---Outside go_to_page_articles function---")
    #
    # def go_to_page_about_us(self):
    #     print("---Inside go_to_page_about_us function---")
    #     header = Header(self.driver)
    #     title = header.go_to_about_us()
    #     actual_page_title= "אודות Real Time Group - חטיבת הדרכה | חטיבת השמה | מיקור חוץ"
    #     button_name = "About Us"
    #     self.compare_title_pages(title, actual_page_title, button_name)
    #     print("---Outside go_to_page_about_us function---")
    #
    # def go_to_page_declaration_of_accessibility(self):
    #     print("---Inside go_to_page_declaration_of_accessibility function---")
    #     header = Header(self.driver)
    #     title = header.go_to_declaration_of_accessibility()
    #     actual_page_title = "הצהרת נגישות » Real Time College"
    #     button_name = "Declaration Of Accessibility"
    #     self.compare_title_pages(title, actual_page_title, button_name)
    #     print("---Outside go_to_page_declaration_of_accessibility function---")
    #
    # def go_to_page_jobs(self):
    #     print("---Inside go_to_page_jobs function---")
    #     header = Header(self.driver)
    #     title = header.go_to_jobs()
    #     actual_page_title = "Real Time College » Real Time Group's Training Center"
    #     button_name = "Jobs"
    #     self.compare_title_pages(title, actual_page_title, button_name)
    #     print("---Outside go_to_page_jobs function---")
    #
    # def test_run_five_buttons(self):
    #     self.go_to_page_courses_for_companies()
    #     self.go_to_page_articles()
    #     self.go_to_page_about_us()
    #     self.go_to_page_declaration_of_accessibility()
    #     self.go_to_page_jobs()

    # def test_get_maslul_and_check_title(self):
    #     print("-----Start get_maslul_and_check_title-----")
    #     header = Header(self.driver)
    #     for category in header.goToMaslul():
    #         for maslul in
    #     print("----- End get_maslul_and_check_title-----")


#    def closeEnteryPopUp(self, driver, popUp_close_xpath):
#        driver.find_element(By.XPATH, popUp_close_xpath).click()


if __name__ == '__main__':
    unittest.main()
