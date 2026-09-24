# In this game, the computer comes up with a secret 4-digit number, and your job is to guess it.
# After each guess, you'll get feedback in the form of "cows" and "bulls"-a "bull" means you've guessed the right digit in the right spot,
# while a "cow" means the digit is correct but in the wrong spot.

import random

def generate_secret_number():
    return random.sample(range(10), 4)

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
        if int(user_num) in secret_number:
            if index == secret_number.index(int(user_num)):
                bull += 1
            else:
                cow += 1

    return bull, cow

def determine_win(bull, cow):
        if bull == 4:
            print("You win")
            return True
        else:
            print(f"You have {bull} bull(s) and {cow} cow(s)!")
            return False

def play_game():
    print("Welcome to the game!")
    print("I have generated a 4-digit number with unique digits. Try to guess it...")

    secret_number = generate_secret_number()

    while True:

        guess = input("Enter your guess: ")

        guess = validate_input(guess)

        bull, cow = count_bulls_cows(guess, secret_number)

        game_won = determine_win(bull, cow)

        if game_won:
            break

play_game()
