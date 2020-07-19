# -------------------------------------------------------------------------------
# user enters their minimum salary, number of hours worked, number of dependents and number of overtime
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
minimum_salary = float(input('What is the salary? '))
hours_worked = float(input('How many hours did you work? '))
dependents = int(input('How many dependents are there in your household? '))
overtime = float(input('How many hours did you work overtime ? '))
hour_rate = minimum_salary * (1 / 5)
salary_of_month = hours_worked * hour_rate
value_per_dependent = dependents * 32
overtime_rate = overtime * (hour_rate + (hour_rate * 50 / 100))
gross_salary = salary_of_month + value_per_dependent + overtime_rate
if gross_salary < 200:
    tax = 0
elif gross_salary >= 200 and gross_salary <= 500:
    tax = gross_salary * 10 / 100
elif gross_salary > 500:
    tax = gross_salary * 20 / 100
net_salary = gross_salary - tax
if net_salary <= 350:
    bonus = 100
elif net_salary > 350:
    bonus = 50
final_salary = net_salary + bonus
print('The total salary to be received is: R$ {}'.format(final_salary))