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
from datetime import datetime

# -------------------------------------
correctUserName = 'dagula74@yahoo.com'
correctPassword = '310870969'


#


class HeaderTest(unittest.TestCase):
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
        cls.date_for_log = now.strftime("%d %m %Y")
        cls.string_result = "-----------------------------------TESTING HEADER-----------------------------------------------\n"
        # print('-----  BEFORE SLEEP  -----')
        # time.sleep(12)
        # print('-----  AFTER SLEEP  -----')
        # cls.driver.find_element(By.XPATH, '//*[@id="lead-form-modal1"]/span').click()
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
        self.string_message(f"---Checking The {button_name} Page...---\n")
        if title == actual_title_of_page:
            self.string_message("---The page is correct---\n")
            return True
        else:
            self.string_message("---Not the right page---\n")
            return False

    def string_message(self, message):
        print(message)
        self.string_result += message

    def open_file_and_append_string_message(self):
        try:
            file = open(f"../../Source/log {self.date_for_log}.txt", "a+")
            file.write(self.string_result)
            file.close()
        except FileNotFoundError:
            print("Did not found a file")

    # -------------------------------------------MASLULIM-------------------------------------------

    def maslul_real_time(self):
        self.string_message("---Inside maslul_real_time function---\n")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {"Bootcamp Real Time": "קורס Real-Time Bootcamp | הכשרה מקוצרת לפיתוח מערכות משובצות מחשב",
                          "Embedded Systems": "קורס Embedded Systems | מסלול הכשרה והשמה בפיתוח bare board",
                          "Real Time Embedded Linux": "קורס Real Time Embedded Linux » Real Time College",
                          "Embedded Linux": "מסלול Embedded Linux | פיתוח מערכות משובצות » Real Time Group"}
        while running:
            for length in range(len(header.list_of_courses_on_real_time())):
                header.maslul().click()
                header.maslul_real_time().click()
                header.list_of_courses_on_real_time()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
                # time.sleep(3)
            running = False

        self.string_message("---Outside maslul_real_time function---\n")

    def maslul_full_stack(self):
        self.string_message("---Inside maslul_full_stack function---\n")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {"Full Stack": "קורס Full Stack | לימודי Full Stack | קורס Web Development"}

        while running:
            for length in range(len(header.list_of_courses_on_full_stack())):
                header.maslul().click()
                header.maslul_full_stack().click()
                header.list_of_courses_on_full_stack()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        self.string_message("---Outside maslul_full_stack function---\n")

    def maslul_cyber(self):
        self.string_message("---Inside maslul_cyber function---\n")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {
            " סייבר ואבטחת מידע | cyber security": "קורס Cyber אבטחת מידע וסייבר | Cyber Security » Real Time Group"}

        while running:
            for length in range(len(header.list_of_courses_on_cyber())):
                header.maslul().click()
                header.maslul_cyber().click()
                header.list_of_courses_on_cyber()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        self.string_message("---Outside maslul_cyber function---\n")

    def maslul_machine_learning(self):
        self.string_message("---Inside maslul_machine_learning function---\n")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {
            "Data Analyst": "Data Analyst » Real Time College",
            "Machine Learning & Data Science": "קורס machine learning | הכשרה והשמה :Real Time Group",
            "Image Processing": "קורס עיבוד תמונה Image Processing | השתלבות בחזית העשייה החדשנית"}

        while running:
            for length in range(len(header.list_of_courses_on_machine_learning())):
                header.maslul().click()
                header.maslul_machine_learning().click()
                header.list_of_courses_on_machine_learning()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        self.string_message("---Outside maslul_machine_learning function---\n")

    def maslul_qa(self):
        self.string_message("---Inside maslul_qa function---\n")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {
            "אוטומציה": "קורס אוטומציה QA | לימודי המשך לקורס QA ואוטומציה » Real Time College",
            " QA |  בדיקות תוכנה": "קורס QA | קורס בודק תוכנה - כולל סטאז' מעשי » Real Time College"}

        while running:
            for length in range(len(header.list_of_courses_on_qa())):
                header.maslul().click()
                header.maslul_qa().click()
                header.list_of_courses_on_qa()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        self.string_message("---Outside maslul_qa function---\n")

    def maslul_dev_ops(self):
        self.string_message("---Inside maslul_dev_ops function---\n")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {
            "DevOps": "קורס DevOps | קורס דאבאופס ניהול פרויקטים בפיתוח » Real Time Group"}

        while running:
            for length in range(len(header.list_of_courses_on_dev_ops())):
                header.maslul().click()
                header.maslul_dev_ops().click()
                header.list_of_courses_on_dev_ops()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        self.string_message("---Outside maslul_dev_ops function---\n")

    def maslul_linux_servers(self):
        self.string_message("---Inside maslul_linux_servers function---\n")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {
            " לינוקס - ניהול שרתי Linux": "קורס לינוקס | לימודי ניהול שרתים בענן (Linux) | קורס לימודי IT / AWS >>>"}

        while running:
            for length in range(len(header.list_of_courses_on_linux_servers())):
                header.maslul().click()
                header.maslul_linux_servers().click()
                header.list_of_courses_on_linux_servers()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        self.string_message("---Outside maslul_linux_servers function---\n")

    # -------------------------------------------COURSES-------------------------------------------

    def course_real_time(self):
        self.string_message("---Inside course_real_time function---\n")
        header = Header(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            " RT Concepts": "קורס RT Concepts | מבוא למערכות משובצות מחשב » Real Time Group",
            " שפת C": "קורס שפת C | לימודים שפת | C למתחילים :Real Time Group",
            " Linux Kernel And Device Drivers": "קורס Linux Kernel and Device Drivers | מערכות משובצות מחשב בסביבת לינוקס",
            " ARM - Embedded Systems": "קורס Arm - Embedded Systems | פיתוח תוכנה - Real Time College",
            " Internet Of Things": "קורס Internet Of Things | מה זה IOT ואיך זה יכול לשנות על חיינו?",
            " FreeRTOS": "קורס Free Rtos - ללמוד איזה תכנית תזכה במעבד בכל נקודת זמן",
            " שפת ++C": "קורס שפת C למתחילים / שפת C ++ למתקדמים | ללמוד » Real Time College",
            "Yocto Programming": "YOCTO programming | מערכות Embedded Linux » Real Time College",
            " Embedded Linux": "קורס Embedded Linux | פיתוח מערכות משובצות מחשב » Real Time Group"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for key in keys_of_dict_of_titles:
                header.courses_tab().click()
                header.course_real_time().click()
                if index == 0:
                    header.sub_course_rt_concepts().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_c_language().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_linux_kernel_and_device_drivers().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 3:
                    header.sub_course_arm_embedded_systems().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 4:
                    header.sub_course_internet_of_things().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 5:
                    header.sub_course_free_rtos().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 6:
                    header.sub_course_c_plus_plus_language().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 7:
                    header.sub_course_yocto_programming().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 8:
                    header.sub_course_linux_embedded().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False

        self.string_message("---Outside course_real_time function---\n")

    def course_web_development(self):
        self.string_message("---Inside course_web_development function---\n")
        header = Header(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            " Web Foundations": "קורס Web Foundations להכיר את היסודות של בניית אתרים» Real Time College",
            " AngularJS | אנגולר": "קורס AngularJS / לימודי אנגולר למתחילים » Real Time College",
            " פייתון |  Python": "קורס פייתון - Python | לימוד שפת פייתון מומלץ למתחילים / מתקדם",
            " CSS3": "קורס CSS3 | ללמוד הצגה ועיצוב של דפי אינטרנט :Real Time Group",
            " NodeJS": "קורס NodeJS | הקורס המקיף והמעשי ביותר בארץ :Real Time Group",
            " Javascript": "קורס JavaScript & jQuery של Real Time College מקבוצה של RTG",
            " TypeScript": "קורס TypeScript | התמחות בכלים של Google » Real Time Group",
            " MongoDB": "קורס MongoDB | ללמוד BigData - MongoDB בקלות! | Real Time Group",
            " HTML5": "קורס HTML | למד HTML5 עם המומחים של Real Time College",
            " React |  ריאקט": "קורס React | לימודי תכנות ופיתוח אפליקציות React native JS",
            " Java": "קורס Java | למידת שפת Java למתחילים / מתקדמים » Real Time Group",
            " Bootstrap": "קורס Bootstrap | בניית אתרי אינטרנט בעזרת בוטסטראפ",
            " פיתוח אפליקציות לאנדרואיד": "קורס פיתוח אפליקציות לאנדרואיד | פיתוח אפליקציות תוך שימוש בשפת התכנות Java",
            " GIT (Version Control)": "קורס Version Control עם המומחים » Real Time Group",
            " SQL": "קורס SQL למתחילים | ניהול בסיסי נתונים :Real Time Group",
        }
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for key in keys_of_dict_of_titles:
                header.courses_tab().click()
                header.course_web_development().click()
                if index == 0:
                    header.sub_course_web_foundations().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 1:
                    header.sub_course_angular_js().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 2:
                    header.sub_course_python_language().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 3:
                    header.sub_course_css_language().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 4:
                    header.sub_course_node_js().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 5:
                    header.sub_course_javascript_language().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 6:
                    header.sub_course_typescript_language().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 7:
                    header.sub_course_mongodb().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 8:
                    header.sub_course_html5().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 9:
                    header.sub_course_react().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 10:
                    header.sub_course_java_language().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 11:
                    header.sub_course_bootstrap().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 12:
                    header.sub_course_app_development_for_android().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 13:
                    header.sub_course_git().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 14:
                    header.sub_course_sql().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("---Outside course_web_development function---\n")

    def course_cyber_security(self):
        self.string_message("---Inside course_cyber_security function---\n")
        header = Header(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            "הכנה לבחינת הסמכה C | EH": "הכנה לבחינת הסמכה CEH » Real Time College",
            " Cyber Attack Infrastructure": "קורס Cyber Attack Infrastructure - לזהות נקודות תורפה | Real Time College",
            " Malware Analysis": "קורס Malware Analysis לפרק ולהבין איומים פוטנציאלים » Real Time College",
            " Penetration Testing": "קורס Penetration Testing - מבחני חדירות » Real Time College",
            " Linux Fundamentals": "קורס Linux Fundamentals -כל הידע והפרקטיקה הנדרשים » Real Time College",
            " Cyber Security Fundamentals": "קורס Cyber Security Fundamentals | סייבר ואבטחת מידע :Real Time Group",
            " Networking": "קורס Networking | לימודי מעשי בתקשורת הנתונים » Real Time College",
            " Forensics Investigation & Incident Response": "קורס Forensics Investigation & Incident Response » Real Time College"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for key in keys_of_dict_of_titles:
                header.courses_tab().click()
                header.course_cyber_security().click()
                if index == 0:
                    header.sub_course_preparations_for_certification_exam().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_cyber_attack_infrastructure().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_malware_analysis().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 3:
                    header.sub_course_penetration_testing().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 4:
                    header.sub_course_linux_fundamentals().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 5:
                    header.sub_course_cyber_security_fundamentals().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 6:
                    header.sub_course_networking().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 7:
                    header.sub_course_forensics_investigation_and_incident_response().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("---Outside course_cyber_security function---\n")

    def course_devops(self):
        self.string_message("---Inside course_devops function---\n")
        header = Header(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            " Docker": "קורס Docker - פלטפורמת תוכנה מובילה לניהול יישומים והרצת קוד בקונטיינרים",
            " לינוקס | Linux Admin": "קורס לינוקס Linux Admin | ניהול מערכות הפעלה - Real Time College",
            " Kubernetes": "קורס Kubernetes | לימוד קוברנטיס מעשי » Real Time College",
            " פייתון |  Python": "קורס פייתון - Python | לימוד שפת פייתון מומלץ למתחילים / מתקדם",
            " Zabbix": "קורס Zabbix | מעקב אחר פעילות שירותי ענן » Real Time Group",
            " Terraform": "קורס Terraform - ניהול תשתיות בענן » Real Time College",
            " Networking": "קורס Networking | לימודי מעשי בתקשורת הנתונים » Real Time College",
            " ANSIBLE": "קורס ANSIBLE - כלי לניהול ופיתוח כלי אוטומציה » Real Time College",
            " Bash Scripting": "קורס Bash Scripting | תיכנות בסביבת לינוקס » Real Time Group",
            " AWS": "קורס AWS | התמחות בכלי שירותי הענן של אמזון :Real Time Group",
            " Jenkins": "קורס Jenkins - למד לעבוד עם ג'נקינס בצורה הטובה ביותר! | Real Time Group"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for key in keys_of_dict_of_titles:
                header.courses_tab().click()
                header.course_devops().click()
                if index == 0:
                    header.sub_course_docker().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_linux_admin().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_kubernetes().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 3:
                    header.sub_course_python_language().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 4:
                    header.sub_course_zabbix().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 5:
                    header.sub_course_terraform().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 6:
                    header.sub_course_networking().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 7:
                    header.sub_course_ansible().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 8:
                    header.sub_course_bash_scripting().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 9:
                    header.sub_course_aws().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 10:
                    header.sub_course_jenkins().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("---Outside course_devops function---\n")

    def course_data_science(self):
        self.string_message("---Inside course_data_science function---\n")
        header = Header(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            " Machine Learning Fundamentals": "קורס Machine Learning Fundamentals » Real Time College",
            " Machine Learning With Python": "קורס Machine Learning with Python » Real Time College",
            " Deep Learning With Tensorflow": "קורס פיתוח Deep Learning with Tensorflow » Real Time College"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for key in keys_of_dict_of_titles:
                header.courses_tab().click()
                header.course_data_science().click()
                if index == 0:
                    header.sub_course_machine_learning_fundamentals().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_machine_learning_with_python().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_deep_learning_with_tensorflow().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("---Outside course_data_science function---\n")

    def course_software_testing(self):
        self.string_message("---Inside course_software_testing function---\n")
        header = Header(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            " Selenium": "קורס Selenium - לימודי פיתוח אוטומציה | הקורס הכי מקיף ומעשי בארץ",
            " LabView": "קורס LabView - לימוד מעשי וממוקד לפיתוח בפלטפורמת LabView",
            " JIRA | ג'ירה": "קורס JIRA | בואו להתמקצע ולצבור ניסיון בכלי המוביל למעקב באגים",
            " מתודולוגיות QA": "קורס מתודולוגיות QA עם המומחים של Real Time College",
            " Java": "קורס Java | למידת שפת Java למתחילים / מתקדמים » Real Time Group"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for key in keys_of_dict_of_titles:
                header.courses_tab().click()
                header.course_software_testing().click()
                if index == 0:
                    header.sub_course_selenium().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_labview().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_jira().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 3:
                    header.sub_course_qa_methodologies().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 4:
                    header.sub_course_java_language().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("---Outside course_software_testing function---\n")

    def course_network_and_sysadmin(self):
        self.string_message("---Inside course_network_and_sysadmin function---\n")
        header = Header(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            " לינוקס | Linux Admin": "קורס לינוקס Linux Admin | ניהול מערכות הפעלה - Real Time College",
            " LPIC-2": "קורס LPIC-2 » Real Time College",
            " Linux Fundamentals": "קורס Linux Fundamentals -כל הידע והפרקטיקה הנדרשים » Real Time College",
            " LPIC-1": "קורס LPIC-1 - הכנה למבחן הסמכה בינלאומית של לינוקס » Real Time College",
            " Networking": "קורס Networking | לימודי מעשי בתקשורת הנתונים » Real Time College"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for key in keys_of_dict_of_titles:
                header.courses_tab().click()
                header.course_network_and_sysadmin().click()
                if index == 0:
                    header.sub_course_linux_admin().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_lpic_2().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_linux_fundamentals().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 3:
                    header.sub_course_lpic_1().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 4:
                    header.sub_course_networking().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("---Outside course_network_and_sysadmin function---\n")

    def course_programming_language(self):
        self.string_message("---Inside course_programming_language function---\n")
        header = Header(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            " Java": "קורס Java | למידת שפת Java למתחילים / מתקדמים » Real Time Group",
            " שפת C": "קורס שפת C | לימודים שפת | C למתחילים :Real Time Group",
            " Javascript": "קורס JavaScript & jQuery של Real Time College מקבוצה של RTG",
            " פייתון |  Python": "קורס פייתון - Python | לימוד שפת פייתון מומלץ למתחילים / מתקדם",
            " שפת ++C": "קורס שפת C למתחילים / שפת C ++ למתקדמים | ללמוד » Real Time College"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for key in keys_of_dict_of_titles:
                header.courses_tab().click()
                header.course_programming_language().click()
                if index == 0:
                    header.sub_course_java_language().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_c_language().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_javascript_language().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 3:
                    header.sub_course_python_language().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 4:
                    header.sub_course_c_plus_plus_language().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("---Outside course_programming_language function---\n")

    def course_cloud_computing(self):
        self.string_message("---Inside course_cloud_computing function---\n")
        header = Header(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            " AWS": "קורס AWS | התמחות בכלי שירותי הענן של אמזון :Real Time Group",
            " Microsoft Azure": "קורס Microsoft Azure | סט כלים בסביבת אונליין » Real Time College"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for key in keys_of_dict_of_titles:
                header.courses_tab().click()
                header.course_cloud_computing().click()
                if index == 0:
                    header.sub_course_aws().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_microsoft_azure().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("---Outside course_cloud_computing function---\n")

    def course_image_processing(self):
        self.string_message("---Inside course_image_processing function---\n")
        header = Header(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            " Machine Learning Fundamentals": "קורס Machine Learning Fundamentals » Real Time College",
            " OpenCV": "קורס OpenCV | לפתח קריירה בחזית התעשייה בתחום של Image Processing",
            " CUDA": "קורס CUDA | לנצל את הכוח GPU של המחשב » Real Time College",
            " Machine Learning With Python": "קורס Machine Learning with Python » Real Time College",
            " Deep Learning With Tensorflow": "קורס פיתוח Deep Learning with Tensorflow » Real Time College",
            " Nvidia GPUs": "קורס Nvidia GPUs | שימוש לטובת פיתוח עיבוד תמונה לצורך פרוייקטים"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for key in keys_of_dict_of_titles:
                header.courses_tab().click()
                header.course_image_processing().click()
                if index == 0:
                    header.sub_course_machine_learning_fundamentals().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_open_cv().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_cuda().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 3:
                    header.sub_course_machine_learning_with_python().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 4:
                    header.sub_course_deep_learning_with_tensorflow().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 5:
                    header.sub_course_nvidia_gpus().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("---Outside course_image_processing function---\n")

    def course_database_management(self):
        self.string_message("---Inside course_database_management function---\n")
        header = Header(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            " SQL": "קורס SQL למתחילים | ניהול בסיסי נתונים :Real Time Group",
            " MongoDB": "קורס MongoDB | ללמוד BigData - MongoDB בקלות! | Real Time Group"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for key in keys_of_dict_of_titles:
                header.courses_tab().click()
                header.course_database_management().click()
                if index == 0:
                    header.sub_course_sql().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_mongodb().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("---Outside course_database_management function---\n")

    # -------------------------------------------5 BUTTONS-------------------------------------------

    def go_to_page_courses_for_companies(self):
        self.string_message("---Inside go_to_page_courses_for_companies function---\n")
        header = Header(self.driver)
        header.courses_for_companies().click()
        title = header.get_title()
        actual_page_title = "Real Time College » Real Time Group's Training Center"
        button_name = 'Courses For Companies'
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("---Outside go_to_page_courses_for_companies function---\n")

    def go_to_page_articles(self):
        self.string_message("---Inside go_to_page_articles function---\n")
        header = Header(self.driver)
        header.articles().click()
        title = header.get_title()
        actual_page_title = "Realtime Group - מאמרים"
        button_name = 'Articles'
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("---Outside go_to_page_articles function---\n")

    def go_to_page_about_us(self):
        self.string_message("---Inside go_to_page_about_us function---\n")
        header = Header(self.driver)
        header.about_us().click()
        title = header.get_title()
        actual_page_title = "אודות Real Time Group - חטיבת הדרכה | חטיבת השמה | מיקור חוץ"
        button_name = "About Us"
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("---Outside go_to_page_about_us function---\n")

    def go_to_page_declaration_of_accessibility(self):
        self.string_message("---Inside go_to_page_declaration_of_accessibility function---\n")
        header = Header(self.driver)
        header.declaration_of_accessibility().click()
        title = header.get_title()
        actual_page_title = "הצהרת נגישות » Real Time College"
        button_name = "Declaration Of Accessibility"
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("---Outside go_to_page_declaration_of_accessibility function---\n")

    def go_to_page_jobs(self):
        self.string_message("---Inside go_to_page_jobs function---\n")
        header = Header(self.driver)
        header.jobs().click()
        title = header.get_title()
        actual_page_title = "Real Time College » Real Time Group's Training Center"
        button_name = "Jobs"
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("---Outside go_to_page_jobs function---\n")

    # -------------------------------------------TEST-------------------------------------------

    def run_maslulim(self):
        self.maslul_real_time()
        self.maslul_full_stack()
        self.maslul_cyber()
        self.maslul_machine_learning()
        self.maslul_qa()
        self.maslul_dev_ops()
        self.maslul_linux_servers()

    def run_courses(self):
        self.course_real_time()
        self.course_web_development()
        self.course_cyber_security()
        self.course_devops()
        self.course_data_science()
        self.course_software_testing()
        self.course_network_and_sysadmin()
        self.course_programming_language()
        self.course_cloud_computing()
        self.course_image_processing()
        self.course_database_management()

    def run_five_buttons(self):
        self.go_to_page_courses_for_companies()
        self.go_to_page_articles()
        self.go_to_page_about_us()
        self.go_to_page_declaration_of_accessibility()
        self.go_to_page_jobs()

    def test_header(self):
        self.run_maslulim()
        self.run_courses()
        self.run_five_buttons()

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
