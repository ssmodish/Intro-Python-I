"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

args = (sys.argv[1:])
# print(*args)


def cal(month_year):
    now = datetime.today()

    def build_cal(month=now.month, year=now.year):
        curr_cal = calendar.month(int(year), int(month))
        print(curr_cal)

    build_cal(*month_year)


if len(args) > 2 or int(args[0]) > 12:
    print("Cal.py can take up to two arguments. The output will be as follows:")
    print("1. No arguments - prints the calendar for the current month")
    print("2. One argument - prints the calendar for that month of the current year")
    print("3. Two arguments - prints the calendar for the month and year provided")
else:
    cal(args)
