#-------------------------------------------------------------------------------
# calculate a student's average grade and outputs their grade letter
#
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------

lab_work = float(input("Please enter student's grade for the lab work: ")) #user inputs the lab work grade
midterm_test = float(input("Now enter their midterm grade: ")) #user inputs the midterm grade
final_test = float(input("Enter their final test result: ")) #user inputs the final test grade
average = (lab_work * 2 + midterm_test * 3 + final_test * 5) / 10 #calculates student's average after teacher inserts the grades
if average >= 8.0 and average <= 10: #checks if average is from 8 to 10 to output grade letter A
    print("Your student's average is", average, "and the their grade letter is A.")
elif average >= 7.0 and average < 8.0: #checks if average is from 7 to 8 to output grade letter B
    print("Your student's average is", average, "and the their grade letter is B.")
elif average >= 6.0 and average < 7.0: #checks if average is from 6 to 7 to output grade letter C
    print("Your student's average is", average, "and the their grade letter is C.")
elif average >= 5.0 and average < 6.0: #checks if average is from 5 to 6 to output grade letter D
    print("Your student's average is", average, "and the their grade letter is D.")
elif average >= 0.0 and average < 5.0: #checks if average is from 0 to 5 to output grade letter E
    print("Your student's average is", average, "and the their grade letter is E.")
else: #outputs that result below 0 or above 10 is invalid if other conditions don't run
    print("Invalid result.")