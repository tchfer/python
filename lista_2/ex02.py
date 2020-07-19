#-------------------------------------------------------------------------------
# asks user's name and age, then checks if the are overage and outputs their name and whether they are overage or not
#
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------

name = input("What's your name? ") # this variable saves the user's name
age = int(input("What's your age? ")) # this stores their age

if age >= 18: # this condition checks if user is overage or not and prints message if it is true
    print("Your name is" ,name, ", you are ",age, "years old and you are overage.")
elif age >0 and age <18: # this checks if they are between 1 and 17 to output the message saying they're underage
    print("Your name is" ,name, ", you are ",age, "years old and you are still underage.")
elif age == 0: # checks if user entered zero and outputs they're a newborn
    print("You are a newborn baby!")
else: # if they insert a negative number, they will be told it's invalid
    print("Invalid age")