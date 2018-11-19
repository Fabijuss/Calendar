# A command-line based program which allows you to read, write or edit entries into a text-based calendar.
# Version 1.3
# By Fabijus Sobolevas

#Imports required libraries
import time
import calendar
import datetime

#Sets the local date in now variable
now = datetime.datetime.now()

#finds local time and formats it
localtime = time.asctime(time.localtime(time.time()))
print "Current date and time:", localtime

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

#while loop so user can only enter 2 options
while dateOption != "y" and dateOption != "n":
        print("Invalid choice, try again.")
        dateOption = raw_input()
        
if dateOption == "y":
    year = now.year
    month = now.month
    day = now.day
    
def yearOption():
    global year #makes the variable global, so that it can be changed later
    year = raw_input("Enter year (xxxx): \n")
    while int(year) > 3000 or int(year) < 1: #limits the date so that a large number can't be entered
                print("Invalid choice, try again.")
                year = raw_input("Enter year (xxxx): \n")      
    while True:
            try:
                float(year) #checks if input is integer
            except ValueError:
                print("Invalid choice, try again.")
                year = raw_input("Enter year (xxxx): \n") #if not integer, ask for another input
            else:
                break #if input is integer, breaks loop        

def monthOption():
    global month
    month = raw_input("Enter month (xx): \n")
    while int(month) > 12 or int(month) < 1:
            print("Invalid choice, try again.")
            month = raw_input("Enter month (xx): \n")            
    while True:
            try:
                float(month)
            except ValueError:
                print("Invalid choice, try again.")
                month = raw_input("Enter month (xx): \n")
            else:
                break        
def dayOption():
    global day
    day = raw_input("Enter day (xx): \n")
    while int(day) > 31 or int(day) < 1:
            print("Invalid choice, try again.")
            day = raw_input("Enter day (xx): \n")            
    while True:
            try:
                float(day)
            except ValueError:
                print("Invalid choice, try again.")
                day = raw_input("Enter day (xx): \n")
            else:
                break
        
if dateOption == "n":
        yearOption()
        
if dateOption == "n":
        monthOption()
        
if dateOption == "n":
        dayOption()

        
        
def calendarProgram():
    print(str(year) + '/' + str(month) + '/' + str(day))
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
|  Change date (d)                                  |
|                                                   |
+---------------------------------------------------+
|                                                   |
|  Exit (x)                                         |
|                                                   |
+---------------------------------------------------+""")
    calanderOption = raw_input()

    while calanderOption != "r" and calanderOption != "w" and calanderOption != "a" and calanderOption != "d" and calanderOption != "x":
        print("Invalid choice, try again.")
        calanderOption = raw_input()
      
    if calanderOption == "r":
        openCalander = open("calander.txt","r")
        contents = openCalander.read()
        print("Printing Calander...\n")
        print(contents)
        openCalander.close()
        
    if calanderOption == "d":
            yearOption()
            monthOption()
            dayOption()
            
    if calanderOption == "a":
        openCalander = open("calander.txt","r+")
        contents = openCalander.read()
        print("Printing Calander...\n")
        print(contents)
        openCalander.close()
        openCalander = open("calander.txt","a+")
        input = raw_input("Enter calander entry\n")
        openCalander.write('\n' + str(year) + '/' + str(month) + '/' + str(day) + ' ' + str(input))
        openCalander.close()

    if calanderOption == "x":
        raise SystemExit

    if calanderOption == "w":
            print("""
+---------------------------------------------------+
|                                                   |
|  Calander application                             |
|                                                   |
+---------------------------------------------------+
|                                                   |
|  Are you sure?                                    |
|                                                   |
|  This will overwrite any existing entries.        |
|                                                   |
|  Yes (y)                                          |
|                                                   |
|  No (n)                                           |
|                                                   |
+---------------------------------------------------+""")
            confirm = raw_input()
            while confirm != "n" and confirm != "y":
                     print("Invalid choice, try again.")
                     confirm = raw_input()

            if confirm == "y":
                openCalander = open("calander.txt","w+")
                contents = openCalander.read()
                print("Printing Calander...\n")
                print(contents)
                input = raw_input("Enter calander entry\n")
                openCalander.write(str(year) + '/' + str(month) + '/' + str(day) + ' ' + str(input))
                openCalander.close()

            if confirm == "n":
                calendarProgram()



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
