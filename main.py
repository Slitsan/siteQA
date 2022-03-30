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

now = datetime.now()
date_for_log = now.strftime("%d %m %Y")
string_error_result = ""

try:
    file = open(f"./Source/log {date_for_log}.txt", "r")
    for line in file.readlines():
        if "*" in line:
            string_error_result += line.strip("*") + "\n"
        elif "@" in line:
            string_error_result += line.strip("@") + "\n"
        elif "@@" in line:
            string_error_result += line.strip("@@") + "\n"
        elif "!" in line:
            string_error_result += line.strip("!") + "\n"
    file.close()
except FileNotFoundError:
    print("Did not found a file")

try:
    file = open(f"./Source/Error log {date_for_log}.txt", "a+")
    file.write(string_error_result)
    file.close()
except FileNotFoundError:
    print("Did not found a file")
