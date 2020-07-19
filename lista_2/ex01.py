#-------------------------------------------------------------------------------
# shows a person's new salary with 30 or 50% depending on how much they make
#
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------

salary = float(input('What is your salary? -> ')) # takes in a person's salary
# this line checks whether user's input was larger than 0 and less or equal to $300 to do the operation below
if salary >0 and salary <= 300: # if the condition above entered above is true, program calculates the bonus, which is 50% of the whole salary up to $300
    bonus = salary * 50 / 100 # here the bonus is added up to the salary in order to print the result to the user
    new_salary = salary + bonus # this line makes the program print the salary after all the calculation have been done if input matches if statement
    print('Your salary with 50% added to it is $' ,new_salary) # this Calculates the salary after 50% was added to it
elif salary > 300: # here the code calculates 30% of the salary and adds it up
    bonus = salary * 30 / 100
    new_salary = salary + bonus
    print('Your salary with 30% added to it is $' ,new_salary)
else:# this prints out a message telling the user it's an incorrect input
    print('The salary you entered is invalid. Type in the correct one.')