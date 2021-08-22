
import calendar
from datetime import date
import os
from decimal import Decimal
import time
import json
import random
import hashlib
from math import *
from ask_function import ask
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

def convert_shortmonthname(month):
    if len(month) == 3:
        return month.capitalize()
    else:
        return (month[:-(len(month)-3)]).capitalize()
with open("usernamePassword.json", "r+") as userpassfile:
    userpassdict = json.load(userpassfile)
d = 0
while(d < 3):
    username = input("Enter username:")
    password = hashlib.sha512(input("Enter password:").encode('utf-8')).hexdigest()

    if username in userpassdict and password == userpassdict[username]:
        with open("plan_"+ username +".json", "r+") as planfile:
            plan = json.load(planfile)
        print(f"Welcome, {username}. You are now successfully logged in.")
        print("Current date: ", todays_date)
        print("Events today:")
        print(plan[convert_shortmonthname(calendar.month_name[todays_date.month])][todays_date.day])
        print("Welcome to Your Life Data Processing Terminal Program That Is Worse Than Your Smartphone And Comes With Absolutely No Warranty!")
        print("Organize your life!")
        print("YLDPTPTIWTYSACWANW is a trademark  of me. ")
        for i in range(8192):
            ask(i,username,(username=="admin"))
    else:
        d += 1
        print("Username or password incorrect. Please try again.")
if d==3:
    print("Sorry, max tries exceeded.")





