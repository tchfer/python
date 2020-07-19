#-------------------------------------------------------------------------------
# checks swimmer's age to tell the user the category they're in
#
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------

age = int(input("Please insert the swimmmer's age: "))
if age >= 5 and age <= 10: # this checks if the age is from 5 to 10 to output that they are in the kids' category
    print('The swimmer is in the Kids category.')
elif age >= 11 and age <= 17: # this checks if the age is from 11 to 17 to output that they are in the teenager / young adult category
    print('The swimmer is in the Teenager / Young Adult category')
elif age >= 18: # this checks if the age is 18 or older to output that they are in the adult's category
    print('The swimmer is in the Adult category')
else: # if all the other conditions are false, this outputs that the child isn't ready to become a swimmer
    print("There isn't a category for this age. Come back when your child is 5 or older.")