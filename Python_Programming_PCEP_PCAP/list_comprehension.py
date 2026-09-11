[5, 6, 6, 7]
[32.0, 68.0, 86.0, 98.6]
['orange', 'banana', 'coconut']


# Given this list, create a new list with the length of each word.
# Expected output: [5, 6, 6, 8]

fruits = ["apple", "orange", "banana", "coconut"]
fruit_lengths = [len(fruit) for fruit in fruits]
print(fruit_lengths)

# Create a list where every temperature in Celsius is converted to Fahrenheit.
# Formula: F = C * 9/5 + 32
# Expected output: [32.0, 68.0, 86.0, 98.6]

celsius = [0, 20, 30, 37]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print(fahrenheit)


# Create a list containing only the fruits whose name has more than 5 characters.
# Expected output: ['orange', 'banana', 'coconut']

fruits = ["apple", "orange", "banana", "coconut"]
long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print(long_fruits)
