#-------------------------------------------------------------------------------
# tell a user the credit they have available according to their average balance
#
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------

average_balance = float(input('Insert the average balance you have had in the last year: ')) #takes a user's balance for the past year
if average_balance >= 0 and average_balance <= 200: #checks if balance ranges from 0 to 200
    print('You do not have any credit available. ') #prints that there is no credit available
elif average_balance > 200 and average_balance <= 400: #checks if balance ranges from 201 to 400
    credit_available = average_balance * 20 / 100 #calculates 20% of the value entered by user
    print('Your average balance in the last year is ', average_balance, 'and the credit available to you now is:', credit_available) #if condition is true, it calculates 20% and outputs message
elif average_balance > 400 and average_balance <= 600: #checks if balance ranges from 401 to 600
    credit_available = average_balance * 30 / 100 #calculates 30% of the value entered by user
    print('Your average balance in the last year is ', average_balance, 'and the credit available to you now is:', credit_available) #if condition is true, it calculates 30% and outputs message
elif average_balance > 600: #checks if balance is higher than 600
    credit_available = average_balance * 40 / 100 #calculates 40% of the value entered by user
    print('Your average balance in the last year is $', average_balance, 'and the credit available to you now is $:', credit_available) #if condition is true, it calculates 40% and outputs message
else:
    print('Your balance has been negative for the past year. You have no credit available.') #if none of the conditions are true, value entered is negative, it outputs that their balance has been negative