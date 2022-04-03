# This is a sample Python script.
#        28_2_2022
#      created by Dima
#   POM automation app for rt-ed.co.il
# --------------------------------------------------------------------------------------

# -------------   main   -----------------------------------------------------

# file = open("./Source/src.html", "r")
# for line in file.readlines():
#     if "maslulim_by_xpath" in line:
#         print(line)
#         striped_line = line.strip("<div class=\"header\" id=\"maslulim_by_xpath\">").split("<")
#         print(striped_line)
#         line = str(striped_line[0])
#         print(line)
# file.close()
from datetime import datetime

from POM.Tests.course_page_test import CoursePageTest
from POM.Tests.header_test import HeaderTest
from POM.Tests.home_page_test import HomePageTest
from POM.Tests.maslul_page_test import MaslulPageTest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


def write_errors_to_different_file():
    now = datetime.now()
    date_for_log = now.strftime("%d %m %Y")
    string_error_result = ""
    try:
        file = open(f"./Source/log {date_for_log}.txt", "r")
        for line in file.readlines():
            if "*" in line:
                string_error_result += line + "\n"
            elif "@" in line:
                string_error_result += line + "\n"
            elif "@@" in line:
                string_error_result += line + "\n"
            elif "!" in line:
                string_error_result += line + "\n"
        file.close()
    except FileNotFoundError:
        print("Did not found a file")
    try:
        file = open(f"./Source/Error log {date_for_log}.txt", "a+")
        file.write(string_error_result)
        file.close()
    except FileNotFoundError:
        print("Did not found a file")


def set_driver():
    driver: WebDriver = webdriver.Chrome(executable_path=
                                         'drivers/chromedriver.exe')
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(20)
    driver.set_page_load_timeout(30)
    driver.get('https://rt-ed.co.il/')
    return driver


if __name__ == '__main__':
    driver = set_driver()

    test_home_page = HomePageTest(driver)
    test_header = HeaderTest(driver)
    test_maslulim = MaslulPageTest(driver)
    test_courses = CoursePageTest(driver)

    test_home_page.test_run_all()
    test_header.test_header()
    test_maslulim.test_run_maslulim()
    test_courses.test_run_courses()
    write_errors_to_different_file()
