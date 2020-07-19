#-------------------------------------------------------------------------------
# calculate a student's average grade and outputs if they have passed, failed or have to sit another test again
#
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------

lab_work = float(input("Please enter student's grade for the lab work: ")) #user inputs the lab work grade
midterm_test = float(input("Now enter their midterm grade: ")) #user inputs the midterm grade
final_test = float(input("Enter their final test result: ")) #user inputs the final test grade
average = (lab_work + midterm_test + final_test) / 3 #calculates the average student got
if average >= 7.0 and average <= 10: #checks first condition and prints out they have passed
    print("You have passed. Congratulations! ")
elif average >= 3.0 and average < 7.0: #checks if they got a grade from 3 to 7 to calculate how much they need to get for the new test in order to pass
    print("You have to sit another test.")
    new_grade = 12 - average
    print("You have to get {}".format(new_grade),"in your new test to pass.") #.format(variable_name) is the new print command in python 3
elif average >= 0 and average < 3: # if they get less than 0, it prints a message saying that they have failed
    print("You have failed.")