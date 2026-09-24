# In this game, the computer comes up with a secret 4-digit number, and your job is to guess it.
# After each guess, you'll get feedback in the form of "cows" and "bulls"-a "bull" means you've guessed the right digit in the right spot,
# while a "cow" means the digit is correct but in the wrong spot.

import random

def generate_secret_number():
    return(random.sample(range(0,10), 4))

def validate_input(guess):
    while True:
        if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
            return guess

        print("Invalid input... You must enter 4 unique digits")
        guess = input("Try again: ")


def count_bulls_cows(guess, secret_number):
    bull = 0
    cow = 0

    for index, user_num in enumerate(guess):
        print("index in for loop:", index)
        print("user num in for loop:", user_num)

        if int(user_num) in secret_number:
            if index == secret_number.index(int(user_num)):
                bull += 1
                print("bull:", bull)
            else:
                cow += 1
                print("cow:", cow)

    print("bull and cow outside loop:", bull, cow)
    return(bull, cow)

def determine_win(bull, cow):
        if bull == 4:
            print("You win")
        # what to return?
        else:
            print(f"You have {bull} bull(s) and {cow} cow(s)!")

def play_game():
    print("Welcome to the game!")

    secret_number = generate_secret_number()
    print("secret number:", secret_number)

    guess = input("I have generated a 4-digit number with unique digits. Try to guess it: ")

    guess = validate_input(guess)

    bull, cow = count_bulls_cows(guess, secret_number)
    print("line 57:", bull, cow)

    determine_win(bull, cow)


play_game()
