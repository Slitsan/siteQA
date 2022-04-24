import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.relative_locator import locate_with


class Footer:

    def __init__(self, drive: WebDriver):
        self.driver = drive
        self.popUp_close_xpath = '//*[@id="lead-form-modal1"]/span'

        self.list_real_time_by_xpath = '//*[@id="colophon"]/div/div[1]/div[1]/ul/li/a'

        self.list_web_development_by_xpath = '//*[@id="colophon"]/div/div[1]/div[2]/ul/li/a'
        self.list_cyber_security_by_xpath = '//*[@id="colophon"]/div/div[1]/div[3]/ul/li/a'
        self.list_devops_by_xpath = '//*[@id="colophon"]/div/div[1]/div[4]/ul/li/a'
        self.list_data_science_by_xpath = '//*[@id="colophon"]/div/div[1]/div[5]/ul/li/a'
        self.list_software_testing_by_xpath = '//*[@id="colophon"]/div/div[1]/div[6]/ul/li/a'
        self.list_image_processing_by_xpath = '//*[@id="colophon"]/div/div[1]/div[7]/ul/li/a'
        self.list_others_by_xpath = '//*[@id="colophon"]/div/div[2]/div[1]/ul'

        self.site_info_by_xpath = '//*[@id="colophon"]/div/div[2]/div[2]/p'
        self.social_links_by_xpath= '//*[@id="social-links"]/div[2]/span'


        # ----------------------- Real Time --------------------------
        self.internet_things_by_txt = "Internet Of Things"
        self.freertos_by_txt = "FreeRTOS"
        self.c_plus_plus_by_txt = "שפת C++"
        self.yocto_by_txt = "Yocto Programming"
        self.embedded_by_txt = "Embedded Linux"
        self.rt_concepts_by_txt = "RT Concepts"
        self.c_language_by_txt = "שפת C"
        self.linux_kernel_by_txt = "Linux Kernel And Device Drivers"
        self.arm_embedded_by_txt = "ARM Embedded Systems"
        # ----------------------- web_development--------------------------
        self.git_by_txt = "GIT (Version Control)"
        self.sql_by_txt = "SQL"
        self.web_by_txt = "Web Foundations"
        self.angularjs_by_txt = "AngularJS | אנגולר"
        self.python_by_txt = "פייתון | Python"
        self.css3_by_txt = "CSS3"
        self.nodeJS_by_txt = "NodeJS"
        self.javascript_by_txt = "Javascript"
        self.typeScript_by_txt = "TypeScript"
        self.mongoDB_by_txt = "MongoDB"
        self.html5_by_txt = "HTML5"
        self.react_by_txt = "React | ריאקט"
        self.java_by_txt = "Java"
        self.bootstrap_by_txt = "Bootstrap"
        self.android_by_txt = "פיתוח אפליקציות לאנדרואיד"
        # ----------------------- Cyber Security --------------------------
        self.forensics_by_txt = "Forensics Investigation & Incident Response"
        self.cyber_attack_by_txt = "Cyber Attack Infrastructure"
        self.c_eh_by_txt = "הכנה לבחינת הסמכה C | EH"
        self.malware_analysis_by_txt = "Malware Analysis"
        self.penetration_testing_by_txt = "Penetration Testing"
        self.cyber_security_by_txt = "Cyber Security Fundamentals"
        self.linux_fundamentals_by_txt = "Linux Fundamentals"
        self.networking_by_txt = "Networking"
        # ----------------------- Devops --------------------------
        self.aws_by_txt = "AWS"
        self.jenkins_by_txt = "Jenkins"
        self.docker_containers_by_txt = "Docker Containers"
        self.linux_admin_by_txt = "לינוקס | Linux Admin"
        self.kubernetes_by_txt = "Kubernetes"
        self.python_by_txt = "פייתון | Python"
        self.zabbix_by_txt = "Zabbix"
        self.terraform_by_txt = "Terraform"
        self.networking_by_txt = "Networking"
        self.ansible_by_txt = "ANSIBLE"
        self.bash_scripting_by_txt = "Bash Scripting"
        # ----------------------- Data Science --------------------------
        self.machine_learning_by_txt = "Machine Learning Fundamentals"
        self.machine_learning_with_python_by_txt = "Machine Learning With Python"
        self.deep_learning_by_txt = "Deep Learning With Tensorflow"
        # ----------------------- Software Testing --------------------------
        self.selenium_by_txt = "Selenium"
        self.labview_by_txt = "LabView"
        self.jira_by_txt = "JIRA | ג'ירה"
        self.qa_by_txt = "מתודולוגיות QA"
        self.java_by_txt = "Java"
        # ----------------------- Image Processing --------------------------
        self.cuda_by_txt = "CUDA"
        self.machine_learning_with_python_by_txt = "Machine Learning With Python"
        self.deep_learning_by_txt = "Deep Learning With Tensorflow"
        self.nvidia_by_txt = "Nvidia GPUs"
        self.machine_learning_by_txt = "Machine Learning Fundamentals"
        self.opencv_by_txt = "OpenCV"
        # ----------------------- others --------------------------

        self.about_us_by_txt = "אודות"
        self.courses_for_companies_by_txt = "קורסים לחברות"
        self.articles_by_txt = "מאמרים"
        self.jobs_by_txt = "דרושים"
        self.privacy_policy_by_txt = "מדיניות פרטיות"
        self.declaration_of_accessibility_by_txt = "הצהרת-נגישות"



    def find_element(self, path):
        return self.driver.find_element(By.XPATH, path)


    def get_title(self) -> str:
        return self.driver.title

    def site_info(self):
        return self.driver.find_element(By.XPATH, self.site_info_by_xpath)

    def social_links(self):
        return self.driver.find_elements(By.XPATH, self.social_links_by_xpath)

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

    def privacy_policy(self):
        return self.driver.find_element(By.LINK_TEXT, self.privacy_policy_by_txt)

    def list_of_real_time(self):
        return self.driver.find_elements(By.XPATH, self.list_real_time_by_xpath)

    def list_of_web_development(self):
        return self.driver.find_elements(By.XPATH, self.list_web_development_by_xpath)

    def list_cyber_security(self):
        return self.driver.find_elements(By.XPATH, self.list_cyber_security_by_xpath)

    def list_of_devops(self):
        return self.driver.find_elements(By.XPATH, self.list_devops_by_xpath)

    def list_of_data_science(self):
        return self.driver.find_elements(By.XPATH, self.list_data_science_by_xpath)

    def list_of_software_testing(self):
        return self.driver.find_elements(By.XPATH, self.list_software_testing_by_xpath)

    def list_of_image_processing(self):
        return self.driver.find_elements(By.XPATH, self.list_image_processing_by_xpath)

    def list_of_others(self):
        return self.driver.find_elements(By.XPATH, self.list_others_by_xpath)

    # def rt_concepts(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.rt_concepts_by_txt)
    #
    # def c_language(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.c_language_by_txt)
    #
    # def linux_kernel_and_device_drivers(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.linux_kernel_by_txt)
    #
    # def arm_embedded_systems(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.arm_embedded_by_txt)
    #
    # def internet_of_things(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.internet_things_by_txt)
    #
    # def free_rtos(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.freertos_by_txt)
    #
    # def c_plus_plus_language(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.c_plus_plus_by_txt)
    #
    # def yocto_programming(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.yocto_by_txt)
    #
    # def embedded(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.embedded_by_txt)
    #
    # def web_foundations(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.web_by_txt)
    #
    # def angular_js(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.angularjs_by_txt)
    #
    # def python_language(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.python_by_txt)
    #
    # def css_language(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.css3_by_txt)
    #
    # def node_js(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.nodeJS_by_txt)
    #
    # def javascript_language(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.javascript_by_txt)
    #
    # def typescript_language(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.typeScript_by_txt)
    #
    # def mongodb(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.mongoDB_by_txt)
    #
    # def html5(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.html5_by_txt)
    #
    # def react(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.react_by_txt)
    #
    # def java_language(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.java_by_txt)
    #
    # def bootstrap(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.bootstrap_by_txt)
    #
    # def app_development_for_android(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.android_by_txt)
    #
    # def git(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.git_by_txt)
    #
    # def sql(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.sql_by_txt)
    #
    # def preparations_for_certification_exam(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.c_eh_by_txt)
    #
    # def cyber_attack_infrastructure(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.cyber_attack_by_txt)
    #
    # def malware_analysis(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.malware_analysis_by_txt)
    #
    # def penetration_testing(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.penetration_testing_by_txt)
    #
    # def linux_fundamentals(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.linux_fundamentals_by_txt)
    #
    # def cyber_security_fundamentals(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.cyber_security_by_txt)
    #
    # def networking(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.networking_by_txt)
    #
    # def forensics_investigation_and_incident_response(self):
    #     return self.driver.find_element(By.LINK_TEXT,
    #                                     self.forensics_by_txt)
    #
    # def docker(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.docker_containers_by_txt)
    #
    # def linux_admin(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.linux_admin_by_txt)
    #
    # def kubernetes(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.kubernetes_by_txt)
    #
    # def zabbix(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.zabbix_by_txt)
    #
    # def terraform(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.terraform_by_txt)
    #
    # def ansible(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.ansible_by_txt)
    #
    # def bash_scripting(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.bash_scripting_by_txt)
    #
    # def aws(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.aws_by_txt)
    #
    # def jenkins(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.jenkins_by_txt)
    #
    # def machine_learning_fundamentals(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.machine_learning_by_txt)
    #
    # def machine_learning_with_python(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.machine_learning_with_python_by_txt)
    #
    # def deep_learning_with_tensorflow(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.deep_learning_by_txt)
    #
    # def selenium(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.selenium_by_txt)
    #
    # def labview(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.labview_by_txt)
    #
    # def jira(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.jira_by_txt)
    #
    # def qa_methodologies(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.qa_by_txt)
    #
    # def open_cv(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.opencv_by_txt)
    #
    # def cuda(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.cuda_by_txt)
    #
    # def nvidia_gpus(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.nvidia_by_txt)

