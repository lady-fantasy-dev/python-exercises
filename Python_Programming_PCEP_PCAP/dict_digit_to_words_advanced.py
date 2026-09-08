# Write a program that propmts the user to enter a phone number
# and returns the numbers as words.

user_input = input("Please enter your phone number: ")

numbers_dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

def phone_number_to_words(user_input):
    result = []

    for digit in user_input:
            # if digit == numbers_dict[digit]:
        result.append(numbers_dict[digit])
    return " ".join(result)

# Test the function
print(phone_number_to_words(user_input))
