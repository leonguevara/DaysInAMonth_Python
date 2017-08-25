#   main.py
#   DaysInAMonth_Python
#
#   This program will give you the number of days of any given month of any given year
#
#   Python interpreter: 3.6
#
#   Author: León Felipe Guevara Chávez
#   email:  leon.guevara@itesm.mx
#   date:   May 31, 2017
#

#   We ask for and read the month's number
month = int(input("Give me the number of the month (1 - 12): "))
#   We ask for and read the year's number
year = int(input("Give me the number of the year (XXXX): "))

#   We find out the number of days that last this particular month
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    daysOfMonth = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    daysOfMonth = 30
else:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        daysOfMonth = 29
    else:
        daysOfMonth = 28

#   We display our findings
print("The numbers of days in this month is " + str(daysOfMonth))
