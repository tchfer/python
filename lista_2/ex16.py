# -------------------------------------------------------------------------------
# reads user's date input and outputs the bigger one between them
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
#lines 7 to 15 asks user to enter dates 1 and 2
print("First date")
day = int(input("   Enter the day: "))
month = int(input("   Enter the month: "))
year = int(input("   Enter the year: "))
print("Second date")
day2 = int(input("   Enter the day: "))
month2 = int(input("   Enter the month: "))
year2 = int(input("   Enter the year: "))
print("=" * 30)
#from this line on, program checks which date is the highest by analyzing the day, month and year of both
if year > year2:
    print("The higher date is: {} / {} / {}".format(day, month, year))
elif year2 > year:
    print("The higher date is: {} / {} / {}".format(day2, month2, year2))
elif month > month2:
    print("The higher date is: {} / {} / {}".format(day, month, year))
elif month2 > month:
    print("The higher date is: {} / {} / {}".format(day2, month2, year2))
elif day > day2:
    print("The higher date is: {} / {} / {}".format(day, month, year))
elif day2 > day:
    print("The higher date is: {} / {} / {}".format(day2, month2, year2))
else:
    print("The dates are identically the same")
