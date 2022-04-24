#   13/03/2022
#   Created By Pablik
#   Courses Page Syllabus Test
# -----------------------------------------------------
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from datetime import datetime
from POM.Pages.course_page import CoursePage
# -----------------------------------------------------
from POM.Pages.header import Header


class CoursePageTest(unittest.TestCase):
    def __init__(self, init_driver):
        super().__init__()
        self.driver = init_driver
        now = datetime.now()
        self.date_for_log = now.strftime("%d %m %Y")
        self.string_result = "*-----------------------------------TESTING COURSE PAGE-----------------------------------------------\n"

    # Compares the syllabus url with a given url inside the 'maslul functions'
    def compare_syllabus_url(self, title: str, actual_page_title: str, button_name: str):
        actual_title_of_page = actual_page_title
        self.string_message(f"---Checking The {button_name} Syllabus---\n")
        if title == actual_title_of_page:
            self.string_message("---The syllabus is correct---\n")
            return True
        else:
            self.string_message("!------Not the right syllabus------!\n")
            return False

    # Appends the message parameter to the string_result
    def string_message(self, message):
        print(message)
        self.string_result += message

    # Opens a new file if there is not one. Appends the string to it
    def open_file_and_append_string_message(self):
        try:
            file = open(f"./Source/log {self.date_for_log}.txt", "a+")
            file.write(self.string_result)
            file.close()
        except FileNotFoundError:
            print("Did not found a file")

    # Switches tabs and gets the syllabus url and compares it
    def switching_tabs_and_comparing_urls(self, dict_of_titles, index, key):
        tabs = self.driver.window_handles  # Takes all the tabs that are currently presented
        self.driver.switch_to.window(tabs[1])
        main_tab = tabs.pop(0)
        url = self.driver.current_url
        expected_url = list(dict_of_titles.values())[index]
        self.compare_syllabus_url(url, expected_url, key)
        for tab in tabs:  # Closes the syllabus tab after comparing the URLs
            self.driver.switch_to.window(tab)
            self.driver.close()
        self.driver.switch_to.window(main_tab)

    # Prepares a dictionary of nav buttons according to page
    def prepares_dictionary_of_div_block(self, course_page):
        dict_of_nav_buttons_blocks = {}
        for div in range(len(course_page.list_of_buttons_in_navigation())):
            if div == 0:
                try:
                    dict_of_nav_buttons_blocks["אודות המסלול"] = course_page.about_block()
                except NoSuchElementException:
                    self.string_message("!------The button 'אודות המסלול' does not work------!\n")
                    continue
            if div == 1:
                try:
                    dict_of_nav_buttons_blocks["נושאים"] = course_page.course_topics_block()
                except NoSuchElementException:
                    self.string_message("!------The button 'נושאים' does not work------!\n")
                    continue
            if div == 2:
                try:
                    dict_of_nav_buttons_blocks["קהל יעד ודרישות קדם"] = course_page.target_audience_block()
                except NoSuchElementException:
                    self.string_message("!------The button 'קהל יעד ודרישות קדם' does not work------!\n")
                    continue
            if div == 3:
                try:
                    dict_of_nav_buttons_blocks["קורסי המשך"] = course_page.follow_up_courses_block()
                except NoSuchElementException:
                    self.string_message("!------The button 'קורסי המשך' does not work------!\n")
                    continue
            if div == 4:
                try:
                    dict_of_nav_buttons_blocks["חוות דעת סטודנטים"] = course_page.videos_block()
                except NoSuchElementException:
                    self.string_message("!------The button 'חוות דעת סטודנטים' does not work------!\n")
                    continue
            if div == 5:
                try:
                    dict_of_nav_buttons_blocks["מאמרים"] = course_page.articles_block()
                except NoSuchElementException:
                    self.string_message("!------The button 'מאמרים' does not work------!\n")
                    continue
        return dict_of_nav_buttons_blocks

    # Checks each of the navigation buttons if they lead to the correct 'div' block
    def checks_navigation_buttons(self, actions, btn, dict_of_nav_buttons_blocks, index):
        index_of_btn = 0
        try:
            btn_id_split = btn.get_attribute("href").split("#")  # Separates the href link of the nav button
            btn_id = str(btn_id_split[-1])  # Takes the 'id' from the end of the list and converts to string
            actions.move_to_element(btn).click().perform()  # Click on the nav button according to the loop iteration
            block = list(dict_of_nav_buttons_blocks.values())[index]  # Value of dictionary
            block_key = list(dict_of_nav_buttons_blocks.keys())[index]  # Key of dictionary
            block_id = block.get_attribute("id")  # 'id' of the current block
            self.string_message(
                f"---Comparing Between The '{btn.text}' Nav Button And The '{block_key}' Div Block---\n")
            if btn_id == block_id:
                self.string_message("---Element Matches---\n")
        except ElementNotVisibleException:
            self.string_message("!------Element Not Found------!\n")
        except IndexError:
            print("Out of bounds")

    # Confirm which nav buttons does not works, and clicks the one that works and confirm if its the same id with the nav button's href
    def confirm_which_nav_buttons_works(self, actions, course_page, index_of_btn):
        div_blocks = self.prepares_dictionary_of_div_block(course_page)
        for btn in course_page.list_of_buttons_in_navigation():
            if index_of_btn == len(div_blocks):
                break
            if btn.text == list(div_blocks.keys())[index_of_btn]:
                self.checks_navigation_buttons(actions, btn, div_blocks, index_of_btn)
                index_of_btn += 1
        return index_of_btn

    # Fills the form under the syllabus
    def form_under_syllabus(self, last_name="test", first_name="test", ending_of_mail="@test.com", phone_number="",
                            choose_maslul="yes", tick_terms_and_services="yes", send_button="yes", close_button="yes"):
        self.string_message("@Inside 'Form under Syllabus' function\n")
        now = datetime.now()
        current_time = now.strftime("%d%m%H%M%S")
        course_page = CoursePage(self.driver)
        self.string_message("---Entering last name---\n")
        course_page.last_name_field_in_form_under_syllabus().send_keys(last_name)
        self.string_message("---Entering first name---\n")
        course_page.first_name_field_in_form_under_syllabus().send_keys(first_name)
        self.string_message("---Entering mail---\n")
        course_page.email_field_in_form_under_syllabus().send_keys(current_time + ending_of_mail)
        if phone_number == "":
            phone_number = current_time
        self.string_message("---Entering phone number---\n")
        course_page.phone_field_in_form_under_syllabus().send_keys(phone_number)
        if choose_maslul == "yes":
            self.string_message("---Choosing maslul---\n")
            course_page.choose_maslul_field_in_form_under_syllabus().click()
            course_page.choose_maslul_real_time_field_in_form_under_syllabus().click()
        if tick_terms_and_services == "yes":
            self.string_message("---Ticking the terms of agreement and services---\n")
            course_page.agreement_of_terms_and_services_field_in_form_under_syllabus().click()
        if send_button == "yes":
            self.string_message("---Clicking on the 'send' button---\n")
            course_page.send_button_in_form_under_syllabus().click()
        if close_button == "yes":
            self.string_message("---Clicking on the close button---\n")
            course_page.close_button_after_filling_details_in_form_under_syllabus().click()
        self.string_message("@Outside 'Form under Syllabus' function\n")

    # Checks if the salary div block is presented, and if there is content there
    def checks_if_salary_block_presented(self, course_page):
        try:
            if course_page.salary_block().is_displayed():
                self.string_message("---Salary Block is Presented---\n")
                if course_page.table_list_of_salary_block():
                    self.string_message("---There is content in Salary block---\n")
                else:
                    self.string_message("!------No content in Salary Block------!\n")
        except NoSuchElementException:
            self.string_message("!------Salary Block is not Presented------!\n")

    # Checks if the faq div block is presented, and clicks on each question
    def checks_if_faq_block_presented(self, actions, course_page):
        try:
            if course_page.faq_block().is_displayed():
                self.string_message("---FAQ Block is Presented---\n")
                for question in course_page.list_of_div_blocks_in_faq():
                    self.string_message(f"---Clicked on question -> {question.text}---\n")
                    actions.move_to_element(question).click().perform()
        except NoSuchElementException:
            self.string_message("!------FAQ Block is not Presented------!\n")

    # ----------------------------------------------COURSE'S METHODS-----------------------------------------------------
    def course_real_time(self):
        self.string_message("@Inside Course 'Real Time' function\n")
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        run = True
        dict_of_urls = {
            "RT Concepts (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/RT/RT%D6%B9_Concepts_FreeRTOS.pdf",
            "(EN) שפת C": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/RT/C_for_embedded.pdf",
            "Linux Kernel And Device Drivers (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/RT/Linux_Kernel_yocto.pdf",
            "ARM - Embedded Systems (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/RT/Embedded_Systems.pdf",
            "Internet Of Things": "NO SYLLABUS FOR NOW",
            "FreeRTOS": "NO SYLLABUS FOR NOW",
            "(EN) שפת ++C": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/RT/CPP_for_RT_Embedded_Systems.pdf",
            "Yocto Programming": "NO SYLLABUS FOR NOW",
            "Embedded Linux (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/RT/Linux%D6%B9%D6%B9_System_Programming.pdf"}
        keys_of_dict_of_urls = dict_of_urls.keys()
        while run:
            for key in keys_of_dict_of_urls:
                header.courses_tab().click()
                header.course_real_time().click()
                index_of_btn = 0
                if index == 0:
                    header.sub_course_rt_concepts().click()
                    self.string_message("@@Inside Sub Course 'RT Concepts'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 1:
                    header.sub_course_c_language().click()
                    self.string_message("@@Inside Sub Course 'C'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 2:
                    header.sub_course_linux_kernel_and_device_drivers().click()
                    self.string_message("@@Inside Sub Course 'Linux Kernel and Device Drivers'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 3:
                    header.sub_course_arm_embedded_systems().click()
                    self.string_message(
                        "@@Inside Sub Course 'ARM Embedded Systems'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 4:
                    header.sub_course_internet_of_things().click()
                    self.string_message(
                        "@@Inside Sub Course 'Internet of Things'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 5:
                    header.sub_course_free_rtos().click()
                    self.string_message(
                        "@@Inside Sub Course 'Free RTOS'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 6:
                    header.sub_course_c_plus_plus_language().click()
                    self.string_message(
                        "@@Inside Sub Course 'C++'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 7:
                    header.sub_course_yocto_programming().click()
                    self.string_message(
                        "@@Inside Sub Course 'Yocto Programming'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 8:
                    header.sub_course_linux_embedded().click()
                    self.string_message(
                        "@@Inside Sub Course 'Linux Embedded'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                index += 1
            run = False

        self.string_message("@Outside Course 'Real Time' function\n")

    def course_web_development(self):
        self.string_message("@Inside Course 'Web Development' function\n")
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        run = True
        dict_of_urls = {
            "Web Foundations (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/FS/webfoundation.pdf",
            "(EN) AngularJS | אנגולר": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/FS/Angular.pdf",
            "(EN) פייתון |  Python": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Shared/Python.pdf",
            "CSS3 (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/FS/css.pdf",
            "NodeJS (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/FS/NodeJS.pdf",
            "Javascript (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/FS/javascript.pdf",
            "TypeScript": "NO SYLLABUS FOR NOW",
            "MongoDB (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/FS/MongoDB.pdf",
            "HTML5 (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/FS/html.pdf",
            "React |  ריאקט (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/FS/React.pdf",
            "Java (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Shared/Java.pdf",
            "Bootstrap (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/FS/bootstrap.pdf",
            "פיתוח אפליקציות לאנדרואיד": "NO SYLLABUS FOR NOW",
            "GIT (Version Control) (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Shared/Git.pdf",
            "SQL (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Shared/SQL.pdf"}

        keys_of_dict_of_urls = dict_of_urls.keys()

        while run:
            for key in keys_of_dict_of_urls:
                header.courses_tab().click()
                header.course_web_development().click()
                index_of_btn = 0
                if index == 0:
                    header.sub_course_web_foundations().click()
                    self.string_message("@@Inside Sub Course 'Web Foundations'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 1:
                    header.sub_course_angular_js().click()
                    self.string_message("@@Inside Sub Course 'AngularJS'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 2:
                    header.sub_course_python_language().click()
                    self.string_message("@@Inside Sub Course 'Python'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 3:
                    header.sub_course_css_language().click()
                    self.string_message("@@Inside Sub Course 'CSS3'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 4:
                    header.sub_course_node_js().click()
                    self.string_message("@@Inside Sub Course 'NodeJS'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 5:
                    header.sub_course_javascript_language().click()
                    self.string_message("@@Inside Sub Course 'JavaScript'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 6:
                    header.sub_course_typescript_language().click()
                    self.string_message("@@Inside Sub Course 'TypeScript'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 7:
                    header.sub_course_mongodb().click()
                    self.string_message("@@Inside Sub Course 'MongoDB'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 8:
                    header.sub_course_html5().click()
                    self.string_message("@@Inside Sub Course 'HTML5'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 9:
                    header.sub_course_react().click()
                    self.string_message("@@Inside Sub Course 'React'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 10:
                    header.sub_course_java_language().click()
                    self.string_message("@@Inside Sub Course 'Java'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 11:
                    header.sub_course_bootstrap().click()
                    self.string_message("@@\Inside Sub Course 'BootStrap'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 12:
                    header.sub_course_app_development_for_android().click()
                    self.string_message("@@Inside Sub Course 'App Development for Android'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 13:
                    header.sub_course_git().click()
                    self.string_message(
                        "@@Inside Sub Course 'GIT Source Control'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                elif index == 14:
                    header.sub_course_sql().click()
                    self.string_message(
                        "@@Inside Sub Course 'SQL'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                index += 1
            run = False

        self.string_message("@Outside Course 'Web Development' function\n")

    def course_cyber(self):
        self.string_message("@Inside Course 'Cyber' function\n")
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        run = True
        dict_of_urls = {
            "הכנה לבחינת הסמכה C | EH": "NO SYLLABUS FOR NOW",
            "Cyber Attack Infrastructure (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Cyber/Cyber_Attack_Infrastructure.pdf",
            "Malware Analysis (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Cyber/Malware_Analysis.pdf",
            "Penetration Testing (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Cyber/Penetrating_Testing.pdf",
            "Linux Fundamentals": "NO SYLLABUS FOR NOW",
            "Cyber Security Fundamentals": "NO SYLLABUS FOR NOW",
            "Networking (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Shared/Practical_Networking.pdf",
            "Forensics Investigation & Incident Response": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Cyber/Forensics_Investigation_Incident_Response.pdf"}

        keys_of_dict_of_urls = dict_of_urls.keys()

        while run:
            for key in keys_of_dict_of_urls:
                header.courses_tab().click()
                header.course_cyber_security().click()
                index_of_btn = 0
                if index == 0:
                    header.sub_course_preparations_for_certification_exam().click()
                    self.string_message(
                        "@@Inside Sub Course 'Preparations for Certification Exam'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 1:
                    header.sub_course_cyber_attack_infrastructure().click()
                    self.string_message(
                        "@@Inside Sub Course 'Cyber Attack Infrastructure'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 2:
                    header.sub_course_malware_analysis().click()
                    self.string_message(
                        "@@Inside Sub Course 'Malware Analysis'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 3:
                    header.sub_course_penetration_testing().click()
                    self.string_message(
                        "@@Inside Sub Course 'Penetration Testing'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 4:
                    header.sub_course_linux_fundamentals().click()
                    self.string_message(
                        "@@Inside Sub Course 'Linux Fundamentals'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 5:
                    header.sub_course_cyber_security_fundamentals().click()
                    self.string_message(
                        "@@Inside Sub Course 'Cyber Security Fundamentals'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 6:
                    header.sub_course_networking().click()
                    self.string_message(
                        "@@Inside Sub Course 'Networking'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 7:
                    header.sub_course_forensics_investigation_and_incident_response().click()
                    self.string_message(
                        "@@Inside Sub Course 'Forensics Investigation and Incident Report'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                index += 1
            run = False

        self.string_message("@Outside Course 'Cyber' function\n")

    def course_devops(self):
        self.string_message("@Inside Course 'DevOps' function\n")
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        run = True
        dict_of_urls = {
            "Docker (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Devops/Docker.pdf",
            "(EN) לינוקס | Linux Admin": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Shared/Linux_Fundamentals.pdf",
            "Kubernetes (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Devops/Kubernetes.pdf",
            "(EN) פייתון |  Python": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Shared/Python.pdf",
            "Zabbix (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Devops/Zabbix.pdf",
            "Terraform (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Devops/Terraform.pdf",
            "Networking (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Shared/Practical_Networking.pdf",
            "ANSIBLE (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Devops/Ansible.pdf",
            "Bash Scripting": "NO SYLLABUS FOR NOW",
            "AWS (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Devops/aws.pdf",
            "Jenkins (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Devops/Jenkins.pdf"}

        keys_of_dict_of_urls = dict_of_urls.keys()

        while run:
            for key in keys_of_dict_of_urls:
                header.courses_tab().click()
                header.course_devops().click()
                index_of_btn = 0
                if index == 0:
                    header.sub_course_docker().click()
                    self.string_message(
                        "@@Inside Sub Course 'Docker'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 1:
                    header.sub_course_linux_admin().click()
                    self.string_message(
                        "@@Inside Sub Course 'Linux Admin'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 2:
                    header.sub_course_kubernetes().click()
                    self.string_message(
                        "@@Inside Sub Course 'Kubernetes'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 3:
                    header.sub_course_python_language().click()
                    self.string_message(
                        "@@Inside Sub Course 'Python'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 4:
                    header.sub_course_zabbix().click()
                    self.string_message(
                        "@@Inside Sub Course 'Zabbix'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 5:
                    header.sub_course_terraform().click()
                    self.string_message(
                        "@@Inside Sub Course 'Terraform'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 6:
                    header.sub_course_networking().click()
                    self.string_message(
                        "@@Inside Sub Course 'Networking'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 7:
                    header.sub_course_ansible().click()
                    self.string_message(
                        "@@Inside Sub Course 'Ansible'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 8:
                    header.sub_course_bash_scripting().click()
                    self.string_message(
                        "@@Inside Sub Course 'Bash Scripting'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 9:
                    header.sub_course_aws().click()
                    self.string_message(
                        "@@Inside Sub Course 'AWS'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 10:
                    header.sub_course_jenkins().click()
                    self.string_message(
                        "@@Inside Sub Course 'Jenkins'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                index += 1
            run = False

        self.string_message("@Outside Course DevOps function\n")

    def course_data_science(self):
        self.string_message("@Inside Course 'Data Science' function\n")
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        run = True
        dict_of_urls = {
            "Machine Learning Fundamentals (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/ML/ML_Fundamentals.pdf",
            "Machine Learning With Python (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/ML/ML_with_Python.pdf",
            "Deep Learning With Tensorflow (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/ML/Deep_Learning_with_Tensorflow.pdf"}

        keys_of_dict_of_urls = dict_of_urls.keys()

        while run:
            for key in keys_of_dict_of_urls:
                header.courses_tab().click()
                header.course_data_science().click()
                index_of_btn = 0
                if index == 0:
                    header.sub_course_machine_learning_fundamentals().click()
                    self.string_message(
                        "@@Inside Sub Course 'Machine Learning Fundamentals'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 1:
                    header.sub_course_machine_learning_with_python().click()
                    self.string_message(
                        "@@Inside Sub Course 'Machine Learning with Python'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 2:
                    header.sub_course_deep_learning_with_tensorflow().click()
                    self.string_message(
                        "@@Inside Sub Course 'Deep Learning with TensorFlow'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                index += 1
            run = False

        self.string_message("@Outside Course 'Data Science' function\n")

    def course_software_testing(self):
        self.string_message("@Inside Course 'Software Testing' function\n")
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        run = True
        dict_of_urls = {
            "Selenium (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/QA/Selenium_Webdriver.pdf",
            "LabView": "NO SYLLABUS FOR NOW",
            "JIRA | ג'ירה": "NO SYLLABUS FOR NOW",
            "מתודולוגיות QA": "NO SYLLABUS FOR NOW",
            "Java (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Shared/Java.pdf"}

        keys_of_dict_of_urls = dict_of_urls.keys()

        while run:
            for key in keys_of_dict_of_urls:
                header.courses_tab().click()
                header.course_software_testing().click()
                index_of_btn = 0
                if index == 0:
                    header.sub_course_selenium().click()
                    self.string_message(
                        "@@Inside Sub Course 'Selenium'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 1:
                    header.sub_course_labview().click()
                    self.string_message(
                        "@@Inside Sub Course 'LabView'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 2:
                    header.sub_course_jira().click()
                    self.string_message(
                        "@@Inside Sub Course 'Jira'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 3:
                    header.sub_course_qa_methodologies().click()
                    self.string_message(
                        "@@Inside Sub Course 'QA Methodologies'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 4:
                    header.sub_course_java_language().click()
                    self.string_message(
                        "@@Inside Sub Course 'Java'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                index += 1
            run = False

        self.string_message("@Outside Course 'Software Testing' function\n")

    def course_network_and_sysadmin(self):
        self.string_message("@Inside Course 'Network and Sysadmin' function\n")
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        run = True
        dict_of_urls = {
            "(EN) לינוקס | Linux Admin": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Shared/Linux_Fundamentals.pdf",
            "LPIC-2": "NO SYLLABUS FOR NOW",
            "Linux Fundamentals": "NO SYLLABUS FOR NOW",
            "LPIC-1": "NO SYLLABUS FOR NOW",
            "Networking (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Shared/Practical_Networking.pdf"}

        keys_of_dict_of_urls = dict_of_urls.keys()

        while run:
            for key in keys_of_dict_of_urls:
                header.courses_tab().click()
                header.course_network_and_sysadmin().click()
                index_of_btn = 0
                if index == 0:
                    header.sub_course_linux_admin().click()
                    self.string_message(
                        "@@Inside Sub Course 'Linux Admin'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 1:
                    header.sub_course_lpic_2().click()
                    self.string_message(
                        "@@Inside Sub Course 'LPIC-2'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 2:
                    header.sub_course_linux_fundamentals().click()
                    self.string_message(
                        "@@Inside Sub Course 'Linux Fundamentals'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 3:
                    header.sub_course_lpic_1().click()
                    self.string_message(
                        "@@Inside Sub Course 'LPIC-1'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 4:
                    header.sub_course_networking().click()
                    self.string_message(
                        "@@Inside Sub Course 'Networking'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                index += 1
            run = False

        self.string_message("@Outside Course 'Network and Sysadmin' function---\n")

    def course_programming_language(self):
        self.string_message("@Inside Course 'Programming Languages' function\n")
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        run = True
        dict_of_urls = {
            "Java (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Shared/Java.pdf",
            "(EN) שפת C": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/RT/C_for_embedded.pdf",
            "Javascript (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/FS/javascript.pdf",
            "(EN) פייתון |  Python": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Shared/Python.pdf",
            "(EN) שפת ++C": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/RT/CPP_for_RT_Embedded_Systems.pdf"}

        keys_of_dict_of_urls = dict_of_urls.keys()

        while run:
            for key in keys_of_dict_of_urls:
                header.courses_tab().click()
                header.course_programming_language().click()
                index_of_btn = 0
                if index == 0:
                    header.sub_course_java_language().click()
                    self.string_message(
                        "@@Inside Sub Course 'Java'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 1:
                    header.sub_course_c_language().click()
                    self.string_message(
                        "@@Inside Sub Course 'C'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 2:
                    header.sub_course_javascript_language().click()
                    self.string_message(
                        "@@Inside Sub Course 'JavaScript'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 3:
                    header.sub_course_python_language().click()
                    self.string_message(
                        "@@Inside Sub Course 'Python'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 4:
                    header.sub_course_c_plus_plus_language().click()
                    self.string_message(
                        "@@Inside Sub Course 'C++'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                index += 1
            run = False

        self.string_message("@Outside Course 'Programming Languages' function\n")

    def course_cloud_composing(self):
        self.string_message("@Inside Course 'Cloud Composing' function\n")
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        run = True
        dict_of_urls = {
            "AWS (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Devops/aws.pdf",
            "Microsoft Azure": "NO SYLLABUS FOR NOW"}

        keys_of_dict_of_urls = dict_of_urls.keys()

        while run:
            for key in keys_of_dict_of_urls:
                header.courses_tab().click()
                header.course_cloud_computing().click()
                index_of_btn = 0
                if index == 0:
                    header.sub_course_aws().click()
                    self.string_message(
                        "@@Inside Sub Course 'AWS'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 1:
                    header.sub_course_microsoft_azure().click()
                    self.string_message(
                        "@@Inside Sub Course 'Microsoft Azure'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()

                index += 1
            run = False

        self.string_message("@Outside Course 'Cloud Composing' function\n")

    def course_image_processing(self):
        self.string_message("@Inside Course 'Image Processing' function\n")
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        run = True
        dict_of_urls = {
            "Machine Learning Fundamentals (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/ML/ML_Fundamentals.pdf",
            "OpenCV": "NO SYLLABUS FOR NOW",
            "CUDA": "NO SYLLABUS FOR NOW",
            "Machine Learning With Python (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/ML/ML_with_Python.pdf",
            "Deep Learning With Tensorflow (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/ML/Deep_Learning_with_Tensorflow.pdf",
            "Nvidia GPUs": "NO SYLLABUS FOR NOW"}

        keys_of_dict_of_urls = dict_of_urls.keys()

        while run:
            for key in keys_of_dict_of_urls:
                header.courses_tab().click()
                header.course_image_processing().click()
                index_of_btn = 0
                if index == 0:
                    header.sub_course_machine_learning_fundamentals().click()
                    self.string_message(
                        "@@Inside Sub Course 'Machine Learning Fundamentals'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 1:
                    header.sub_course_open_cv().click()
                    self.string_message(
                        "@@Inside Sub Course 'OpenCV'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 2:
                    header.sub_course_cuda().click()
                    self.string_message(
                        "@@Inside Sub Course 'CUDA'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 3:
                    header.sub_course_machine_learning_with_python().click()
                    self.string_message(
                        "@@Inside Sub Course 'Machine Learning with Python'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 4:
                    header.sub_course_deep_learning_with_tensorflow().click()
                    self.string_message(
                        "@@Inside Sub Course 'Deep Learning with TensorFlow'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 5:
                    header.sub_course_nvidia_gpus().click()
                    self.string_message(
                        "@@Inside Sub Course 'Nvidia GPUs'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                index += 1
            run = False

        self.string_message("@Outside Course 'Image Processing' function\n")

    def course_database_management(self):
        self.string_message("@Inside Course 'Database Management' function\n")
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
        actions = ActionChains(self.driver)
        index = 0
        run = True
        dict_of_urls = {
            "SQL (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/Shared/SQL.pdf",
            "MongoDB (EN)": "https://rt-ed.co.il/wp-content/uploads/syllabus/Courses/FS/MongoDB.pdf"}

        keys_of_dict_of_urls = dict_of_urls.keys()

        while run:
            for key in keys_of_dict_of_urls:
                header.courses_tab().click()
                header.course_database_management().click()
                index_of_btn = 0
                if index == 0:
                    header.sub_course_sql().click()
                    self.string_message(
                        "@@Inside Sub Course 'SQL'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()
                if index == 1:
                    header.sub_course_mongodb().click()
                    self.string_message(
                        "@@Inside Sub Course 'MongoDB'---\n")
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                    index_of_btn = self.confirm_which_nav_buttons_works(actions, course_page, index_of_btn)
                    self.checks_if_salary_block_presented(course_page)
                    self.checks_if_faq_block_presented(actions, course_page)
                    # self.form_under_syllabus()

                index += 1
            run = False

        self.string_message("@Outside Course 'Database Management' function\n")
        self.driver.quit()
    # ----------------------------------------------------TEST----------------------------------------------------

    def test_run_courses(self):
        self.course_real_time()
        self.course_web_development()
        self.course_cyber()
        self.course_devops()
        self.course_data_science()
        self.course_software_testing()
        self.course_network_and_sysadmin()
        self.course_programming_language()
        self.course_cloud_composing()
        self.course_image_processing()
        self.course_database_management()
        self.open_file_and_append_string_message()
