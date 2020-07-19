# -------------------------------------------------------------------------------
# takes user's wages and outputs it with all bonuses included
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
#stores value of salary
wages = float(input("What is your current salary? -> "))
if wages < 500: #checks if salary is below 500 to calculate 5% of it
    bonus: float = wages * 5 / 100
elif wages >= 500 and wages <= 1200: #checks if salary is between 501 and up to 1200 to calculate 12% of it
    bonus = wages * 12 / 100
elif wages > 1200: #checks if salary is above 1200 to store Zero bonus
        bonus = 0
if wages > 0 and wages <= 600: #this part checks if salary is above 0 and up to 600 to store a value of 150 to be added to salary
    social_welfare = 150
else: #this part checks if salary is above above 600 to add only 100 to the salary
    social_welfare = 100
print("Your salary plus bonus and social welfare R${}".format(wages + bonus + social_welfare))