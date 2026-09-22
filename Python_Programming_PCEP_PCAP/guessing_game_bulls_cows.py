# In this game, the computer comes up with a secret 4-digit number, and your job is to guess it.
# After each guess, you'll get feedback in the form of "cows" and "bulls"-a "bull" means you've guessed the right digit in the right spot,
# while a "cow" means the digit is correct but in the wrong spot.

import random

print("Welcome to the game!")

secret_number = random.sample(range(0,10), 4)
print("secret number:", secret_number)

while True:
    guess = input("I have generated a 4-digit number with unique digits. Try to guess it: ")

# Validate guess

# check if digits are only 4 and unique
# if len(guess) == 4:
#     seen = []
#     for char in guess:
#         if char.isdigit() and char not in seen:
#             seen.append(char)
#         else:
#             print("Only unique digits are accepted...")
#     print("char seen", seen)

# else:
#     print("Please enter 4 unique digits!")

    bull = 0
    cow = 0


    for user_num in guess:
        if int(user_num) in secret_number:
            print(guess.index(user_num))
            print(secret_number.index(int(user_num)))
            if guess.index(user_num) == secret_number.index(user_num):
                bull += 1
                print("bull:", bull)
            else:
                cow += 1
                print("cow:", cow)

    if bull == 4:
        break
    else:
        print(f"You have {bull} bulls and {cow} cows!")
