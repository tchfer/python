# -------------------------------------------------------------------------------
# A program which takes in how many tons a lorry is carrying, checks where it came from,
# calculates tax based on which location it comes from, and outputs the total being carried, load total and tax
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
# gets user's input, transforms tons into kgs and outputs the weight of the product in kgs
state_code = int(input("Enter the State's code: "))
weight_in_tons = float(input("What is the weight the lorry is carrying? Write the weight in tons: "))
load_code = int(input("What is the code of the lorry's load? "))
weight_in_kgs = weight_in_tons * 1000
print("The weight in kilos is: {}".format(weight_in_kgs))
# checks the load code to process the correct price of the load
if load_code >= 10 and load_code <= 20:
    load_price = 100 * weight_in_kgs
if load_code >= 21 and load_code <= 30:
    load_price = 250 * weight_in_kgs
if load_code >= 31 and load_code <= 40:
    load_price = 340 * weight_in_kgs
print("The price for the load is: {}".format(load_price))
# checks the state code to process the tax to be added to the total amount of the load. Then it outputs the tax and
# net price of the load after tax is added to it
if state_code == 1:
    tax = load_price * 35 / 100
if state_code == 2:
    tax = load_price * 25 / 100
if state_code == 3:
    tax = load_price * 15 / 100
if state_code == 4:
    tax = load_price * 5 / 100
if state_code == 5:
    tax = 0
print("The tax charged is: {}".format(tax))
final_price = load_price + tax
print("The net price of the load after tax is charged is: {}".format(final_price))