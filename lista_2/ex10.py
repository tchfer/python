#-------------------------------------------------------------------------------
# write a program which asks the user to enter 2 numbers and outputs the biggest one
#
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------

num1 = float(input("Type the first number: ")) #allocates value for the fisrt number
num2 = float(input("Type the second number: ")) #allocates value for the second number

if num1 > num2: #checks if the first number is bigger than the second and prints if it's true
    print("The first number you entered, {:.2f}, is bigger than {:.2f} ".format(num1, num2)) # {:.2f} is the command to reduce decimal places down to 2 - it can be altered to however many you want
else: #prints that the second number is bigger than the first entered
    print("{:.2f} is bigger than {:.2f}!".format(num2, num1)) # {} .format(variable, variable), is the python 3 print feature