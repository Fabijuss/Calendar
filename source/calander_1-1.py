# A command-line based program which allows you to read, write or edit entries into a text-based calendar.
# Version 1.1
# By Fabijus Sobolevas

def calendar():
    print("""
+---------------------------------------------------+
|                                                   |
|  What would you like to do?                       |
|                                                   |
|  Read (r)                                         |
|                                                   |
|  Write (w)                                        |
|                                                   |
|  Edit (e)                                         |
|                                                   |
+---------------------------------------------------+
|                                                   |
|  Exit (x)                                         |
|                                                   |
+---------------------------------------------------+""")
    calanderOption = raw_input()

    while calanderOption != "r" and calanderOption != "w" and calanderOption != "e" and calanderOption != "x":
        print("Invalid choice, try again.")
        calanderOption = raw_input()
      
    if calanderOption == "r":
        readCalander = open("calander.txt","r")
        contents = readCalander.read()
        print(contents)
        readCalander.close()

    if calanderOption == "x":
        raise SystemExit


def restartCode():
    print("""
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
        calendar()
        restartCode()

    if restart == "x":
        raise SystemExit

calendar()
restartCode()

# Keeps commandline from closing instantly
exit = raw_input
