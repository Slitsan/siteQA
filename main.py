# This is a sample Python script.
#        28_2_2022
#      created by Dima
#   POM automation app for rt-ed.co.il
# --------------------------------------------------------------------------------------

# -------------   main   -----------------------------------------------------

file = open("./Source/src.html", "r")
for line in file.readlines():
    if "maslulim_by_xpath" in line:
        print(line)
        striped_line = line.strip("<div class=\"header\" id=\"maslulim_by_xpath\">").split("<")
        print(striped_line)
        line = str(striped_line[0])
        print(line)
file.close()