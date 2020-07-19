#-------------------------------------------------------------------------------
# Receives 3 numbers that are inserted in ascending order and 4th one that doesn't apply the rule,
# output these numbers in descending order
#
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------

n1 = float(input("Type in a number -> ")) #stores first number
n2 = float(input("Now insert a number that is bigger than the last one -> ")) #stores second number
if n2 > n1: #checks if the first number is smaller than the second one to proceed
    n3 = float(input("Insert another number which is bigger than the previous two -> ")) #if last step is true, it runs this part
    if n3 > n2: #checks if third number is bigger than the second one to proceed to last input step
        n4 = float(input("Insert any number of your choice -> ")) #if all other conditions are true, it stores value for 4th number
        if n4 > n3: #checks if 4th number is bigger than 3rd to output result
            print("The descending order is: {:.0f} - {:.0f} - {:.0f} - {:.0f}".format(n4, n3, n2, n1))
        elif n4 > n2 and n4 < n3: #checks if 4th number is bigger than the 2nd and if it's smaller than the 3rd to output result
            print("The descending order is: {:.0f} - {:.0f} - {:.0f} - {:.0f}".format(n3, n4, n2, n1))
        elif n4 > n1 and n4 < n2: #checks if 4th number is bigger than the 1st and if it's smaller than the 2nd to output result
            print("The descending order is: {:.0f} - {:.0f} - {:.0f} - {:.0f}".format(n3, n2, n4, n1))
        elif n4 < n1: #checks if 4th number is snaller than the 1st entered
            print("The descending order is: {:.0f} - {:.0f} - {:.0f} - {:.0f}".format(n3, n2, n1, n4))
        elif n4 == n1 or n4 == n2 or n4 == n3: #checks if values for the 4th number is equal to any of the others entered so that it ends program with a message that user has to enter a bigger number
            print("This number cannot be equal to the ones previously typed!")
    else:
        print("This number has to be a bigger number than the previous one!") # if n3 isn't bigger than n2, run this
else:
    print("This number has to be bigger than the previous one!") #if n2 isn't bigger than n1, run this instead