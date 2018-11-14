# A command-line based program which allows you to read, write or edit entries into a text-based calendar.
# Version 1.2
# By Fabijus Sobolevas

import time
import calendar
import datetime

now = datetime.datetime.now()

localtime = time.asctime(time.localtime(time.time()))
print "Current date and time: ", localtime

print("""
+---------------------------------------------------+
|                                                   |
|  Calander application                             |
|                                                   |
+---------------------------------------------------+
|                                                   |
|  Would you like to use current date?              |
|                                                   |
|  Yes (y)                                          |
|                                                   |
|  No (n)                                           |
|                                                   |
+---------------------------------------------------+""")

dateOption = raw_input()

while dateOption != "y" and dateOption != "n":
        print("Invalid choice, try again.")
        dateOption = raw_input()
        
if dateOption == "y":
    year = now.year
    month = now.month
    day = now.day

if dateOption == "n":
    year = int(input("Enter year: \n"))
    if year == "":
        print("Invalid choice, try again.")
        year = input("Enter year: \n")
if dateOption == "n":
    month = input("Enter month: \n")

if dateOption == "n":
    day = input("Enter day: \n")

if year == "":
    print("Invalid choice, try again.")
    year = input("Enter year: \n")
    
def calendarProgram():
    print("""
+---------------------------------------------------+
|                                                   |
|  Calander application                             |
|                                                   |
+---------------------------------------------------+
|                                                   |
|  What would you like to do?                       |
|                                                   |
|  Read (r)                                         |
|                                                   |
|  Overwrite entries (w)                            |
|                                                   |
|  Add new entries (a)                              |
|                                                   |
+---------------------------------------------------+
|                                                   |
|  Exit (x)                                         |
|                                                   |
+---------------------------------------------------+""")
    calanderOption = raw_input()

    while calanderOption != "r" and calanderOption != "w" and calanderOption != "a" and calanderOption != "x":
        print("Invalid choice, try again.")
        calanderOption = raw_input()
      
    if calanderOption == "r":
        openCalander = open("calander.txt","r")
        contents = openCalander.read()
        print("Printing Calander...\n")
        print(contents)
        openCalander.close()

    if calanderOption == "x":
        raise SystemExit

    if calanderOption == "w":
        openCalander = open("calander.txt","w+")
        contents = openCalander.read()
        print("Printing Calander...\n")
        print(contents)
        input = raw_input("Enter calander entry\n")
        openCalander.write(str(year) + '/' + str(month) + '/' + str(day) + ' ' + str(input))
        openCalander.close()





def restartCode():
    print("""
+---------------------------------------------------+
|                                                   |
|  Calander application                             |
|                                                   |
+---------------------------------------------------+
|                                                   |
|  What would you like to do?                       |
|                                                   |
|  Perform another action (y)                       |
|                                                   |
|  Exit (x)                                         |
|                                                   |
+---------------------------------------------------+""")
    restart = raw_input()
    while restart != "y" and restart != "x":
        print("Invalid choice, try again.")
        restart = raw_input()
        
    while restart == "y":
        calendarProgram()
        restartCode()

    if restart == "x":
        raise SystemExit

calendarProgram()
restartCode()

# Keeps commandline from closing instantly
exit = raw_input
