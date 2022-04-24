import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.relative_locator import locate_with


class Header:

    def __init__(self, drive: WebDriver):
        self.driver = drive
        self.list_of_five_buttons = None

        self.popUp_close_xpath = '//*[@id="lead-form-modal1"]/span'
        self.studentPortal_id = 'student-portal'
        self.search_textbox_id = 'nav-search-string'
        self.search_btn_class = 'btn btn-outline-light order-2 my-2 my-sm-0 col-3'

        self.maslulim_by_xpath = "//*[@id='primar-menu']/li[@class='nav-item dropdown ml-2'][2]"
        self.courses_by_xpath = "//*[@id='primar-menu']/li[@class='nav-item dropdown ml-2'][1]"
        self.courses_for_companies_by_txt = "קורסים לחברות"
        self.articles_by_txt = "מאמרים"
        self.about_us_by_txt = "אודות"
        self.declaration_of_accessibility_by_txt = "הצהרת נגישות"
        self.jobs_by_txt = "דרושים"
        # ----------------------- MASLULIM --------------------------
        self.maslulim_categories_by_xpath = '//*[@id="primar-menu"]/li[8]/ul/li'
        self.maslul_real_time_by_xpath = "//*[@id=\"RT\"]"
        self.maslul_real_time_courses_by_xpath = "//*[@id=\"RT\"]/ul/li"
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
        self.real_time_course_by_xpath = "//*[@id=\"Real time\"]"
        self.real_time_sub_courses_by_xpath = "//*[@id=\"Real time\"]/ul/li"
        self.course_web_development_by_xpath = "//*[@id=\"Web Development\"]/a"
        self.web_development_sub_courses_by_xpath = "//*[@id=\"Web Development\"]/ul/li"
        self.course_cyber_security_by_xpath = "//*[@id=\"Cyber security\"]/a"
        self.cyber_security_sub_courses_by_xpath = "//*[@id=\"Cyber security\"]/ul/li"
        self.course_devops_by_xpath = "//*[@id='Cyber security'] /following-sibling::li[1]"
        self.devops_sub_courses_by_xpath = "//*[@id='Cyber security'] /following-sibling::li[1]/ul/li"
        self.course_data_science_by_xpath = "//*[@id=\"Data science\"]/a"
        self.data_science_courses_by_xpath = "//*[@id=\"Data science\"]/ul/li"
        self.course_software_testing_by_xpath = "//*[@id=\"Software testing\"]/a"
        self.software_testing_courses_by_xpath = "//*[@id=\"Software testing\"]/ul/li"
        self.course_network_and_sysadmin_by_xpath = "//*[@id=\"Network and sysadmin\"]/a"
        self.network_and_sysadmin_courses_by_xpath = "//*[@id=\"Network and sysadmin\"]/ul/li"
        self.course_programming_language_by_xpath = "//*[@id=\"Programming languages\"]/a"
        self.programming_language_courses_by_xpath = "//*[@id=\"Programming languages\"]/ul/li"
        self.course_cloud_computing_by_xpath = "//*[@id=\"Cloud computing\"]/a"
        self.cloud_computing_courses_by_xpath = "//*[@id=\"Cloud computing\"]/ul/li"
        self.course_image_processing_by_xpath = "//*[@id=\"Image Processing\"]/a"
        self.image_processing_courses_by_xpath = "//*[@id=\"Image Processing\"]/ul/li"
        self.course_database_management_by_xpath = "//*[@id=\"Database management\"]/a"
        self.database_management_courses_by_xpath = "//*[@id=\"Database management\"]/ul/li"
        # ------------------------ SUB COURSES --------------------------
        self.sub_course_rt_concepts_by_txt = "RT Concepts"
        self.sub_course_c_language_by_txt = "שפת C"
        self.sub_course_linux_kernel_and_device_drivers_by_txt = "Linux Kernel And Device Drivers"
        self.sub_course_arm_embedded_systems_by_txt = "ARM - Embedded Systems"
        self.sub_course_internet_of_things_by_txt = "Internet Of Things"
        self.sub_course_free_rtos_by_txt = "FreeRTOS"
        self.sub_course_c_plus_plus_language_by_txt = "שפת ++C"
        self.sub_course_yocto_programming_by_txt = "Yocto Programming"
        self.sub_course_linux_embedded_by_txt = "Embedded Linux"
        self.sub_course_web_foundations_by_txt = "Web Foundations"
        self.sub_course_angular_js_by_txt = "AngularJS | אנגולר"
        self.sub_course_python_language_by_txt = "פייתון | Python"
        self.sub_course_css_language_by_txt = "CSS3"
        self.sub_course_node_js_by_txt = "NodeJS"
        self.sub_course_javascript_by_txt = "Javascript"
        self.sub_course_typescript_by_txt = "TypeScript"
        self.sub_course_mongodb_by_txt = "MongoDB"
        self.sub_course_html5_by_txt = "HTML5"
        self.sub_course_react_by_txt = "React | ריאקט"
        self.sub_course_java_language_by_txt = "Java"
        self.sub_course_bootstrap_by_txt = "Bootstrap"
        self.sub_course_app_development_for_android_by_txt = "פיתוח אפליקציות לאנדרואיד"
        self.sub_course_git_by_txt = "GIT (Version Control)"
        self.sub_course_sql_by_txt = "SQL"
        self.sub_course_preparations_for_certification_exam_by_txt = "הכנה לבחינת הסמכה C | EH"
        self.sub_course_cyber_attack_infrastructure_by_txt = "Cyber Attack Infrastructure"
        self.sub_course_malware_analysis_by_txt = "Malware Analysis"
        self.sub_course_penetration_testing_by_txt = "Penetration Testing"
        self.sub_course_linux_fundamentals_by_txt = "Linux Fundamentals"
        self.sub_course_cyber_security_fundamentals_by_txt = "Cyber Security Fundamentals"
        self.sub_course_networking_by_txt = "Networking"
        self.sub_course_forensics_investigation_and_incident_response_by_txt = "Forensics Investigation & Incident Response"
        self.sub_course_docker_by_txt = "Docker"
        self.sub_course_linux_admin_by_txt = "לינוקס | Linux Admin"
        self.sub_course_kubernetes_by_txt = "Kubernetes"
        self.sub_course_zabbix_by_txt = "Zabbix"
        self.sub_course_terraform_by_txt = "Terraform"
        self.sub_course_ansible_by_txt = "ANSIBLE"
        self.sub_course_bash_scripting_by_txt = "Bash Scripting"
        self.sub_course_aws_by_txt = "AWS"
        self.sub_course_jenkins_by_txt = "Jenkins"
        self.sub_course_machine_learning_fundamentals_by_txt = "Machine Learning Fundamentals"
        self.sub_course_machine_learning_with_python_by_txt = "Machine Learning With Python"
        self.sub_course_deep_learning_with_tensorflow_by_txt = "Deep Learning With Tensorflow"
        self.sub_course_selenium_by_txt = "Selenium"
        self.sub_course_labview_by_txt = "LabView"
        self.sub_course_jira_by_txt = "JIRA | ג'ירה"
        self.sub_course_qa_methodologies_by_txt = "מתודולוגיות QA"
        self.sub_course_lpic_1_by_txt = "LPIC-1"
        self.sub_course_lpic_2_by_txt = "LPIC-2"
        self.sub_course_microsoft_azure_by_txt = "Microsoft Azure"
        self.sub_course_open_cv_by_txt = "OpenCV"
        self.sub_course_cuda_by_txt = "CUDA"
        self.sub_course_nvidia_gpus_by_txt = "Nvidia GPUs"

    def get_title(self) -> str:
        return self.driver.title

    def maslul(self):
        return self.driver.find_element(By.XPATH, self.maslulim_by_xpath)

    # def goToMaslul(self, name):
    #     self.driver.find_element(By.XPATH, self.maslulim_by_xpath).click()

    def goToStudentPortal(self):
        self.driver.find_element(By.ID, self.studentPortal_id).click()
        return self.driver

    def courses_for_companies(self):
        return self.driver.find_element(By.LINK_TEXT, self.courses_for_companies_by_txt)

    def articles(self):
        return self.driver.find_element(By.LINK_TEXT, self.articles_by_txt)

    def about_us(self):
        return self.driver.find_element(By.LINK_TEXT, self.about_us_by_txt)

    def declaration_of_accessibility(self):
        return self.driver.find_element(By.LINK_TEXT, self.declaration_of_accessibility_by_txt)

    def jobs(self):
        return self.driver.find_element(By.LINK_TEXT, self.jobs_by_txt)

    # -------------------- Methods For Maslulim ----------------------------

    def list_of_maslulim_categories(self):
        return self.driver.find_elements(By.XPATH, self.maslulim_categories_by_xpath)

    def maslul_real_time(self):
        return self.driver.find_element(By.XPATH, self.maslul_real_time_by_xpath)

    def list_of_courses_on_real_time(self):
        return self.driver.find_elements(By.XPATH, self.maslul_real_time_courses_by_xpath)

    def maslul_full_stack(self):
        return self.driver.find_element(By.XPATH, self.maslul_full_stack_by_xpath)

    def list_of_courses_on_full_stack(self):
        return self.driver.find_elements(By.XPATH, self.full_stack_courses_by_xpath)

    def maslul_cyber(self):
        return self.driver.find_element(By.XPATH, self.maslul_cyber_by_xpath)

    def list_of_courses_on_cyber(self):
        return self.driver.find_elements(By.XPATH, self.cyber_courses_by_xpath)

    def maslul_machine_learning(self):
        return self.driver.find_element(By.XPATH, self.maslul_machine_learning_by_xpath)

    def list_of_courses_on_machine_learning(self):
        return self.driver.find_elements(By.XPATH, self.machine_learning_courses_by_xpath)

    def maslul_qa(self):
        return self.driver.find_element(By.XPATH, self.maslul_qa_by_xpath)

    def list_of_courses_on_qa(self):
        return self.driver.find_elements(By.XPATH, self.qa_courses_by_xpath)

    def maslul_dev_ops(self):
        return self.driver.find_element(By.XPATH, self.maslul_dev_ops_by_xpath)

    def list_of_courses_on_dev_ops(self):
        return self.driver.find_elements(By.XPATH, self.dev_ops_courses_by_xpath)

    def maslul_linux_servers(self):
        return self.driver.find_element(By.XPATH, self.maslul_linux_servers_by_xpath)

    def list_of_courses_on_linux_servers(self):
        return self.driver.find_elements(By.XPATH, self.linux_servers_courses_by_xpath)

    # ------------------------------- COURSES --------------------------------------

    def courses_tab(self):
        return self.driver.find_element(By.XPATH, self.courses_tab_by_xpath)

    def course_real_time(self):
        return self.driver.find_element(By.XPATH, self.real_time_course_by_xpath)

    def list_of_sub_courses_on_real_time_course(self):
        return self.driver.find_elements(By.XPATH, self.real_time_sub_courses_by_xpath)

    def course_web_development(self):
        return self.driver.find_element(By.XPATH, self.course_web_development_by_xpath)

    def list_of_sub_courses_on_web_development_course(self):
        return self.driver.find_elements(By.XPATH, self.web_development_sub_courses_by_xpath)

    def course_cyber_security(self):
        return self.driver.find_element(By.XPATH, self.course_cyber_security_by_xpath)

    def list_of_sub_courses_on_cyber_security_course(self):
        return self.driver.find_elements(By.XPATH, self.cyber_security_sub_courses_by_xpath)

    def course_devops(self):
        return self.driver.find_element(By.XPATH, self.course_devops_by_xpath)

    def list_of_sub_courses_on_devops_course(self):
        return self.driver.find_elements(By.XPATH, self.devops_sub_courses_by_xpath)

    def course_data_science(self):
        return self.driver.find_element(By.XPATH, self.course_data_science_by_xpath)

    def list_of_sub_courses_on_data_science_course(self):
        return self.driver.find_elements(By.XPATH, self.data_science_courses_by_xpath)

    def course_software_testing(self):
        return self.driver.find_element(By.XPATH, self.course_software_testing_by_xpath)

    def list_of_sub_courses_on_software_testing_course(self):
        return self.driver.find_elements(By.XPATH, self.software_testing_courses_by_xpath)

    def course_network_and_sysadmin(self):
        return self.driver.find_element(By.XPATH, self.course_network_and_sysadmin_by_xpath)

    def list_of_sub_courses_on_network_and_sysadmin_course(self):
        return self.driver.find_elements(By.XPATH, self.network_and_sysadmin_courses_by_xpath)

    def course_programming_language(self):
        return self.driver.find_element(By.XPATH, self.course_programming_language_by_xpath)

    def list_of_sub_courses_on_programming_language_course(self):
        return self.driver.find_elements(By.XPATH, self.programming_language_courses_by_xpath)

    def course_cloud_computing(self):
        return self.driver.find_element(By.XPATH, self.course_cloud_computing_by_xpath)

    def list_of_sub_courses_on_cloud_computing_course(self):
        return self.driver.find_elements(By.XPATH, self.cloud_computing_courses_by_xpath)

    def course_image_processing(self):
        return self.driver.find_element(By.XPATH, self.course_image_processing_by_xpath)

    def list_of_sub_courses_on_image_processing_course(self):
        return self.driver.find_elements(By.XPATH, self.image_processing_courses_by_xpath)

    def course_database_management(self):
        return self.driver.find_element(By.XPATH, self.course_database_management_by_xpath)

    def list_of_sub_courses_on_database_management_course(self):
        return self.driver.find_elements(By.XPATH, self.database_management_courses_by_xpath)

    # -------------------------------- SUB COURSES ----------------------------------------

    def sub_course_rt_concepts(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_rt_concepts_by_txt)

    def sub_course_c_language(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_c_language_by_txt)

    def sub_course_linux_kernel_and_device_drivers(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_linux_kernel_and_device_drivers_by_txt)

    def sub_course_arm_embedded_systems(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_arm_embedded_systems_by_txt)

    def sub_course_internet_of_things(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_internet_of_things_by_txt)

    def sub_course_free_rtos(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_free_rtos_by_txt)

    def sub_course_c_plus_plus_language(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_c_plus_plus_language_by_txt)

    def sub_course_yocto_programming(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_yocto_programming_by_txt)

    def sub_course_linux_embedded(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_linux_embedded_by_txt)

    def sub_course_web_foundations(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_web_foundations_by_txt)

    def sub_course_angular_js(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_angular_js_by_txt)

    def sub_course_python_language(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_python_language_by_txt)

    def sub_course_css_language(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_css_language_by_txt)

    def sub_course_node_js(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_node_js_by_txt)

    def sub_course_javascript_language(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_javascript_by_txt)

    def sub_course_typescript_language(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_typescript_by_txt)

    def sub_course_mongodb(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_mongodb_by_txt)

    def sub_course_html5(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_html5_by_txt)

    def sub_course_react(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_react_by_txt)

    def sub_course_java_language(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_java_language_by_txt)

    def sub_course_bootstrap(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_bootstrap_by_txt)

    def sub_course_app_development_for_android(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_app_development_for_android_by_txt)

    def sub_course_git(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_git_by_txt)

    def sub_course_sql(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_sql_by_txt)

    def sub_course_preparations_for_certification_exam(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_preparations_for_certification_exam_by_txt)

    def sub_course_cyber_attack_infrastructure(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_cyber_attack_infrastructure_by_txt)

    def sub_course_malware_analysis(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_malware_analysis_by_txt)

    def sub_course_penetration_testing(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_penetration_testing_by_txt)

    def sub_course_linux_fundamentals(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_linux_fundamentals_by_txt)

    def sub_course_cyber_security_fundamentals(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_cyber_security_fundamentals_by_txt)

    def sub_course_networking(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_networking_by_txt)

    def sub_course_forensics_investigation_and_incident_response(self):
        return self.driver.find_element(By.LINK_TEXT,
                                        self.sub_course_forensics_investigation_and_incident_response_by_txt)

    def sub_course_docker(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_docker_by_txt)

    def sub_course_linux_admin(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_linux_admin_by_txt)

    def sub_course_kubernetes(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_kubernetes_by_txt)

    def sub_course_zabbix(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_zabbix_by_txt)

    def sub_course_terraform(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_terraform_by_txt)

    def sub_course_ansible(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_ansible_by_txt)

    def sub_course_bash_scripting(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_bash_scripting_by_txt)

    def sub_course_aws(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_aws_by_txt)

    def sub_course_jenkins(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_jenkins_by_txt)

    def sub_course_machine_learning_fundamentals(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_machine_learning_fundamentals_by_txt)

    def sub_course_machine_learning_with_python(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_machine_learning_with_python_by_txt)

    def sub_course_deep_learning_with_tensorflow(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_deep_learning_with_tensorflow_by_txt)

    def sub_course_selenium(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_selenium_by_txt)

    def sub_course_labview(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_labview_by_txt)

    def sub_course_jira(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_jira_by_txt)

    def sub_course_qa_methodologies(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_qa_methodologies_by_txt)

    def sub_course_lpic_1(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_lpic_1_by_txt)

    def sub_course_lpic_2(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_lpic_2_by_txt)

    def sub_course_microsoft_azure(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_microsoft_azure_by_txt)

    def sub_course_open_cv(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_open_cv_by_txt)

    def sub_course_cuda(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_cuda_by_txt)

    def sub_course_nvidia_gpus(self):
        return self.driver.find_element(By.LINK_TEXT, self.sub_course_nvidia_gpus_by_txt)

    # def get_category_maslulim_list(self) -> list:
    #     return self.driver.find_elements(By.CLASS_NAME, self.maslulim_by_categories_by_class)
    #     self.driver.get('https://rt-crm.com/portal/#/login')
    #     return self.driver.title
