# -------------------------------------------------------------------------------
# A program which asks user for the price of a product, the type of it and it needs refrigerating. It outputs
# added value, tax, discount, new price and if it is considered expensive or not
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
price = float(input("Enter product price: "))
type = input("Enter one of the letters to represent the product's category: A for ATTIRE, C for CLEANING or F for FOOD -> ")
refrigeration = input("Does the product need refrigeration? Type Y for YES or N for NO. -> ")
if refrigeration == "N":
    if type == "F":
        if price < 15:
            added_value = 2
        else:
            added_value = 5
    if type == "C":
        if price < 10:
            added_value = 1.5
        else:
            added_value = 2.5
    if type == "A":
        if price < 30:
            added_value = 3
        else:
            added_value = 2.5
elif type == "F":
    added_value = 8
    if type == "C":
        added_value = 0
    if type == "A":
        added_value = 0
print("Added value to the product is: R${}".format(added_value))
if price < 25:
    tax = price * 5 / 100
else:
    tax = price * 8 / 100
print("The value of tax is: R${}".format(tax))
at_cost = price + tax
print("The product at cost is: R${}".format(at_cost))
if type != "F" and refrigeration != "Y":
    discount = at_cost * 3 / 100
else:
    discount = 0
new_price = at_cost + added_value - discount
print("The new price for the pruduct is: R${}".format(new_price))
if new_price <= 50:
    print("The item is cheap! ")
elif new_price < 100:
    print("The price of the product is reasonable! ")
else:
    print("The item is a rip-off")