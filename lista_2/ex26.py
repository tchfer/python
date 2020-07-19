# -------------------------------------------------------------------------------
# outputs the weight of a product in GMs, the total price of it, tax rate, and full price of it
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
# gets user's input, transforms kgs into grams and outputs the weight of the product in grams
product_code = int(input("What is the product's code? "))
weight = float(input("What is the weight of the product? Use (K.GM) "))
country_code = int(input("Enter the country's code: "))
weight_grams = weight * 1000
print("The weight in grams is: {}".format(weight_grams))
# checks the product code to process the correct price per gram and multiplies it by the last output
if product_code >= 1 and product_code <= 4:
    price_per_gram = 10
if product_code >= 5 and product_code <= 7:
    price_per_gram = 25
if product_code >= 8 and product_code <= 10:
    price_per_gram = 35
total_price = weight_grams * price_per_gram
print("The final price of the product is: {}".format(total_price))
# checks the country code to process the tax to be added to the total amount of the product. Then it outputs the tax and
# net price of the product
if country_code == 1:
    tax = 0
if country_code == 2:
    tax = total_price * 15 / 100
if country_code == 3:
    tax = total_price * 25 / 100
print("The tax charged is: {}".format(tax))
final_price = total_price + tax
print("The net price after tax is charged is: {}".format(final_price))