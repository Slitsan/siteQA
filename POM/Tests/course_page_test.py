#   13/03/2022
#   Created By Pablik
#   Courses Page Syllabus Test
# -----------------------------------------------------

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from datetime import datetime
from POM.Pages.course_page import CoursePage
# -----------------------------------------------------
from POM.Pages.header import Header


class CoursePageTest(unittest.TestCase):
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
        cls.string_result = "-----------------------------------TESTING COURSE'S SYLLABUS-----------------------------------------------\n"

    # Compares the syllabus url with a given url inside the 'maslul functions'
    def compare_syllabus_url(self, title: str, actual_page_title: str, button_name: str):
        actual_title_of_page = actual_page_title
        print(f"---Checking The {button_name} Syllabus...---")
        self.string_result += f"---Checking The {button_name} Syllabus...---\n"
        if title == actual_title_of_page:
            print("---The syllabus is correct---")
            self.string_result += "---The syllabus is correct---\n"
            return True
        else:
            print("---Not the right syllabus---")
            self.string_result += "---Not the right syllabus---\n"
            return False

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

    # ----------------------------------------------COURSE'S METHODS-----------------------------------------------------
    def course_real_time(self):
        print("---Inside course_real_time function---")
        self.string_result += "---Inside course_real_time function---\n"
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
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
                if index == 0:
                    header.sub_course_rt_concepts().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                elif index == 1:
                    header.sub_course_c_language().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                elif index == 2:
                    header.sub_course_linux_kernel_and_device_drivers().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                elif index == 3:
                    header.sub_course_arm_embedded_systems().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                elif index == 4:
                    header.sub_course_internet_of_things().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                elif index == 5:
                    header.sub_course_free_rtos().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                elif index == 6:
                    header.sub_course_c_plus_plus_language().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                elif index == 7:
                    header.sub_course_yocto_programming().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                elif index == 8:
                    header.sub_course_linux_embedded().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                index += 1
            run = False

        print("---Outside course_real_time function---")
        self.string_result += "---Outside course_real_time function---\n"

    def course_web_development(self):
        print("---Inside course_web_development function---")
        self.string_result += "---Inside course_web_development function---\n"
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
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
                if index == 0:
                    header.sub_course_web_foundations().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 1:
                    header.sub_course_angular_js().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 2:
                    header.sub_course_python_language().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 3:
                    header.sub_course_css_language().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 4:
                    header.sub_course_node_js().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 5:
                    header.sub_course_javascript_language().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 6:
                    header.sub_course_typescript_language().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 7:
                    header.sub_course_mongodb().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 8:
                    header.sub_course_html5().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 9:
                    header.sub_course_react().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 10:
                    header.sub_course_java_language().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 11:
                    header.sub_course_bootstrap().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 12:
                    header.sub_course_app_development_for_android().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 13:
                    header.sub_course_git().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 14:
                    header.sub_course_sql().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                index += 1
            run = False

        print("---Outside course_web_development function---")
        self.string_result += "---Outside course_web_development function---\n"

    def course_cyber(self):
        print("---Inside course_cyber function---")
        self.string_result += "---Inside course_cyber function---\n"
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
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
                if index == 0:
                    header.sub_course_preparations_for_certification_exam().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 1:
                    header.sub_course_cyber_attack_infrastructure().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 2:
                    header.sub_course_malware_analysis().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 3:
                    header.sub_course_penetration_testing().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 4:
                    header.sub_course_linux_fundamentals().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 5:
                    header.sub_course_cyber_security_fundamentals().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 6:
                    header.sub_course_networking().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 7:
                    header.sub_course_forensics_investigation_and_incident_response().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                index += 1
            run = False

        print("---Outside course_cyber function---")
        self.string_result += "---Outside course_cyber function---\n"

    def course_devops(self):
        print("---Inside course_devops function---")
        self.string_result += "---Inside course_devops function---\n"
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
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
                if index == 0:
                    header.sub_course_docker().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 1:
                    header.sub_course_linux_admin().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 2:
                    header.sub_course_kubernetes().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 3:
                    header.sub_course_python_language().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 4:
                    header.sub_course_zabbix().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 5:
                    header.sub_course_terraform().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 6:
                    header.sub_course_networking().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 7:
                    header.sub_course_ansible().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 8:
                    header.sub_course_bash_scripting().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 9:
                    header.sub_course_aws().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 10:
                    header.sub_course_jenkins().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                index += 1
            run = False

        print("---Outside course_devops function---")
        self.string_result += "---Outside course_devops function---\n"

    def course_data_science(self):
        print("---Inside course_data_science function---")
        self.string_result += "---Inside course_data_science function---\n"
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
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
                if index == 0:
                    header.sub_course_machine_learning_fundamentals().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 1:
                    header.sub_course_machine_learning_with_python().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 2:
                    header.sub_course_deep_learning_with_tensorflow().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)

                index += 1
            run = False

        print("---Outside course_data_science function---")
        self.string_result += "---Outside course_data_science function---\n"

    def course_software_testing(self):
        print("---Inside course_software_testing function---")
        self.string_result += "---Inside course_software_testing function---\n"
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
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
                if index == 0:
                    header.sub_course_selenium().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 1:
                    header.sub_course_labview().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 2:
                    header.sub_course_jira().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 3:
                    header.sub_course_qa_methodologies().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 4:
                    header.sub_course_java_language().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                index += 1
            run = False

        print("---Outside course_software_testing function---")
        self.string_result += "---Outside course_software_testing function---\n"

    def course_network_and_sysadmin(self):
        print("---Inside course_network_and_sysadmin function---")
        self.string_result += "---Inside course_network_and_sysadmin function---\n"
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
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
                if index == 0:
                    header.sub_course_linux_admin().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 1:
                    header.sub_course_lpic_2().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 2:
                    header.sub_course_linux_fundamentals().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 3:
                    header.sub_course_lpic_1().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 4:
                    header.sub_course_networking().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                index += 1
            run = False

        print("---Outside course_network_and_sysadmin function---")
        self.string_result += "---Outside course_network_and_sysadmin function---\n"

    def course_programming_language(self):
        print("---Inside course_programming_language function---")
        self.string_result += "---Inside course_programming_language function---\n"
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
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
                if index == 0:
                    header.sub_course_java_language().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 1:
                    header.sub_course_c_language().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 2:
                    header.sub_course_javascript_language().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 3:
                    header.sub_course_python_language().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 4:
                    header.sub_course_c_plus_plus_language().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                index += 1
            run = False

        print("---Outside course_programming_language function---")
        self.string_result += "---Outside course_programming_language function---\n"

    def course_cloud_composing(self):
        print("---Inside course_cloud_composing function---")
        self.string_result += "---Inside course_cloud_composing function---\n"
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
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
                if index == 0:
                    header.sub_course_aws().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 1:
                    header.sub_course_microsoft_azure().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)

                index += 1
            run = False

        print("---Outside course_cloud_composing function---")
        self.string_result += "---Outside course_cloud_composing function---\n"

    def course_image_processing(self):
        print("---Inside course_image_processing function---")
        self.string_result += "---Inside course_image_processing function---\n"
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
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
                if index == 0:
                    header.sub_course_machine_learning_fundamentals().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 1:
                    header.sub_course_open_cv().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 2:
                    header.sub_course_cuda().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 3:
                    header.sub_course_machine_learning_with_python().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 4:
                    header.sub_course_deep_learning_with_tensorflow().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 5:
                    header.sub_course_nvidia_gpus().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                index += 1
            run = False

        print("---Outside course_image_processing function---")
        self.string_result += "---Outside course_image_processing function---\n"

    def course_database_management(self):
        print("---Inside course_database_management function---")
        self.string_result += "---Inside course_database_management function---\n"
        header = Header(self.driver)
        course_page = CoursePage(self.driver)
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
                if index == 0:
                    header.sub_course_sql().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)
                if index == 1:
                    header.sub_course_mongodb().click()
                    course_page.download_syllabus().click()
                    self.switching_tabs_and_comparing_urls(dict_of_urls, index, key)

                index += 1
            run = False

        print("---Outside course_database_management function---")
        self.string_result += "---Outside course_database_management function---\n"

    def test_run_maslulim(self):
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
        try:
            file = open(f"../../Source/log {self.date_for_log}.txt", "a+")
            file.write(self.string_result)
            file.close()
        except FileNotFoundError:
            print("Did not found a file")
