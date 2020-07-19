#-------------------------------------------------------------------------------
# A program that calculates the user's BMI (body mass index)
#
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
#-------------------------------------------------------------------------------

weight = float(input("Enter your weight in (KGs) -> ")) #stores a value for the user's weight
height = float(input("Enter your height in (M.CM) -> ")) #stores a value for the user's height
bmi = round(weight / (height) ** 2, 1) #calculates BMI (body mass index)
if bmi < 18.5: #checks person BMI value to output message saying the are underweight
    print("Your BMI is", bmi, "and you are underweight.")
elif bmi >= 18.5 and  bmi < 25: #checks person BMI value to output message saying the are in the normal weight
    print("Your BMI is", bmi, "and you are in the normal weight.")
elif bmi >= 25.1 and bmi < 30: #checks person BMI value to output message saying the are overweight
    print("Your BMI is", bmi, "you are overweight.")
else: #checks person BMI value to output message saying the are obese
    print("Your BMI is", bmi, "and you are obese.")