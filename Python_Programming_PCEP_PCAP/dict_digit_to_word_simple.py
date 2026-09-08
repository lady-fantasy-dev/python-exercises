# Write a program that propmts the user to enter a phone number
# and returns the numbers as words.

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
    for i in user_input:
            try:
                print(numbers_dict[i])
                word = numbers_dict[i]
                # print(word, end = " ")

            except KeyError:
                 raise Exception("That was not a valid number!")

user_input = input("Please enter your phone number: ")
phone_number_to_words(user_input)
