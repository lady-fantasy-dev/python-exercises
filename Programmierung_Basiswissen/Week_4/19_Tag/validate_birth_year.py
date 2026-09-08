# Write a function that validates a birth year.
#
# The function receives the birth year as a STRING.
#
# The input is valid only if:
# - It contains exactly 4 digits.
# - It is not a negative number.
# - The resulting age is plausible.
# - The person is at least 12 years old.
#
# If the input is valid, return the birth year as an INTEGER.
# Otherwise, raise a ValueError with an appropriate error message.
#
# Example:
# "2000" → 2000
# "123" → ValueError
# "-2000" → ValueError
# "2020" → ValueError (age is less than 12)

import datetime

def validate_birth_year(birth_year):
    this_year = datetime.datetime.now().year

    if len(birth_year) != 4:
        raise ValueError("Falsche Eingabe: enter only 4 digits")
    elif int(birth_year) > this_year:
        raise ValueError("Birth year cannot be in the future.")
    elif 100 > int(birth_year) > 12:
        raise ValueError("Birth year should be plausible.")
    else:
        print(int(birth_year))

user_input = input("Geben Sie Ihr Geburtsjahr ein: ").strip()

validate_birth_year(user_input)
    