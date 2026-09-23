# create a variable named capitalized_fruits
# and use list comprehension syntax to produce output like
# ['Mango', 'Kiwi', 'Strawberry', etc...]

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

# Make a list that contains fruits that have less than 5 characters
new_list = [fruit for fruit in fruits if len(fruit) < 5]

# Make a variable named odd_negative_numbers
# that contains only the numbers that are both odd and negative.
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

odd_negative_numbers = [number for number in numbers if number % 2 != 0 and number < 0]
