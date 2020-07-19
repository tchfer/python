# -------------------------------------------------------------------------------
# a program which checks a product's price, average month sale and calculates a new value for it
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
# asks user to input the the current price and the number of sales for the month
current_price = float(input('What is the current price of the product? '))
average_sale = int(input('What was the average sales number for this product: '))
#checks conditions to calculate the new price
if average_sale < 500 or current_price < 30:
    new_price = current_price + (current_price * 10 / 100)
elif average_sale >= 500 and average_sale < 1200 or current_price >= 30 and current_price < 80:
    new_price = current_price + (current_price * 15 / 100)
elif average_sale >= 1200 or current_price >= 80:
    new_price = current_price - (current_price * 20 / 100)
# outputs the new price for the product
print('The new price for the product is: R${}'.format(new_price))