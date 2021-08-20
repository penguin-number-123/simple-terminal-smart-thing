
import calendar
from datetime import date
from datetime import date
import os
from decimal import Decimal
import time
import json
import random
import hashlib
from math import *
for i in range(5):
    print("Loading... |")
    time.sleep(0.1)
    os.system("cls")
    print("Loading... /")
    time.sleep(0.1)
    os.system("cls")
    print("Loading... -")
    time.sleep(0.1)
    os.system("cls")
    print("Loading... \\")
    time.sleep(0.1)
    os.system("cls")

todays_date = date.today()
hist = []
with open("plan.json", "r+") as planfile:
    plan = json.load(planfile)
with open("notes.json", "r+") as notesfile:
    notes = json.load(notesfile)

print("Current date: ", todays_date)
print("Welcome to Your Life Data Processing Terminal Program That Is Worse Than Your Smartphone And Comes With Absolutely No Warranty!")
print("Organize your life!")
print("YLDPTPTIWTYSACWANW is a trademark  of me. ")
print("Enter Credidentialsdjoifidfjdjf:")

inpt = ""

planner = 0
def ask(n):
    inpt = input("In[" + str(n) + "]:")
    if inpt == "Planner" or inpt == "planner" or inpt == "plan":
        month = input("Enter any month (shorthand, i.e. Jan):")
        max = 0

        if month == "Jan":
            m = 1
            max = 31

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
        print("Note")
        ninp = input("Enter the sub command.")
        Notenum = input("Please enter the number of the note. (1-16):")
        while note == 1:
            if ninp == "exit":
                note = 0
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
    if inpt =="Calculator" or inpt == "Calc" or inpt == "calc" or inpt =="calculator":
        mode = input("Enter Simple for normal, Sci for scientific.")
        while mode == "Simple":
            def printhist():
                print("+--------------------------------------------------+")
                print("|History:                                          |")
                for i in range(len(hist)):
                    print("|"+str(hist[i]).ljust(50," ")+"|")
                print("+--------------------------------------------------+")
            print("All operations will take the form a/b, where a is the first input and b is the second.")
            op = input("Enter the operation symbol: +-*/, or exit to exit:")
            num1 = input("Enter a number:")
            num2 = input("Enter a number:") 
            if op == "+":
                a = Decimal(int(num1)) + Decimal(int(num2))
                hist.append(num1 +"+"+ num2)
                hist.append(a)
                print(a)
            if op == "-":
                a = Decimal(int(num1)) - Decimal(int(num2))
                hist.append(num1 +"-"+ num2)
                hist.append(a)
                print(a)
            if op == "*":
                a = Decimal(int(num1)) * Decimal(int(num2))
                hist.append(num1 +"*"+ num2)
                hist.append(a)
                print(a)
            if op == "/":
                a = Decimal(int(num1)) / Decimal(int(num2))
                hist.append(num1 +"/"+ num2)
                hist.append(a)
                print(a)
            if op == "^":
                a = Decimal(int(num1)) ** Decimal(int(num2))
                hist.append(num1 +"^"+ num2)
                hist.append(a)
                print(a)
            printhist()
            if op == "exit":
                mode = ""
        while mode == "Sci":
            def printhist():
                print("+--------------------------------------------------+")
                print("|History:                                          |")
                for i in range(len(hist)):
                    print("|"+str(hist[i]).ljust(50," ")+"|")
                print("+--------------------------------------------------+")
            expression = input("Enter the expression:")
            if expression == "exit":
                mode = ""
                break
            else:
                out = eval(expression)
                print(out)
                hist.append(expression)
                hist.append(str(out))
                printhist()
    if inpt == "Games":
        print("Games: Guess the number, null")
        print("For guess the number, enter GTN., for null, enter null")
    if inpt == "GTN":
        gtn = 1
        while(gtn == 1):
            maxnum = int(input("What do you want the largest number to be?"))
            correctans = random.randint(1, maxnum)
            maxtry = int(input("Enter 1, 2 or 3 for 10, 20 ,30 tries respectively:"))
            if maxtry > 3:
                print("input is not valid, try again")
                maxtry = int(input("Enter 1, 2 or 3 for 10, 20 ,30 tries respectively:"))
            else:
                maxtry = maxtry * 10
            print("Generated random number.")
            b = 0
            print(b)
            print(correctans)
            while(b < maxtry):
                b += 1
                guess = int(input("Enter your guess(-1 to exit):"))
                if guess == -1:
                    gtn = 0
                    break
                if guess == correctans:
                    print("You did it! It only took you "+ str(b) +" steps.")
                    break
                elif guess > correctans and guess - correctans > 100:
                    print("You went too high, try going lower.")
                elif guess > correctans and guess - correctans <= 100:
                    print("You are close, try going lower.")
                elif guess < correctans and correctans - guess > 100:
                    print("You went too low, try going higher.")
                elif guess < correctans and correctans - guess <= 100:
                    print("You are close, try going higher.")
                
    if inpt == "Help" or inpt == "help":
        print("There is no help now. How sad.")

    if inpt == "exit" or inpt == "Exit" or inpt == "end":
        planfile.close()
        notesfile.close()
        exit()
with open("usernamePassword.json", "r+") as userpassfile:
    userpassdict = json.load(userpassfile)
d = 0
while(d < 3):
    username = input("Enter username:")
    password = hashlib.sha512(input("Enter password:").encode('utf-8')).hexdigest()
    if username in userpassdict and password == userpassdict[username]:
        print(f"Welcome, {username}. You are now successfully logged in.")
        for i in range(8192):
            ask(i)
    else:
        d += 1
        print("Username or password incorrect. Please try again.")
if d==3:
    print("Sorry, max tries exceeded.")