# -------------------------------------------------------------------------------
# A program which asks user for their base salary and time they've worked, then outputs tax to be added, bonus, net salary
# and their category
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
salary = float(input("Enter your base salary: "))
time = int(input("Now enter the number of years you have worked in this company: "))
if salary < 200:
    tax = 0
elif salary <= 450:
    tax = salary * 3 / 100
elif salary < 700:
    tax = salary * 8 / 100
else:
    tax = salary * 12 / 100
print("The tax for this salary is: R${}".format(tax))
if salary > 500:
    if time <= 3:
        bonus = 20
    else:
        bonus = 30
else:
    if time <= 3:
        bonus = 23
    elif time < 6:
        bonus = 35
    else:
        bonus = 33
print("The amount for the bonus to be received is: R${}".format(bonus))
net_wages = salary - tax + bonus
print("Your net salary is: R${}".format(net_wages))
if net_wages <= 350:
    print("You are classified as A")
elif net_wages < 600:
    print("You are classified as B")
else:
    print("You are classified as C")