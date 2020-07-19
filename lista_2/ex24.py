# -------------------------------------------------------------------------------
# takes in 3 measurements to output if it makes an equilateral, isosceles, scalene or no triangle
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
# asks user to input 3 measures
x = float(input('Insert the first value to check if it is one to make one of the sides of triangle: '))
y = float(input('Insert the another value to be checked: '))
z = float(input('Insert the last value to be checked: '))
# checks if measures make a triangle
if x < y + z and  y < x + z and z < x + y:
# if condition above is true, checks the inputs to output the type of triangle it is
    if x == y and y == z:
        print('These measures make an equilateral triangle.')
    elif x == y or x == z or y == z:
        print('These measures make an isosceles triangle.')
    elif x != y and x != z and y != z:
        print('These measures make an scalene triangle.')
# if one of the numbers is not lower than the sum of the other two sides, it cannot be a triangle
else:
    print('These measures do not make a triangle!')