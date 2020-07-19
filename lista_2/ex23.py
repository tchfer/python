# -------------------------------------------------------------------------------
# 2nd degree equation
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
# this is a library which imports the square root command so we do not have to put delta to the power of (1/2)
from math import sqrt
# reads users input for first number to be inserted and if it's 0, stops and tells user value has to be another
a = int(input('Inser a real number for A: '))
if a == 0:
    print('First value cannot be 0 for equation to be a second degree one!')
# checks conditions to output one of the three results
else:
    b = int(input('Inser a real number for B: '))
    c = int(input('Inser a real number for C: '))
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print('There is no real root!')
    elif delta == 0:
        print('There is real root!')
        x1 = (-b) / (2 * a)
    elif delta > 0:
        print('There are two real roots!')
        x1 = (-b) + sqrt(delta) / (2 * a)
        x2 = (-b) - sqrt(delta) / (2 * a)
        print('The real roots are: {:.2f} and {:.2f}'.format(x1, x2))