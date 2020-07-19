# -------------------------------------------------------------------------------
# A program which asks user for their base salary, shift they work, category and amount of hours they work. It, then,
# calculates their gross salary, tax they have to pay on it, bonus and assistance they will receive, display their
# net wages and say how well they are paid.
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
salary = float(input("Enter your minimum salary: "))
shift = str(input("What period of the day do you work? Enter M for MORNING, A for AFTERNOON or N for NIGHT: "))
category = str(input("What is your category in the company? Enter O for OPERATOR or M for MANAGER: "))
hours_worked = float(input("Enter the number of hours worked by the employee during the month: "))
if shift == "M":
    coefficient = salary * 10 / 100
elif shift == "A":
    coefficient = salary * 15 / 20
elif shift == "N":
    coefficient = salary * 20 / 100
print("The coefficient of the salary is: {}".format(coefficient))
gross_salary = hours_worked * coefficient
print("The gross salary is: {}".format(gross_salary))
if category == "O":
    if gross_salary >= 300:
        tax = gross_salary * 5 / 100
    else:
        tax = gross_salary * 3 / 100
else:
    if gross_salary >= 300: #aqui coloquei 300 porque foi o que estava escrito no enunciado. Depois verifiquei que nas instruções você colocou 400. Era aquele valor mesmo?
        tax = gross_salary * 6 / 100
    else:
        tax = gross_salary * 4 / 100
print("The tax to be paid based on the gross salary is: {}".format(tax))
if shift == "N" and hours_worked > 80:
    bonus = 50
else:
    bonus = 30
print("The bonus calculated for this employee based on their hours worked and shift is: {}".format(bonus))
if category == "O" or coefficient <= 25:
    assistance = gross_salary * 1 /3
else:
    assistance = gross_salary * 1 /2
print("The assistance you will have is: {}".format(assistance))
net_wages = gross_salary - tax + bonus + assistance
print("Your net salary is: R${}".format(net_wages))
if net_wages < 350:
    print("You are badly paid.")
elif net_wages >= 350 and net_wages <= 600:
    print("You are salary is O.K.")
else:
    print("You are well-paid")