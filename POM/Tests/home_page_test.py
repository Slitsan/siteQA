#   07/03/2022
#   Created By Pablik
#   Home Page Test
# ---------------------------------------------------------
import time
from datetime import datetime
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from POM.Pages.home_page import HomePage


# ---------------------------------------------------------
class HomePageTest(unittest.TestCase):
    def __init__(self, init_driver):
        super().__init__()
        self.driver = init_driver
        now = datetime.now()
        current_time = now.strftime("%d%m%H%M%S")
        self.date_for_log = now.strftime("%d %m %Y")
        self.test_user_last_name = "test"
        self.test_user_first_name = "test"
        self.test_user_mail = current_time + "@test.com"
        self.test_user_phone_number = current_time
        self.string_result = "*-----------------------------------TESTING HOME PAGE-----------------------------------------------\n"


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

    # ---------------------------------POPUP METHODS-----------------------------------------
    def popup_form(self, last_name="test", first_name="test", ending_of_mail="@test.com", phone_number="",
                   choose_maslul="yes", tick_terms_and_services="yes", send_button="yes", close_form="yes"):
        self.string_message("@Inside PopUp Form function\n")
        now = datetime.now()
        current_time = now.strftime("%d%m%H%M%S")
        home_page = HomePage(self.driver)
        self.string_message("---Entering last name---\n")
        home_page.last_name_field_in_form_popup().send_keys(last_name)
        self.string_message("---Entering first name---\n")
        home_page.first_name_field_in_form_popup().send_keys(first_name)
        self.string_message("---Entering mail---\n")
        home_page.email_field_in_form_popup().send_keys(current_time + ending_of_mail)
        if phone_number == "":
            phone_number = current_time
        self.string_message("---Entering phone number---\n")
        home_page.phone_field_in_form_popup().send_keys(phone_number)
        if choose_maslul == "yes":
            self.string_message("---Choosing maslul---\n")
            home_page.choose_maslul_in_form_popup().click()
            home_page.choose_maslul_real_time_in_form_popup().click()
        if tick_terms_and_services == "yes":
            self.string_message("---Ticking the terms of agreement and services---\n")
            home_page.terms_of_agreement_field_in_form_popup().click()
        # if send_button == "yes":
        #     self.string_message("---Clicking on the 'send' button---\n")
        #     home_page.send_button_in_form_popup().click()
        if close_form == "yes":
            self.string_message("---Closing the popup form---\n")
            home_page.close_button_in_popup_form().click()
        self.string_message("@Outside PopUp Form function\n")

    # def test_popup_form(self):
    # self.popup_form()
    # self.open_file_and_append_string_message()

    # -----------------------------------------MAIN FORM METHODS---------------------------------------
    def main_form(self, last_name="test", first_name="test", ending_of_mail="@test.com", phone_number="",
                  choose_maslul="yes", tick_terms_and_services="yes", send_button="yes", close_button="yes"):
        self.string_message("@Inside Main Form function\n")
        now = datetime.now()
        current_time = now.strftime("%d%m%H%M%S")
        home_page = HomePage(self.driver)
        self.string_message("---Entering last name---\n")
        home_page.last_name_field_in_main_form().send_keys(last_name)
        self.string_message("---Entering first name---\n")
        home_page.first_name_field_in_main_form().send_keys(first_name)
        self.string_message("---Entering mail---\n")
        home_page.email_field_in_main_form().send_keys(current_time + ending_of_mail)
        if phone_number == "":
            phone_number = current_time
        self.string_message("---Entering phone number---\n")
        home_page.phone_number_field_in_main_form().send_keys(phone_number)
        if choose_maslul == "yes":
            self.string_message("---Choosing maslul---\n")
            home_page.choose_maslul_in_main_form().click()
            home_page.choose_maslul_real_time_in_main_form().click()
        if tick_terms_and_services == "yes":
            self.string_message("---Ticking the terms of agreement and services---\n")
            home_page.terms_of_agreement_field_in_main_form().click()
        # if send_button == "yes":
        #     self.string_message("---Clicking on the 'send' button---\n")
        #     home_page.send_button_in_main_form().click()
        # if close_button == "yes":
        #     self.string_message("---Clicking on the close button---\n")
        #     home_page.close_button_after_filling_the_main_form().click()
        self.string_message("@Outside Main Form function\n")

    # def test_main_form(self):
    #     self.close_popup()
    #     self.main_form()
    #     self.open_file_and_append_string_message()

    # -----------------------------------FLOATING MENU METHODS-------------------------------
    def whatsup_in_floating_menu(self):
        self.string_message("@Inside WhatsUp Button in Floating Menu function\n")
        home_page = HomePage(self.driver)
        try:
            if home_page.whatsup_link_in_floating_menu().is_displayed():
                self.string_message("---Button 'WhatsUp' is presented---\n")
            else:
                self.string_message("!------Button 'WhatsUp' is not presented------!\n")
        except NoSuchElementException:
            self.string_message("!------Element not found------!\n")
        self.string_message("@Outside WhatsUp Button in Floating Menu function\n")

    def floating_form(self, last_name="test", first_name="test", ending_of_mail="@test.com", phone_number="",
                      choose_maslul="yes", tick_terms_and_services="yes", send_button="yes", close_button="yes"):
        self.string_message("@Inside Floating Form function\n")
        now = datetime.now()
        current_time = now.strftime("%d%m%H%M%S")
        home_page = HomePage(self.driver)
        self.string_message("---Clicking on the floating form---\n")
        home_page.form_in_floating_menu().click()
        self.string_message("---Entering last name---\n")
        home_page.last_name_field_in_floating_form().send_keys(last_name)
        self.string_message("---Entering first name---\n")
        home_page.first_name_field_in_floating_form().send_keys(first_name)
        self.string_message("---Entering mail---\n")
        home_page.email_field_in_floating_form().send_keys(current_time + ending_of_mail)
        if phone_number == "":
            phone_number = current_time
        self.string_message("---Entering phone number---\n")
        home_page.phone_number_field_in_floating_form().send_keys(phone_number)
        if choose_maslul == "yes":
            self.string_message("---Choosing maslul---\n")
            home_page.choose_maslul_in_floating_form().click()
            home_page.choose_maslul_real_time_in_floating_form().click()
        if tick_terms_and_services == "yes":
            self.string_message("---Ticking the terms of agreement and services---\n")
            home_page.terms_of_agreement_field_in_floating_form().click()
        # if send_button == "yes":
        #     self.string_message("---Clicking on the 'send' button---\n")
        #     home_page.send_button_in_floating_form().click()
        if close_button == "yes":
            self.string_message("---Clicking on the close button---\n")
            home_page.close_button_in_floating_form().click()
        self.string_message("@Outside Floating Form function\n")

    def contact_us_in_floating_menu(self):
        self.string_message("@Inside Contact Us Button in Floating Menu function---\n")
        home_page = HomePage(self.driver)
        try:
            if home_page.about_us_in_floating_menu().is_displayed():
                self.string_message("---Button 'Contact Us' is presented---\n")
            else:
                self.string_message("!------Button 'Contact Us' is not presented------!\n")
        except NoSuchElementException:
            self.string_message("!------Element not found------!\n")
        self.string_message("@Outside Contact Us Button in Floating Menu function---\n")

    # ----------------------------------TRAINING TEST-------------------------------------
    def opens_tab_and_compares_title(self, course, dict_of_titles, index):
        href = course.get_attribute("href")
        self.driver.execute_script("window.open('');")
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        self.driver.get(href)
        title = self.driver.title
        expected_title = list(dict_of_titles.values())[index]
        self.compare_title_pages(title, expected_title, list(dict_of_titles.keys())[index])
        self.driver.close()
        self.driver.switch_to.window(tabs[0])

    def enter_each_training_and_compare_title(self):
        self.string_message("@Inside 'Training and Placement Tracks for High-Tech Professions' function---\n")
        home_page = HomePage(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            "Real-Time Embedded": "קורס Real Time Embedded Linux » Real Time College",
            "Cyber Security": "קורס Cyber אבטחת מידע וסייבר | Cyber Security » Real Time Group",
            "Fullstack Developer": "קורס Full Stack | לימודי Full Stack | קורס Web Development",
            "DevOps": "קורס DevOps | קורס דאבאופס ניהול פרויקטים בפיתוח » Real Time Group",
            "Automation and QA": "קורס QA | קורס בודק תוכנה QA - כולל סטאז' מעשי » Real Time College",
            "Machine Learning": "קורס machine learning | הכשרה והשמה :Real Time Group"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for course in home_page.training_and_placement_tracks_for_high_tech_professions():
                self.opens_tab_and_compares_title(course, dict_of_titles, index)
                index += 1
            run = False
        self.string_message("@Outside 'Training and Placement Tracks for High-Tech Professions' function---\n")

    # -----------------------------------LIST OF COURSES ON HOME PAGE----------------------
    def enter_each_course_on_bootcamp_real_time_and_compare_title(self):
        self.string_message("@Inside 'Real-Time Bootcamp' course table in home page function---\n")
        home_page = HomePage(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            "C language": "קורס שפת C | לימודים שפת | C למתחילים :Real Time Group",
            "Linux Admin": "קורס לינוקס Linux Admin | ניהול מערכות הפעלה - Real Time College",
            "Bash Scripting": "קורס Bash Scripting | תיכנות בסביבת לינוקס » Real Time Group",
            "RT Concepts": "קורס RT Concepts | מבוא למערכות משובצות מחשב » Real Time Group",
            "Python language": "קורס פייתון - Python | לימוד שפת פייתון מומלץ למתחילים / מתקדם",
            "ARM Embedded Systems": "קורס Arm - Embedded Systems | פיתוח תוכנה - Real Time College",
            "Embedded Linux": "קורס Embedded Linux | פיתוח מערכות משובצות מחשב » Real Time Group",
            "Networking": "קורס Networking | לימודי מעשי בתקשורת הנתונים » Real Time College",
            "C++ Language": "קורס שפת C למתחילים / שפת C ++ למתקדמים | ללמוד » Real Time College",
            "Linux Kernel And Device Driver": "קורס Linux Kernel and Device Drivers | מערכות משובצות מחשב בסביבת לינוקס"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for course in home_page.list_of_courses_on_bootcamp_real_time_on_home_page():
                self.opens_tab_and_compares_title(course, dict_of_titles, index)
                index += 1
            run = False
        self.string_message("@Outside 'Real-Time Bootcamp' course table in home page function---\n")

    def enter_each_course_on_bootcamp_fullstack_and_compare_title(self):
        self.string_message("@Inside 'Full-Stack Bootcamp' course table in home page function---\n")
        home_page = HomePage(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            "Web Foundations": "קורס Web Foundations להכיר את היסודות של בניית אתרים» Real Time College",
            "HTML5": "קורס HTML | לימודי html5 עם המומחים של Real Time College",
            "CSS3": "קורס CSS3 | ללמוד הצגה ועיצוב של דפי אינטרנט :Real Time Group",
            "JavaScript": "קורס JavaScript & jQuery של Real Time College מקבוצה של RTG",
            "SQL": "קורס SQL למתחילים | ניהול בסיסי נתונים :Real Time Group",
            "MongoDB": "קורס MongoDB | ללמוד BigData - MongoDB בקלות! | Real Time Group",
            "NodeJS": "קורס NodeJS | הקורס המקיף והמעשי ביותר בארץ :Real Time Group",
            "TypeScript": "קורס TypeScript | התמחות בכלים של Google » Real Time Group",
            "AngularJS": "קורס AngularJS | לימודי אנגולר למתחילים » Real Time College",
            "GIT (Version Control)": "קורס Version Control עם המומחים » Real Time Group"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for course in home_page.list_of_courses_on_bootcamp_fullstack_on_home_page():
                self.opens_tab_and_compares_title(course, dict_of_titles, index)
                index += 1
            run = False
        self.string_message("@Outside 'Full-Stack Bootcamp' course table in home page function---\n")

    def enter_each_course_on_bootcamp_qa_and_compare_title(self):
        self.string_message("@Inside 'QA Bootcamp' course table in home page function---\n")
        home_page = HomePage(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            "Computer Architecture": "קורס Computer Architecture - קורס מבנה מחשבים | Real Time Group",
            "QA Methodologies": "קורס מתודולוגיות QA עם המומחים של Real Time College",
            "Linux Admin": "קורס לינוקס Linux Admin | ניהול מערכות הפעלה - Real Time College",
            "Bash Scripting": "קורס Bash Scripting | תיכנות בסביבת לינוקס » Real Time Group",
            "Python Language": "קורס פייתון - Python | לימוד שפת פייתון מומלץ למתחילים / מתקדם",
            "SQL": "קורס SQL למתחילים | ניהול בסיסי נתונים :Real Time Group",
            "Java Language": "קורס Java | למידת שפת Java למתחילים / מתקדמים » Real Time Group",
            "GIT (Version Control)": "קורס Version Control עם המומחים » Real Time Group",
            "Jenkins": "קורס Jenkins - למד לעבוד עם ג'נקינס בצורה הטובה ביותר! | Real Time Group",
            "JIRA": "קורס JIRA | בואו להתמקצע ולצבור ניסיון בכלי המוביל למעקב באגים",
            "Networking": "קורס Networking | לימודי מעשי בתקשורת הנתונים » Real Time College"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for course in home_page.list_of_courses_on_bootcamp_qa_on_home_page():
                self.opens_tab_and_compares_title(course, dict_of_titles, index)
                index += 1
            run = False
        self.string_message("@Outside 'QA Bootcamp' course table in home page function---\n")

    def enter_each_course_on_bootcamp_cyber_security_and_compare_title(self):
        self.string_message("@Inside 'Cyber Security Bootcamp' course table in home page function---\n")
        home_page = HomePage(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            "Linux Admin": "קורס לינוקס Linux Admin | ניהול מערכות הפעלה - Real Time College",
            "Bash Scripting": "קורס Bash Scripting | תיכנות בסביבת לינוקס » Real Time Group",
            "Python Language": "קורס פייתון - Python | לימוד שפת פייתון מומלץ למתחילים / מתקדם",
            "GIT (Version Control)": "קורס Version Control עם המומחים » Real Time Group",
            "Networking": "קורס Networking | לימודי מעשי בתקשורת הנתונים » Real Time College",
            "Cyber Security Fundamentals": "קורס Cyber Security Fundamentals | סייבר ואבטחת מידע :Real Time Group",
            "Cyber Attack Infrastructure": "קורס Cyber Attack Infrastructure - לזהות נקודות תורפה | Real Time College",
            "SOC Analyst with SIEM": "קורס SOC Analyst with SIEM | לימודי אנליסט סייבר » Real Time College",
            "Malware Analysis": "קורס Malware Analysis לפרק ולהבין איומים פוטנציאלים » Real Time College",
            "Forensics Investigation & Incident Response": "קורס Forensics Investigation & Incident Response » Real Time College",
            "Penetration Testing": "קורס Penetration Testing - מבחני חדירות » Real Time College",
            "CEH": "הכנה לבחינת הסמכה CEH » Real Time College"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for course in home_page.list_of_courses_on_bootcamp_cyber_security_on_home_page():
                self.opens_tab_and_compares_title(course, dict_of_titles, index)
                index += 1
            run = False
        self.string_message("@Outside 'Cyber Security Bootcamp' course table in home page function---\n")

    def enter_each_course_on_bootcamp_machine_learning_and_compare_title(self):
        self.string_message("@Inside 'Machine Learning Bootcamp' course table in home page function---\n")
        home_page = HomePage(self.driver)
        index = 0
        run = True
        dict_of_titles = {
            "Python Language": "קורס פייתון - Python | לימוד שפת פייתון מומלץ למתחילים / מתקדם",
            "SQL": "קורס SQL למתחילים | ניהול בסיסי נתונים :Real Time Group",
            "Machine Learning Fundamentals": "קורס Machine Learning Fundamentals » Real Time College",
            "Scientific Python": "קורס Scientific Python במכללת Real Time College RTG",
            "Machine Learning With Python": "קורס Machine Learning with Python » Real Time College",
            "Deep Learning With Tensorflow": "קורס פיתוח Deep Learning with Tensorflow » Real Time College",
            "AWS": "קורס AWS | התמחות בכלי שירותי הענן של אמזון :Real Time Group"}
        keys_of_dict_of_titles = dict_of_titles.keys()

        while run:
            for course in home_page.list_of_courses_on_bootcamp_machine_learning_on_home_page():
                self.opens_tab_and_compares_title(course, dict_of_titles, index)
                index += 1
            run = False
        self.string_message("@Outside 'Machine Learning Bootcamp' course table in home page function---\n")

    # -------------------------------------------DEPARTMENT PAGES-------------------------------
    def department_pages(self):
        self.string_message("@Inside Department Pages function\n")
        home_page = HomePage(self.driver)
        actions = ActionChains(self.driver)
        index_of_dict = 0
        running = True
        dict_of_urls = {
            "Development Department": "https://rt-projects.com/",
            "Education Department": "https://rt-ed.co.il/",
            "HR Department": "https://rt-hr.co.il/"
        }
        while running:
            for key in dict_of_urls.keys():
                if index_of_dict == 0:
                    actions.move_to_element(home_page.development_apartment()).click().perform()
                    tabs = self.driver.window_handles
                    self.driver.switch_to.window(tabs[1])
                    url = "https://rt-projects.com/"
                    actual_url = list(dict_of_urls.values())[index_of_dict]
                    self.compare_title_pages(url, actual_url, key)
                    self.driver.close()
                    self.driver.switch_to.window(tabs[0])
                elif index_of_dict == 1:
                    actions.move_to_element(home_page.teaching_apartment()).click().perform()
                    tabs = self.driver.window_handles
                    self.driver.switch_to.window(tabs[1])
                    url = "https://rt-ed.co.il/"
                    actual_url = list(dict_of_urls.values())[index_of_dict]
                    self.compare_title_pages(url, actual_url, key)
                    self.driver.close()
                    self.driver.switch_to.window(tabs[0])
                elif index_of_dict == 2:
                    actions.move_to_element(home_page.hr_apartment()).click().perform()
                    tabs = self.driver.window_handles
                    self.driver.switch_to.window(tabs[1])
                    url = "https://rt-hr.co.il/"
                    actual_url = list(dict_of_urls.values())[index_of_dict]
                    self.compare_title_pages(url, actual_url, key)
                    self.driver.close()
                    self.driver.switch_to.window(tabs[0])
                index_of_dict += 1
            running = False
        self.string_message("@Outside Department Pages function\n")

    # -------------------------------------------------TEST-------------------------------------------------------------------
    def test_run_all(self):
        self.popup_form()
        self.main_form()
        self.whatsup_in_floating_menu()
        self.floating_form()
        self.contact_us_in_floating_menu()
        self.enter_each_training_and_compare_title()
        self.enter_each_course_on_bootcamp_real_time_and_compare_title()
        self.enter_each_course_on_bootcamp_fullstack_and_compare_title()
        self.enter_each_course_on_bootcamp_qa_and_compare_title()
        self.enter_each_course_on_bootcamp_cyber_security_and_compare_title()
        self.enter_each_course_on_bootcamp_machine_learning_and_compare_title()
        self.department_pages()
        self.open_file_and_append_string_message()
