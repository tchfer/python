#-------------------------------------------------------------------------------
# user enter an otion from menu to have the sum of two numbers or the square root of a number
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------
from math import sqrt #library to do square root automatically
print("=" * 27) #lines 8, 9 and 10 creates the menu
print("Option menu: \n1. Add up two numbers. \n2. A number's square root. ") #\n is to star a new line without having another print command
print("=" * 27)
option = int(input("Enter one of the options from the menu -> ")) #user selects the option from the menu
if option == 1: #if user enter option 1, program gets the sum of the two numbers entered and prints it out
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number to add the two of them up: "))
    print("The sum of {} and {} is {}".format(n1, n2, n1 + n2))
elif option == 2: #if user chooses this otion, it gets the square root of a number they entered and prints it
    n = int(input("Enter a number to know its square root: "))
    print("The square root of {} is {}".format(n, sqrt(n)))
else: #tells the user it's an invalid option
    print("Invalid option")