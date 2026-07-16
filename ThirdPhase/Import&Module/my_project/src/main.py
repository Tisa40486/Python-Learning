from calculations import currency, tax 

price = 250 

print(currency.format_currency(price))

x = tax.calculate_tax(price, 12)

print(currency.format_currency(x))