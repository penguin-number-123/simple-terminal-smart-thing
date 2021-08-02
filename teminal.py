
import calendar
from datetime import date
from datetime import date
import wikipedia
todays_date = date.today()

print("Current date: ", todays_date)
print("Welcome to MyManagannarojf co Manager!")
print("Type the input below!")
inpt = ""
inno = 0
plan = {
    "Jan":["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
    "Feb":["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
    "Mar":["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
    "Apr":["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
    "May":["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
    "Jun":["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
    "Jul":["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
    "Aug":["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
    "Sep":["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
    "Oct":["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
    "Nov":["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
    "Dec":["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
}
notes = {
    "note1":["","","","","","","","","","","","","","","",""],
    "note2":["","","","","","","","","","","","","","","",""],
    "note3":["","","","","","","","","","","","","","","",""],
    "note4":["","","","","","","","","","","","","","","",""],
    "note5":["","","","","","","","","","","","","","","",""],
    "note6":["","","","","","","","","","","","","","","",""],
    "note7":["","","","","","","","","","","","","","","",""],
    "note8":["","","","","","","","","","","","","","","",""],
    "note9":["","","","","","","","","","","","","","","",""],
    "note10":["","","","","","","","","","","","","","","",""],
    "note11":["","","","","","","","","","","","","","","",""],
    "note12":["","","","","","","","","","","","","","","",""],
    "note13":["","","","","","","","","","","","","","","",""],
    "note14":["","","","","","","","","","","","","","","",""],
    "note15":["","","","","","","","","","","","","","","",""],
    "note16":["","","","","","","","","","","","","","","",""]
}
planner = 0
def ask(n):
    inno = n
    inpt = input("In[" + str(inno) + "]:")
    if inpt == "Planner" or inpt == "planner" or inpt == "plan":
        month = input("Enter any month (shorthand, i.e. Jan):")
        if month == "Jan":
            m = 1
        if month == "Feb":
            m = 2
        if month == "Mar":
            m = 3
        if month == "Apr":
            m = 4
        if month == "May":
            m = 5
        if month == "Jun":
            m = 6
        if month == "Jul":
            m = 7
        if month == "Aug":
            m = 8
        if month == "Sep":
            m = 9
        if month == "Oct":
            m = 10
        if month == "Nov":
            m = 11
        if month == "Dec":
            m = 12
        print(calendar.month(todays_date.year, m))
        planner = 1
        if planner == 1:
            print("Enter a number to see what you need to do on the date, or a subcommand.")
            pinp = input("Enter planner subcommand:")
            month = input("Enter any month (shorthand, i.e. Jan):")
            if pinp.isnumeric() == True and int(pinp) <=31:
                print("On "+pinp+"th of "+ month +" , your plans are:")
                print("+--------------------------------------------------------------------------------------+")
                print(plan[str(month)][int(pinp)-1])
                print("+--------------------------------------------------------------------------------------+")

            elif pinp == "edit":
                month = input("Enter any month (shorthand, i.e. Jan):")
                day = int(input("Enter day to edit(1-31):"))
                text = input("Enter the plan (Use | to add a line break):")
                plan[str(month)][day-1] = text.replace('|', '\n')
                print(plan[str(month)][day-1])
            elif pinp == "exit" or pinp == "Exit" or pinp == "end":
                planner = 0
    if inpt == "note" or inpt == "Note":
        print("Note")
        Notenum = input("Please enter the number of the note. (1-16):")
        print("+-----------------------------------------------+")
        for i in notes["note"+Notenum]:
            print(notes["note"+Notenum][i])
        print("+-----------------------------------------------+")
    if inpt == "exit" or inpt == "Exit" or inpt == "end":
        exit()
            
for i in range(8192):
    ask(i)

