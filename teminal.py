
import calendar
from datetime import date
from datetime import date
import os
from decimal import Decimal
import time
import json
from wikipedia.wikipedia import languages
for i in range(5):
    print("Loading... |")
    time.sleep(0.2)
    os.system("cls")
    print("Loading... /")
    time.sleep(0.2)
    os.system("cls")
    print("Loading... -")
    time.sleep(0.2)
    os.system("cls")
    print("Loading... \\")
    time.sleep(0.2)
    os.system("cls")

todays_date = date.today()

print("Current date: ", todays_date)
print("Welcome to Your Life Data Processing Terminal Program That Is Worse Than Your Smartphone And Comes With Absolutely No Warranty!")
print("Organize your life!")
print("YLDPTPTIWTYSACWANW is a trademark  of me. ")
print("Type a command below!(For help, type \"help\" for help)")
inpt = ""
with open("plan.json", "r+") as fp:
    plan = json.load(fp)
inno = 0
with open("notes.json", "r+") as fp:
    notes = json.load(fp)

planner = 0
def ask(n):
    inno = n
    inpt = input("In[" + str(inno) + "]:")
    if inpt == "Planner" or inpt == "planner" or inpt == "plan":
        month = input("Enter any month (shorthand, i.e. Jan):")
        max = 0
        lname = ""
        if month == "Jan":
            m = 1
            max = 31
            lname = "January"
        if month == "Feb":
            m = 2
            if calendar.isleap(todays_date.year):
                max = 29
            else:
                max = 28

        if month == "Mar":
            m = 3
            max = 31


        if month == "Apr":
            m = 4
            max = 30

        if month == "May":
            m = 5
            max = 31

        if month == "Jun":
            m = 6
            max = 30

        if month == "Jul":
            m = 7
            max = 31

        if month == "Aug":
            m = 8
            max = 31

        if month == "Sep":
            m = 9
            max = 30

        if month == "Oct":
            m = 10
            max = 31

        if month == "Nov":
            m = 11
            max = 30

        if month == "Dec":
            m = 12
            max = 31

        print(calendar.month(todays_date.year, m))
        planner = 1
        while planner == 1:
            print("Enter a number to see what you need to do on the date, or a subcommand.")
            pinp = input("Enter planner subcommand:")
            month = input("Enter any month (shorthand, i.e. Jan):")
            if pinp.isnumeric() == True and int(pinp) <=31 and int(pinp) <= max:
                print("On "+pinp+"th of "+ month +" , your plans are:")
                print("+--------------------------------------------------------------------------------------+")
                print(plan[str(month)][int(pinp)-1])
                print("+--------------------------------------------------------------------------------------+")
            elif pinp == "edit":
                edit = 1
                while edit == 1:
                    day = int(input("Enter day to edit(1-31):"))
                    text = input("Enter the plan (Use | to add a line break):")
                    if day <=0:
                        edit = 0
                    if day >= 0 and day <= max:
                        plan[str(month)][day-1] = text.replace('|', '\n')
                        print(plan[str(month)][day-1])
                    if day > max:
                        print("There is no "+ pinp +"th of "+ month+ "\n Please try again.")
            elif pinp == "exit" or pinp == "Exit" or pinp == "end":
                planner = 0
            elif pinp.isnumeric() == True and int(pinp) > max:
                print("There is no "+ pinp +"th of "+ month+ "\n Please try again.")
    if inpt == "note" or inpt == "Note":
        note = 1
        while note == 1:
            if ninp == "exit":
                note = 0
            print("Note")
            ninp = input("Enter the sub command.")
            Notenum = input("Please enter the number of the note. (1-16):")
            print("+-----------------------------------------------+")
            for i in range(len(notes["note"+str(Notenum)])):
                print(notes["note"+str(Notenum)][int(i)])
            print("+-----------------------------------------------+")
            if ninp == "edit":
                edit = 1
                while edit == 1:
                    print("Editing Mode.")
                    print("Enter a number (1-16 when prompted to enter a number.) \n This is the line to be edited in note "+Notenum)
                    line = int(input("Enter a number(1-16) or -1 to exit:"))
                    if line <= 16 and line > 0:
                        txt = input("Enter the text for the line.")
                        notes["note"+str(Notenum)][line-1] = txt
                    if line == 0 or line == -1:
                        edit = 0
            else:
                print("You couldn't follow simple instructions. How sad.")
            if ninp == "read":
                print("Enter the file number (1-16)")
                Notenum = input("Please enter the number of the note. (1-16):")
                print("+-----------------------------------------------+")
                for i in range(len(notes["note"+str(Notenum)])):
                    print(notes["note"+str(Notenum)][int(i)])
                print("+-----------------------------------------------+")
    if inpt == "Help" or inpt == "help":
        print("There is no help now. How sad.")

    if inpt == "exit" or inpt == "Exit" or inpt == "end":
        exit()
            
for i in range(8192):
    ask(i)

