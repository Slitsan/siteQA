#   Footer test
# --------------------------------------------------------------------------------------
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from POM.Pages.footer import Footer
from datetime import datetime

# -------------------------------------

popUp_close_XPATH = '//*[@id="lead-form-modal1"]/span'


class FooterTest(unittest.TestCase):
    def __init__(self, init_driver):
        super().__init__()
        self.driver = init_driver
        now = datetime.now()
        self.date_for_log = now.strftime("%d %m %Y")
        self.string_result = "*-----------------------------------TESTING Footer-----------------------------------------------\n"

    def compare_title_pages(self, title: str, actual_page_title: str, button_name: str):
        actual_title_of_page = actual_page_title
        self.string_message(f"---Checking The {button_name} Page...---\n")
        self.string_message(f"---Expected title {title} ---\n")
        self.string_message(f"---Actual title {actual_page_title} ---\n")
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

    # -------------------------------------------Real Time-------------------------------------------

    def real_time_list(self):
        self.string_message("@Inside Real-Time function---\n")
        footer = Footer(self.driver)
        dict_of_titles = {"Internet Of Things": "קורס Internet Of Things | מה זה IOT ואיך זה יכול לשנות על חיינו?",
                          "FreeRTOS": "קורס Free Rtos - ללמוד איזה תכנית תזכה במעבד בכל נקודת זמן",
                          "שפת ++C": "קורס שפת C למתחילים / שפת C ++ למתקדמים | ללמוד » Real Time College",
                          "Yocto Programming": "YOCTO programming | מערכות Embedded Linux » Real Time College",
                          "Embedded Linux": "קורס Embedded Linux | פיתוח מערכות משובצות מחשב » Real Time Group",
                          "RT Concepts": "קורס RT Concepts | מבוא למערכות משובצות מחשב » Real Time Group",
                          "שפת C": "קורס שפת C | לימודים שפת | C למתחילים :Real Time Group",
                          "Linux Kernel And Device Drivers": "קורס Linux Kernel and Device Drivers | מערכות משובצות מחשב בסביבת לינוקס",
                          "ARM - Embedded Systems": "קורס Arm - Embedded Systems | פיתוח תוכנה - Real Time College"}
        real_time = footer.list_of_real_time()
        links = {}
        for element in real_time:
            text = element.text
            ref = element.get_dom_attribute("href")
            links[text] = ref
        for key in links:
            self.driver.get(links[key])
            time.sleep(3)
            title = footer.get_title()
            expected_title = dict_of_titles[key]
            self.compare_title_pages(expected_title, title, key)
            time.sleep(3)

        self.string_message("@Outside  Real-Time function---\n")

        # -------------------------------------------web-------------------------------------------

    def web_development_list(self):
        self.string_message("@Inside web_development function---\n")
        footer = Footer(self.driver)
        dict_of_titles = {"Web Foundations": "קורס Web Foundations להכיר את היסודות של בניית אתרים» Real Time College",
                          "AngularJS | אנגולר": "קורס AngularJS | לימודי אנגולר למתחילים » Real Time College",
                          "פייתון | Python": "קורס פייתון - Python | לימוד שפת פייתון מומלץ למתחילים / מתקדם",
                          "CSS3": "קורס CSS3 | ללמוד הצגה ועיצוב של דפי אינטרנט :Real Time Group",
                          "NodeJS": "קורס NodeJS | הקורס המקיף והמעשי ביותר בארץ :Real Time Group",
                          "Javascript": "קורס JavaScript & jQuery של Real Time College מקבוצה של RTG",
                          "TypeScript": "קורס TypeScript | התמחות בכלים של Google » Real Time Group",
                          "MongoDB": "קורס MongoDB | ללמוד BigData - MongoDB בקלות! | Real Time Group",
                          "HTML5": "קורס HTML | לימודי html5 עם המומחים של Real Time College",
                          "React | ריאקט": "קורס React | לימודי תכנות ופיתוח אפליקציות React native JS",
                          "Java": "קורס Java | למידת שפת Java למתחילים / מתקדמים » Real Time Group",
                          "Bootstrap": "קורס Bootstrap | בניית אתרי אינטרנט בעזרת בוטסטראפ",
                          "פיתוח אפליקציות לאנדרואיד": "קורס פיתוח אפליקציות לאנדרואיד | פיתוח אפליקציות תוך שימוש בשפת התכנות Java",
                          "GIT (Version Control)": "קורס Version Control עם המומחים » Real Time Group",
                          "SQL": "קורס SQL למתחילים | ניהול בסיסי נתונים :Real Time Group", }

        web_development = footer.list_of_web_development()
        links = {}
        for element in web_development:
            text = element.text
            ref = element.get_dom_attribute("href")
            links[text] = ref

        for key in links:
            self.driver.get(links[key])
            time.sleep(3)
            title = footer.get_title()
            expected_title = dict_of_titles[key]
            self.compare_title_pages(expected_title, title, key)
            time.sleep(3)

        self.string_message("@Outside  web_development function---\n")

        # -------------------------------------------Cyber Security-------------------------------------------

    def cyber_security_list(self):
        self.string_message("@Inside Cyber Security function---\n")
        footer = Footer(self.driver)
        dict_of_titles = {
            "הכנה לבחינת הסמכה C | EH": "הכנה לבחינת הסמכה CEH » Real Time College",
            "Cyber Attack Infrastructure": "קורס Cyber Attack Infrastructure - לזהות נקודות תורפה | Real Time College",
            "Malware Analysis": "קורס Malware Analysis לפרק ולהבין איומים פוטנציאלים » Real Time College",
            "Penetration Testing": "קורס Penetration Testing - מבחני חדירות » Real Time College",
            "Linux Fundamentals": "קורס Linux Fundamentals -כל הידע והפרקטיקה הנדרשים » Real Time College",
            "Cyber Security Fundamentals": "קורס Cyber Security Fundamentals | סייבר ואבטחת מידע :Real Time Group",
            "Networking": "קורס Networking | לימודי מעשי בתקשורת הנתונים » Real Time College",
            "Forensics Investigation & Incident Response": "קורס Forensics Investigation & Incident Response » Real Time College"
        }

        cyber_security = footer.list_cyber_security()
        links = {}
        for element in cyber_security:
            text = element.text
            ref = element.get_dom_attribute("href")
            links[text] = ref
        for key in links:
            self.driver.get(links[key])
            time.sleep(3)
            title = footer.get_title()
            expected_title = dict_of_titles[key]
            self.compare_title_pages(expected_title, title, key)
            time.sleep(3)

        self.string_message("@Outside  cyber_security function---\n")

    def devops_list(self):
        self.string_message("@Inside devops function---\n")
        footer = Footer(self.driver)
        dict_of_titles = {
            "Docker Containers": "קורס Docker - פלטפורמת תוכנה מובילה לניהול יישומים והרצת קוד בקונטיינרים",
            "לינוקס | Linux Admin": "קורס לינוקס Linux Admin | ניהול מערכות הפעלה - Real Time College",
            "Kubernetes": "קורס Kubernetes | לימוד קוברנטיס מעשי » Real Time College",
            "פייתון | Python": "קורס פייתון - Python | לימוד שפת פייתון מומלץ למתחילים / מתקדם",
            "Zabbix": "קורס Zabbix | מעקב אחר פעילות שירותי ענן » Real Time Group",
            "Terraform": "קורס Terraform - ניהול תשתיות בענן » Real Time College",
            "Networking": "קורס Networking | לימודי מעשי בתקשורת הנתונים » Real Time College",
            "ANSIBLE": "קורס ANSIBLE - כלי לניהול ופיתוח כלי אוטומציה » Real Time College",
            "Bash Scripting": "קורס Bash Scripting | תיכנות בסביבת לינוקס » Real Time Group",
            "AWS": "קורס AWS | התמחות בכלי שירותי הענן של אמזון :Real Time Group",
            "Jenkins": "קורס Jenkins - למד לעבוד עם ג'נקינס בצורה הטובה ביותר! | Real Time Group"}

        devops = footer.list_of_devops()
        links = {}
        for element in devops:
            text = element.text
            ref = element.get_dom_attribute("href")
            links[text] = ref
        for key in links:
            self.driver.get(links[key])
            time.sleep(3)
            title = footer.get_title()
            expected_title = dict_of_titles[key]
            self.compare_title_pages(expected_title, title, key)
            time.sleep(3)

        self.string_message("@Outside  devops function---\n")

    def data_science_list(self):
        self.string_message("@Inside Course 'Data Science' function---\n")
        footer = Footer(self.driver)

        dict_of_titles = {
            "Machine Learning Fundamentals": "קורס Machine Learning Fundamentals » Real Time College",
            "Machine Learning With Python": "קורס Machine Learning with Python » Real Time College",
            "Deep Learning With Tensorflow": "קורס פיתוח Deep Learning with Tensorflow » Real Time College"}
        data_science = footer.list_of_data_science()
        links = {}
        for element in data_science:
            text = element.text
            ref = element.get_dom_attribute("href")
            links[text] = ref
        for key in links:
            self.driver.get(links[key])
            time.sleep(3)
            title = footer.get_title()
            expected_title = dict_of_titles[key]
            self.compare_title_pages(expected_title, title, key)
            time.sleep(3)

        self.string_message("@Outside  data science function---\n")

    def software_testing_list(self):
        self.string_message("@Inside Course 'Software Testing' function---\n")
        footer = Footer(self.driver)
        dict_of_titles = {
            "Selenium": "קורס Selenium - לימודי פיתוח אוטומציה | הקורס הכי מקיף ומעשי בארץ",
            "LabView": "קורס LabView - לימוד מעשי וממוקד לפיתוח בפלטפורמת LabView",
            "JIRA | ג'ירה": "קורס JIRA | בואו להתמקצע ולצבור ניסיון בכלי המוביל למעקב באגים",
            "מתודולוגיות QA": "קורס מתודולוגיות QA עם המומחים של Real Time College",
            "Java": "קורס Java | למידת שפת Java למתחילים / מתקדמים » Real Time Group"
        }
        software_testing = footer.list_of_software_testing()

        links = {}
        for element in software_testing:
            text = element.text
            ref = element.get_dom_attribute("href")
            links[text] = ref
        for key in links:
            self.driver.get(links[key])
            time.sleep(3)
            title = footer.get_title()
            expected_title = dict_of_titles[key]
            self.compare_title_pages(expected_title, title, key)
            time.sleep(3)

        self.string_message("@Outside  software testing function---\n")

    #
    def image_processing_list(self):
        self.string_message("@Inside Course 'Image Processing' function---\n")
        footer = Footer(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            "Machine Learning Fundamentals": "קורס Machine Learning Fundamentals » Real Time College",
            "OpenCV": "קורס OpenCV | לפתח קריירה בחזית התעשייה בתחום של Image Processing",
            "CUDA": "קורס CUDA | לנצל את הכוח GPU של המחשב » Real Time College",
            "Machine Learning With Python": "קורס Machine Learning with Python » Real Time College",
            "Deep Learning With Tensorflow": "קורס פיתוח Deep Learning with Tensorflow » Real Time College",
            "Nvidia GPUs": "קורס Nvidia GPUs | שימוש לטובת פיתוח עיבוד תמונה לצורך פרוייקטים"
        }
        image_processing = footer.list_of_image_processing()
        links = {}
        for element in image_processing:
            text = element.text
            ref = element.get_dom_attribute("href")
            links[text] = ref
        for key in links:
            self.driver.get(links[key])
            time.sleep(3)
            title = footer.get_title()
            expected_title = dict_of_titles[key]
            self.compare_title_pages(expected_title, title, key)
            time.sleep(3)

        self.string_message("@Outside  image processing function---\n")

    #  -------------------------------------------others-------------------------------------------
    def go_to_page_articles(self):
        self.string_message("@Inside 'Articles' function---\n")
        footer = Footer(self.driver)
        footer.articles().click()
        title = footer.get_title()
        actual_page_title = "Realtime Group - מאמרים"
        button_name = 'Articles'
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("@Outside 'Articles' function---\n")

    def go_to_page_about_us(self):
        self.string_message("@Inside 'About Us' function---\n")
        footer = Footer(self.driver)
        footer.about_us().click()
        title = footer.get_title()
        actual_page_title = "אודות Real Time Group - חטיבת הדרכה | חטיבת השמה | מיקור חוץ"
        button_name = "About Us"
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("@Outside 'About Us' function---\n")

    def go_to_page_declaration_of_accessibility(self):
        self.string_message("@Inside 'Declaration of Accessibility' function---\n")
        footer = Footer(self.driver)
        footer.declaration_of_accessibility().click()
        title = footer.get_title()
        actual_page_title = "הצהרת נגישות » Real Time College"
        button_name = "Declaration Of Accessibility"
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("@Outside 'Declaration of Accessibility' function---\n")

    def go_to_page_privacy_policy(self):
        self.string_message("@Inside 'privacy_policy' function---\n")
        footer = Footer(self.driver)
        footer.privacy_policy().click()
        title = footer.get_title()
        actual_page_title = "מדיניות פרטיות » Real Time College"
        button_name = "privacy_policy"
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("@Outside 'privacy_policy' function---\n")

    def go_to_page_jobs(self):
        self.string_message("@Inside 'Jobs' function---\n")
        footer = Footer(self.driver)
        footer.jobs().click()
        title = footer.get_title()
        actual_page_title = "Real Time Group - דרושים"
        button_name = "Jobs"
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("@Outside 'Jobs' function---\n")

    def go_to_page_courses_for_companies(self):
        self.string_message("@Inside 'courses_for_companies' function---\n")
        footer = Footer(self.driver)
        footer.courses_for_companies().click()
        title = footer.get_title()
        actual_page_title = "Real Time College » Real Time Group's Training Center"
        button_name = "Courses For Companies"
        self.compare_title_pages(title, actual_page_title, button_name)
        self.string_message("@Outside 'courses_for_companies' function---\n")

    def social_links(self):
        self.string_message("@Inside Social function---\n")
        footer = Footer(self.driver)
        links = footer.social_links()
        expected_texts = [
            "נחלת יצחק 32, תל אביב-יפו",
            "info@rt-ed.co.il",
            "+972 77 7067 057",
            "RT-Collage"
        ]

        for index in range(len(links)):
            if (links[index].text == expected_texts[index]):
                print("Data of social links is correct")
            else:
                print("Data of social links is wrong")
        self.string_message("@Outside 'social links' function---\n")

    def info(self):
        self.string_message("@Inside info function---\n")
        footer = Footer(self.driver)
        link = footer.site_info()
        expected_text = "מרכז ללימודי מקצועות ההייטק המשלב הכשרה, סטאז' בבית תוכנה והשמה"
        if link.text == expected_text:
            print("Data of info link is correct")
        else:
            print("Data of info link is wrong")
        self.string_message("@Outside info function---\n")

    # -------------------------------------------TEST-------------------------------------------
    def run_others(self):
        self.go_to_page_courses_for_companies()
        self.go_to_page_articles()
        self.go_to_page_about_us()
        self.go_to_page_declaration_of_accessibility()
        self.go_to_page_privacy_policy()
        self.go_to_page_jobs()

    def run_colons(self):
        self.real_time_list()
        self.web_development_list()
        self.cyber_security_list()
        self.devops_list()
        self.data_science_list()
        self.software_testing_list()
        self.image_processing_list()

    def test_social_links(self):
        self.social_links()

    def test_info(self):
        self.info()

    def test_footer(self):
        self.run_colons()
        self.run_others()
        self.test_social_links()
        self.test_info()
        self.open_file_and_append_string_message()
