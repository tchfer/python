#-------------------------------------------------------------------------------
# program outputs date and time from system
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------
from datetime import datetime # library
today = datetime.now()#gets the date and time from library
# conditions checks which month is being output to change from number to name of month
if today.month == 1:
    month = ("January")
elif today.month == 2:
    month = ("February")
elif today.month == 3:
    month = ("March")
elif today.month == 4:
    month = ("April")
elif today.month == 5:
    month = ("May")
elif today.month == 6:
    month = ("June")
elif today.month == 7:
    month = ("July")
elif today.month == 8:
    month = ("August")
elif today.month == 9:
    month = ("September")
elif today.month == 10:
    month = ("October")
elif today.month == 11:
    month = ("November")
elif today.month == 12:
    month = ("December")
print("The current date is time is: {:02d}/ {} / {} - {:02d}:{:02d}:{:02d} ".format(today.day, month, today.year, today.hour, today.minute, today.second))