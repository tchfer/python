#-------------------------------------------------------------------------------
# check if a number is even, odd and positive or negative
#
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------

num = int(input('Type in a whole number -> ')) # takes in the number user wants to enter

result = num % 2 # returns remainder of the division

if result == 0 and num > 0: # checks if the number is even and higher than 0, then outputs the message if it's true
    print('The number you typed in is even and positive.')
elif result == 0 and num < 0: # checks if the number is even and lower than 0, then outputs the message if it's true
    print('The number you typed in is even and negative.')
elif num > 0: # checks if the number is higher than 0 to output that it's positive and even if condition is true
    print('The number you typed in is odd and positive.')
elif num < 0: # checks if the number is lower than 0 to output that it's positive and even if condition is true
    print('The number you typed in is odd and negative.')
else: # checks if none of the above is true and outputs that zero is a null number if the others are false
    print('Zero is a neutral number!')