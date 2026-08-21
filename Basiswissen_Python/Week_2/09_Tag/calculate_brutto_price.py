# Calculate the Brutto preis of products based on Mehrwertsteuer = 19%

tax = 1.19
user_netto = float(input("Enter the price of the product: "))

def calculate_brutto(netto):
    return round(netto * tax, 2)

# Test the function
print(calculate_brutto(user_netto))
