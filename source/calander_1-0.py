# A command-line based program which allows you to read, write or edit entries into a text-based calendar.
# Version 1.0
# By Fabijus Sobolevas

print("Open calander? yes/no")
calander_open = raw_input()
if calander_open == "yes":
    read_calander = open("calander.txt","r")
    contents = read_calander.read()
    print(contents)
read_calander.close()



