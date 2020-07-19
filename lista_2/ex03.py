#-------------------------------------------------------------------------------
# asks user's height and gender to output their ideal weight
#
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------

height = float(input("Insert your height as (M.CM): ")) # this asks the user to input their height
gender = input("Enter your gender as W for woman or M for man? ") # take in user's gender

if gender == 'M' or gender == 'm': # this checks if user is a man by checking characters in capital or lowercase letters
    ideal_weight = round((72.2 * height) - 58, 2) # calculates the ideal height for a man and rounds it down to 2 decimals (insert round before calculus, open brackets and add ", (number of decimals you want)" then close brackets
    print("Your ideal weight is: " ,ideal_weight) # outputs ideal weight
else:
    ideal_weight = round((62.1 * height) - 44.7, 2) # does calculus if first statement is false and outputs result
    print("Your ideal weight is: " ,ideal_weight)