#!python
"""
10/20/2017
This program should give us all the weekdays for a date.
 Example: 20 as a date can occur 3 times as a Wednesday.
"""
import datetime

def weekday():
    """
    Gets int as input and returns how many dates we have per weekday this year.
    """
    date_input = 1
    leap_year = False # 29.2 would be possible to be generated
    current_year = datetime.datetime.today().year # TODO: allow user to specify year
    dates = [] # will hold the 12 generated dates specified
    weekdays = [ ["Mo",0], ["Tu",0], ["We",0], ["Th",0], ["Fr",0], ["Sa",0], ["Su",0]] 

    if (current_year % 4) == 0:
        if (current_year % 100) == 0:
            if (current_year % 400) == 0:
                leap_year = True
        else:
            leap_year = True

    try:
        date_input = input("Enter date (1-31)")
    except IOError:
        print "Input Error. Bad Input for date!"

    if date_input > 0 and date_input <= 31:
        for month in range(1,13): #will go to 12 only
            if date_input < 29:
                dates.append(datetime.date(current_year, month, date_input))
            elif date_input <= 29 and leap_year: #This block should be for leap years only
                dates.append(datetime.date(current_year, month, date_input))
            elif date_input < 31 and month != 2:
                dates.append(datetime.date(current_year, month, date_input))
            elif date_input == 31:
                if month in [1,3,5,7,8,10,12]:
                    dates.append(datetime.date(current_year, month, date_input))

        for date in dates:
            weekdays[date.weekday()][1] += 1        

        for wday in weekdays:
            print wday[0], wday[1]
    

if __name__ == "__main__":
    weekday()
