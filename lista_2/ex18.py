# -------------------------------------------------------------------------------
# creates a menu with jobs and outputs salary increase according to one's position
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
#creates menu
print("=" * 37)
print("Option menu: \n1. Book Keeper       50% \n2. Secretary         35% \n3. Bank Clerk        20% \n4. Manager           10% \n5. Director          No payment raise ")
print("=" * 37)
option = int(input("Enter one of the options from the menu according to your position -> "))
wages = float(input("What is your current salary? -> "))
#checks position, calculates salary raise, adds bonus to salary and outputs position, salary raise and new salary
if option == 1:
    print("The position is Book Keeper")
    pay_raise = wages * 50 / 100
    print("The pay raise is: R${}".format(pay_raise))
    print("The new salary is: R${}".format(wages + pay_raise))
elif option == 2:
    print("The position is Secretary")
    pay_raise = wages * 35 / 100
    print("The pay raise is: R${}".format(pay_raise))
    print("The new salary is: R${}".format(wages + pay_raise))
elif option == 3:
    print("The position is Bank Clerk")
    pay_raise = wages * 20 / 100
    print("The pay raise is: R${}".format(pay_raise))
    print("The new salary is: R${}".format(wages + pay_raise))
elif option == 4:
    print("The position is Manager")
    pay_raise = wages * 10 / 100
    print("The pay raise is: R${}".format(pay_raise))
    print("The new salary is: R${}".format(wages + pay_raise))
elif option == 5:
    print("The position is Director")
    print("There is no pay rise as you are a Director.")
else:
    print("Invalid option!")