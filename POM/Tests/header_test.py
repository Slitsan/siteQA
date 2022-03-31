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
studentPortalTitle = 'Students Portal RT-ED'
popUp_close_XPATH = '//*[@id="lead-form-modal1"]/span'
#


class HeaderTest(unittest.TestCase):
    def __init__(self, init_driver):
        super().__init__()
        self.driver = init_driver
        now = datetime.now()
        self.date_for_log = now.strftime("%d %m %Y")
        self.string_result = "*-----------------------------------TESTING HEADER-----------------------------------------------\n"

    def compare_title_pages(self, title: str, actual_page_title: str, button_name: str):
        actual_title_of_page = actual_page_title
        self.string_message(f"---Checking The {button_name} Page...---\n")
        if title == actual_title_of_page:
            self.string_message("---The page is correct---\n")
            return True
        else:
            self.string_message("!------Not the right page------!\n")
            return False

    def string_message(self, message):
        print(message)
        self.string_result += message

    def open_file_and_append_string_message(self):
        try:
            file = open(f"./Source/log {self.date_for_log}.txt", "a+")
            file.write(self.string_result)
            file.close()
        except FileNotFoundError:
            print("Did not found a file")

    # -------------------------------------------MASLULIM-------------------------------------------

    def maslul_real_time(self):
        self.string_message("@Inside Maslul Real-Time function---\n")
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
                self.string_message(f"@@Inside course {header.list_of_courses_on_real_time()[index].text}\n")
                header.list_of_courses_on_real_time()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
                # time.sleep(3)
            running = False

        self.string_message("@Outside Maslul Real-Time function---\n")

    def maslul_full_stack(self):
        self.string_message("@Inside Maslul Full-Stack function---\n")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {"Full Stack": "קורס Full Stack | לימודי Full Stack | קורס Web Development"}

        while running:
            for length in range(len(header.list_of_courses_on_full_stack())):
                header.maslul().click()
                header.maslul_full_stack().click()
                self.string_message(f"@@Inside course {header.list_of_courses_on_full_stack()[index].text}\n")
                header.list_of_courses_on_full_stack()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        self.string_message("@Outside Maslul Full-Stack function---\n")

    def maslul_cyber(self):
        self.string_message("@Inside Maslul Cyber function---\n")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {
            " סייבר ואבטחת מידע | cyber security": "קורס Cyber אבטחת מידע וסייבר | Cyber Security » Real Time Group"}

        while running:
            for length in range(len(header.list_of_courses_on_cyber())):
                header.maslul().click()
                header.maslul_cyber().click()
                self.string_message(f"@@Inside course {header.list_of_courses_on_cyber()[index].text}\n")
                header.list_of_courses_on_cyber()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        self.string_message("@Outside Maslul Cyber function---\n")

    def maslul_machine_learning(self):
        self.string_message("@Inside Maslul Machine Learning function---\n")
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
                self.string_message(f"@@Inside course {header.list_of_courses_on_machine_learning()[index].text}\n")
                header.list_of_courses_on_machine_learning()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        self.string_message("@Outside Maslul Machine Learning function---\n")

    def maslul_qa(self):
        self.string_message("@Inside Maslul QA function---\n")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {
            "אוטומציה": "קורס אוטומציה QA | לימודי המשך לקורס QA ואוטומציה » Real Time College",
            " QA |  בדיקות תוכנה": "קורס QA | קורס בודק תוכנה QA - כולל סטאז' מעשי » Real Time College"}

        while running:
            for length in range(len(header.list_of_courses_on_qa())):
                header.maslul().click()
                header.maslul_qa().click()
                self.string_message(f"@@Inside course {header.list_of_courses_on_qa()[index].text}\n")
                header.list_of_courses_on_qa()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        self.string_message("@Outside Maslul QA function---\n")

    def maslul_dev_ops(self):
        self.string_message("@Inside Maslul DevOps function---\n")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {
            "DevOps": "קורס DevOps | קורס דאבאופס ניהול פרויקטים בפיתוח » Real Time Group"}

        while running:
            for length in range(len(header.list_of_courses_on_dev_ops())):
                header.maslul().click()
                header.maslul_dev_ops().click()
                self.string_message(f"@@Inside course {header.list_of_courses_on_dev_ops()[index].text}\n")
                header.list_of_courses_on_dev_ops()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        self.string_message("@Outside Maslul DevOps function---\n")

    def maslul_linux_servers(self):
        self.string_message("@Inside Maslul Linux Servers function---\n")
        header = Header(self.driver)
        index = 0
        running = True
        dict_of_titles = {
            " לינוקס - ניהול שרתי Linux": "קורס לינוקס | לימודי ניהול שרתים בענן (Linux) | קורס לימודי IT / AWS >>>"}

        while running:
            for length in range(len(header.list_of_courses_on_linux_servers())):
                header.maslul().click()
                header.maslul_linux_servers().click()
                self.string_message(f"@@Inside course {header.list_of_courses_on_linux_servers()[index].text}\n")
                header.list_of_courses_on_linux_servers()[index].click()
                title = header.get_title()
                expected_title = list(dict_of_titles.values())[index]
                self.compare_title_pages(title, expected_title, title)
                index += 1
            running = False

        self.string_message("@Outside Maslul Linux Servers function---\n")

    # -------------------------------------------COURSES-------------------------------------------

    def course_real_time(self):
        self.string_message("@Inside Course 'Real-Time' function---\n")
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
                    self.string_message("@@Inside Sub Course 'RT Concepts'---\n")
                    header.sub_course_rt_concepts().click()
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_c_language().click()
                    self.string_message("@@Inside Sub Course 'C'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_linux_kernel_and_device_drivers().click()
                    self.string_message("@@Inside Sub Course 'Linux Kernel and Device Drivers'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 3:
                    header.sub_course_arm_embedded_systems().click()
                    self.string_message("@@Inside Sub Course 'ARM Embedded Systems'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 4:
                    header.sub_course_internet_of_things().click()
                    self.string_message("@@Inside Sub Course 'Internet of Things'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 5:
                    header.sub_course_free_rtos().click()
                    self.string_message("@@Inside Sub Course 'free RTOS'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 6:
                    header.sub_course_c_plus_plus_language().click()
                    self.string_message("@@Inside Sub Course 'C++'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 7:
                    header.sub_course_yocto_programming().click()
                    self.string_message("@@Inside Sub Course 'Yocto Programming'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 8:
                    header.sub_course_linux_embedded().click()
                    self.string_message("@@Inside Sub Course 'Linux Embedded'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False

        self.string_message("@Outside Course 'Real-Time' function---\n")

    def course_web_development(self):
        self.string_message("@Inside Course 'Web Development' function---\n")
        header = Header(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            " Web Foundations": "קורס Web Foundations להכיר את היסודות של בניית אתרים» Real Time College",
            " AngularJS | אנגולר": "קורס AngularJS | לימודי אנגולר למתחילים » Real Time College",
            " פייתון |  Python": "קורס פייתון - Python | לימוד שפת פייתון מומלץ למתחילים / מתקדם",
            " CSS3": "קורס CSS3 | ללמוד הצגה ועיצוב של דפי אינטרנט :Real Time Group",
            " NodeJS": "קורס NodeJS | הקורס המקיף והמעשי ביותר בארץ :Real Time Group",
            " Javascript": "קורס JavaScript & jQuery של Real Time College מקבוצה של RTG",
            " TypeScript": "קורס TypeScript | התמחות בכלים של Google » Real Time Group",
            " MongoDB": "קורס MongoDB | ללמוד BigData - MongoDB בקלות! | Real Time Group",
            " HTML5": "קורס HTML | לימודי html5 עם המומחים של Real Time College",
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
                    self.string_message("@@Inside Sub Course 'Web Foundations'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 1:
                    header.sub_course_angular_js().click()
                    self.string_message("@@Inside Sub Course 'AngularJS'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 2:
                    header.sub_course_python_language().click()
                    self.string_message("@@Inside Sub Course 'Python'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 3:
                    header.sub_course_css_language().click()
                    self.string_message("@@Inside Sub Course 'CSS3'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 4:
                    header.sub_course_node_js().click()
                    self.string_message("@@Inside Sub Course 'NodeJS'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 5:
                    header.sub_course_javascript_language().click()
                    self.string_message("@@Inside Sub Course 'Javascript'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 6:
                    header.sub_course_typescript_language().click()
                    self.string_message("@@Inside Sub Course 'Typescript'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 7:
                    header.sub_course_mongodb().click()
                    self.string_message("@@Inside Sub Course 'MongoDB'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 8:
                    header.sub_course_html5().click()
                    self.string_message("@@Inside Sub Course 'HTML5'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 9:
                    header.sub_course_react().click()
                    self.string_message("@@Inside Sub Course 'React'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 10:
                    header.sub_course_java_language().click()
                    self.string_message("@@Inside Sub Course 'Java'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 11:
                    header.sub_course_bootstrap().click()
                    self.string_message("@@Inside Sub Course 'Bootstrap'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 12:
                    header.sub_course_app_development_for_android().click()
                    self.string_message("@@Inside Sub Course 'App Development for Android'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 13:
                    header.sub_course_git().click()
                    self.string_message("@@Inside Sub Course 'GIT'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 14:
                    header.sub_course_sql().click()
                    self.string_message("@@Inside Sub Course 'SQL'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("@Outside Course 'Web Development' function---\n")

    def course_cyber_security(self):
        self.string_message("@Inside Course 'Cyber Security' function---\n")
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
                    self.string_message("@@Inside Sub Course 'Preparations for Certification Exam'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_cyber_attack_infrastructure().click()
                    self.string_message("@@Inside Sub Course 'Cyber Attack Infrastructure'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_malware_analysis().click()
                    self.string_message("@@Inside Sub Course 'Malware Analysis'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 3:
                    header.sub_course_penetration_testing().click()
                    self.string_message("@@Inside Sub Course 'Penetration Testing'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 4:
                    header.sub_course_linux_fundamentals().click()
                    self.string_message("@@Inside Sub Course 'Linux Fundamentals'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 5:
                    header.sub_course_cyber_security_fundamentals().click()
                    self.string_message("@@Inside Sub Course 'Cyber Security Fundamentals'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 6:
                    header.sub_course_networking().click()
                    self.string_message("@@Inside Sub Course 'Networking'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 7:
                    header.sub_course_forensics_investigation_and_incident_response().click()
                    self.string_message("@@Inside Sub Course 'Forensics Investigation and Incident Response'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("@Outside Course 'Cyber Security' function---\n")

    def course_devops(self):
        self.string_message("@Inside Course 'DevOps' function---\n")
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
                    self.string_message("@@Inside Sub Course 'Docker'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_linux_admin().click()
                    self.string_message("@@Inside Sub Course 'Linux Admin'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_kubernetes().click()
                    self.string_message("@@Inside Sub Course 'Kubernetes'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 3:
                    header.sub_course_python_language().click()
                    self.string_message("@@Inside Sub Course 'Python'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 4:
                    header.sub_course_zabbix().click()
                    self.string_message("@@Inside Sub Course 'Zabbix'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                if index == 5:
                    header.sub_course_terraform().click()
                    self.string_message("@@Inside Sub Course 'Terraform'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 6:
                    header.sub_course_networking().click()
                    self.string_message("@@Inside Sub Course 'Networking'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 7:
                    header.sub_course_ansible().click()
                    self.string_message("@@Inside Sub Course 'Ansible'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 8:
                    header.sub_course_bash_scripting().click()
                    self.string_message("@@Inside Sub Course 'Bash Scripting'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 9:
                    header.sub_course_aws().click()
                    self.string_message("@@Inside Sub Course 'AWS'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 10:
                    header.sub_course_jenkins().click()
                    self.string_message("@@Inside Sub Course 'Jenkins'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("@Outside Course 'DevOps' function---\n")

    def course_data_science(self):
        self.string_message("@Inside Course 'Data Science' function---\n")
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
                    self.string_message("@@Inside Sub Course 'Machine Learning Fundamentals'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_machine_learning_with_python().click()
                    self.string_message("@@Inside Sub Course 'Machine Learning with Python'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_deep_learning_with_tensorflow().click()
                    self.string_message("@@Inside Sub Course 'Deep Learning with Tensorflow'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("@Outside Course 'Data Science' function---\n")

    def course_software_testing(self):
        self.string_message("@Inside Course 'Software Testing' function---\n")
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
                    self.string_message("@@Inside Sub Course 'Selenium'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_labview().click()
                    self.string_message("@@Inside Sub Course 'Labview'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_jira().click()
                    self.string_message("@@Inside Sub Course 'Jira'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 3:
                    header.sub_course_qa_methodologies().click()
                    self.string_message("@@Inside Sub Course 'QA Methodologies'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 4:
                    header.sub_course_java_language().click()
                    self.string_message("@@Inside Sub Course 'Java'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("@Outside Course 'Software Testing' function---\n")

    def course_network_and_sysadmin(self):
        self.string_message("@Inside Course 'Network and Sysadmin' function---\n")
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
                    self.string_message("@@Inside Sub Course 'Linux Admin'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_lpic_2().click()
                    self.string_message("@@Inside Sub Course 'LPIC-2'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_linux_fundamentals().click()
                    self.string_message("@@Inside Sub Course 'Linux Fundamentals'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 3:
                    header.sub_course_lpic_1().click()
                    self.string_message("@@Inside Sub Course 'LPIC-1'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 4:
                    header.sub_course_networking().click()
                    self.string_message("@@Inside Sub Course 'Networking'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("@Outside Course 'Network and Sysadmin' function---\n")

    def course_programming_language(self):
        self.string_message("@Inside Course 'Programming Languages' function---\n")
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
                    self.string_message("@@Inside Sub Course 'Java'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_c_language().click()
                    self.string_message("@@Inside Sub Course 'C'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_javascript_language().click()
                    self.string_message("@@Inside Sub Course 'Javascript'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 3:
                    header.sub_course_python_language().click()
                    self.string_message("@@Inside Sub Course 'Python'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 4:
                    header.sub_course_c_plus_plus_language().click()
                    self.string_message("@@Inside Sub Course 'C++'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("@Outside Course 'Programming Languages' function---\n")

    def course_cloud_computing(self):
        self.string_message("@Inside Course 'Cloud Computing' function---\n")
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
                    self.string_message("@@Inside Sub Course 'AWS'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_microsoft_azure().click()
                    self.string_message("@@Inside Sub Course 'Microsoft Azure'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("@Outside Course 'Cloud Computing' function---\n")

    def course_image_processing(self):
        self.string_message("@Inside Course 'Image Processing' function---\n")
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
                    self.string_message("@@Inside Sub Course 'Machine Learning Fundamentals'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_open_cv().click()
                    self.string_message("@@Inside Sub Course 'Open CV'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 2:
                    header.sub_course_cuda().click()
                    self.string_message("@@Inside Sub Course 'CUDA'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 3:
                    header.sub_course_machine_learning_with_python().click()
                    self.string_message("@@Inside Sub Course 'Machine Learning with Python'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 4:
                    header.sub_course_deep_learning_with_tensorflow().click()
                    self.string_message("@@Inside Sub Course 'Deep Learning with Tensorflow'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 5:
                    header.sub_course_nvidia_gpus().click()
                    self.string_message("@@Inside Sub Course 'Nvidia GPUs'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("@Outside Course 'Image Processing' function---\n")

    def course_database_management(self):
        self.string_message("@Inside Course 'Database Management' function---\n")
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
                    self.string_message("@@Inside Sub Course 'SQL'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                elif index == 1:
                    header.sub_course_mongodb().click()
                    self.string_message("@@Inside Sub Course 'MongoDB'---\n")
                    title = header.get_title()
                    expected_title = list(dict_of_titles.values())[index]
                    self.compare_title_pages(title, expected_title, key)
                index += 1
            run = False
        self.string_message("@Outside Course 'Database Managemnt' function---\n")

    # -------------------------------------------5 BUTTONS-------------------------------------------

    def go_to_page_courses_for_companies(self):
        self.string_message("@Inside 'Courses for Companies' function---\n")
        header = Header(self.driver)
        header.courses_for_companies().click()
        title = header.get_title()
        actual_page_title = "Real Time College » Real Time Group's Training Center"
        button_name = 'Courses For Companies'
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("@Outside 'Courses for Companies' function---\n")

    def go_to_page_articles(self):
        self.string_message("@Inside 'Articles' function---\n")
        header = Header(self.driver)
        header.articles().click()
        title = header.get_title()
        actual_page_title = "Realtime Group - מאמרים"
        button_name = 'Articles'
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("@Outside 'Articles' function---\n")

    def go_to_page_about_us(self):
        self.string_message("@Inside 'About Us' function---\n")
        header = Header(self.driver)
        header.about_us().click()
        title = header.get_title()
        actual_page_title = "אודות Real Time Group - חטיבת הדרכה | חטיבת השמה | מיקור חוץ"
        button_name = "About Us"
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("@Outside 'About Us' function---\n")

    def go_to_page_declaration_of_accessibility(self):
        self.string_message("@Inside 'Declaration of Accessibility' function---\n")
        header = Header(self.driver)
        header.declaration_of_accessibility().click()
        title = header.get_title()
        actual_page_title = "הצהרת נגישות » Real Time College"
        button_name = "Declaration Of Accessibility"
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("@Outside 'Declaration of Accessibility' function---\n")

    def go_to_page_jobs(self):
        self.string_message("@Inside 'Jobs' function---\n")
        header = Header(self.driver)
        header.jobs().click()
        title = header.get_title()
        actual_page_title = "Real Time College » Real Time Group's Training Center"
        button_name = "Jobs"
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("@Outside 'Jobs' function---\n")

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
        self.open_file_and_append_string_message()



