#-------------------------------------------------------------------------------
# Receives 3 numbers and outputs them in ascending order
#
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------

n1 = float(input('Enter the first of the three numbers to be entered: ')) #stores first number in memory
n2 = float(input('Enter the second one: ')) #stores second number
n3 = float(input('Enter the last number now: ')) #stores the last number
if n1 < n2 and n1 < n3: #checks if first number is bigger than the second and the third
    if n2 < n3: #checks if second number is bigger than the third
        print('The ascending order is: {:.0f} - {:.0f} - {:.0f}'.format(n1, n2, n3))
    else:
        print('The ascending order is: {:.0f} - {:.0f} - {:.0f}'.format(n1, n3, n2))
if n2 < n1 and n2 < n3: #checks if second number is bigger than the first and the third
    if n1 < n3: #checks if first number is bigger than the third
        print('The ascending order is: {:.0f} - {:.0f} - {:.0f}'.format(n2, n1, n3))
    else:
        print('The ascending order is: {:.0f} - {:.0f} - {:.0f}'.format(n2, n3, n1))
if n3 < n1 and n3 < n2: #checks if last number is bigger than the first and the second
    if n1 < n2: #checks if first number is bigger than the second
        print('The ascending order is: {:.0f} - {:.0f} - {:.0f}'.format(n3, n1, n2))
    else:
        print('The ascending order is: {:.0f} - {:.0f} - {:.0f}'.format(n3, n2, n1))
