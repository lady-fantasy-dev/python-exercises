# Write a program to convert an amount of money from one currency to another using fixed exchange rates.
# The user inputs the amount and selects the currencies for conversion.

from currency_converter import CurrencyConverter
from datetime import date

c = CurrencyConverter()

user_input = float(input("Enter the amount to be converted: "))
source_currency = input("Choose a source currency: 'USD', 'EUR', or 'CAD': ")
target_currency = input("Choose a target currency: 'USD', 'EUR', or 'CAD': ")

conversion = c.convert(user_input, source_currency, target_currency, date=date(2026, 9, 14))

print(conversion)
