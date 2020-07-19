# -------------------------------------------------------------------------------
# takes in person's weight and height to output a category they're in
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
# stores information user inserts
height = float(input("Enter person's height here in the following format: (M.CM) -> "))
weight = float(input("Enter person's weight here in the following format: (K.GM) -> "))
# checks conditions to output the correct categorization according to user's inputs
if height < 1.2:
    if weight <= 60:
        print('You are in category A')
    elif weight > 60 and weight <= 90:
        print('You are in category D')
    elif weight > 90:
        print('You are in category G')
elif height >= 1.2 and height <= 1.7:
    if weight <= 60:
        print('You are in category B')
    elif weight > 60 and weight <= 90:
        print('You are in category E')
    elif weight > 90:
        print('You are in category H')
elif height > 1.7:
    if weight <= 60:
        print('You are in category C')
    elif weight > 60 and weight <= 90:
        print('You are in category F')
    elif weight > 90:
        print('You are in category I')