#-------------------------------------------------------------------------------
# user chooses an option from menu to output numbers in ascending, descending order or put the biggest out of 3 numbers entered by user
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------

#reads variable values
A = int(input("Type in a number for A: "))
B = int(input("Type in a number for B: "))
C = int(input("Type in a number for C: "))
I = int(input("Select one of the options: ascending order (1), descending order (2) and biggest number between (3) -> "))
#conditions to check the order the numbers according to user's choice and output of those results
if I == 1:
    if A < B and A < C:
        if B < C:
            print("The ascending order of the numbers entered is: {} - {} - {}".format(A, B, C))
        else:
            print("The ascending order of the numbers entered is: {} - {} - {}".format(A, C, B))
    if B < A and B < C:
        if A < C:
            print("The ascending order of the numbers entered is: {} - {} - {}".format(B, A, C))
        else:
            print("The ascending order of the numbers entered is: {} - {} - {}".format(B, C, A))
    if C < A and C < B:
        if A < B:
            print("The ascending order of the numbers entered is: {} - {} - {}".format(C, A, B))
        else:
            print("The ascending order of the numbers entered is: {} - {} - {}".format(C, B, A))
if I == 2:
    if A > B and A > C:
        if B > C:
            print("The descending order of the numbers entered is: {} - {} - {}".format(A, B, C))
        else:
            print("The descending order of the numbers entered is: {} - {} - {}".format(A, C, B))
    if B > A and B > C:
        if A > C:
            print("The descending order of the numbers entered is: {} - {} - {}".format(B, A, C))
        else:
            print("The descending order of the numbers entered is: {} - {} - {}".format(B, C, A))
    if C > A and C > B:
        if A > B:
            print("The descending oder of the numbers entered is: {} - {} - {}".format(C, A, B))
        else:
            print("The descending oder of the numbers entered is: {} - {} - {}".format(C, B, A))
if I == 3:
    if A > B and A > C:
        print("The order requested is: {} - {} - {} ".format(B, A, C))
    if B > A and B > C:
        print("The order requested is: {} - {} - {} ".format(A, B, C))
    if C > A and C > B:
        print("The order requested is: {} - {} - {} ".format(A, C, B))
