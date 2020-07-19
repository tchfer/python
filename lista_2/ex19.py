# -------------------------------------------------------------------------------
# creates a menu for user to choose between tax, new wages, wages classification
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
#creates menu
print("=" * 37)
print("Option menu: \n1. Tax        \n2. New Salary          \n3. Salary classification ")
print("=" * 37)
option = int(input("Enter one of the options from the menu -> "))
wages = float(input("What is your current salary? -> "))
if option == 1: #check if option 1 was selected to do calculations and output result
    if wages < 500:
        tax = wages * 5 / 100
        print("The tax you will have to pay based on your wages is: R${}".format(tax))
    elif wages >= 500 and wages <= 850:
        tax = wages * 10 / 100
        print("The tax you will have to pay based on your wages is: R${}".format(tax))
    elif wages > 850:
        tax = wages * 15 / 100
        print("The tax you will have to pay based on your wages is: R${}".format(tax))
elif option == 2: #check if option 2 was selected to do calculations and output result
    if wages < 450:
        print("Your new salary is R${}".format(wages + 100))
    elif wages >= 450 and wages < 750:
        print("Your new salary is R${}".format(wages + 75))
    elif wages >= 750 and wages <= 1500:
        print("Your new salary is R${}".format(wages + 50))
    elif wages > 1500:
        print("Your new salary is R${}".format(wages + 25))
elif option == 3: #check if option 3 was selected to do calculations and output result
     if wages <= 700:
        print("You are badly paid.")
     elif wages > 700:
        print("You are well paid.")
else: #outputs that user entered an invalid option if the others don't run
    print("Invalid option!")