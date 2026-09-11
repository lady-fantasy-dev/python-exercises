# Write a program to have the computer randomly select a number between 1 and 100
# Then prompt the player to guess the number.
# The program should give hints in the guess is too high or too low.

import random

def greet():
    print("Welcome to the guessing game!\nGuess the secret number.")

def generate_secret_number():
    return random.randint(1, 100)

def get_valid_guess():
    # while True to handle invalid/None output, and loop again
    while True:
        try:
            user_guess = int(input("Enter a number between 1 and 100: "))

            if 1 <= user_guess <= 100:
                return user_guess

            print(("The number should be between 1 and 100."))

        except ValueError:
            print("Please enter a valid number between 1 and 100.\nTry again...")

def play_game():
    greet()

    secret_number = generate_secret_number()

    attempts = 0

    while attempts < 5:
        user_guess = get_valid_guess()
        print("user guess inside play() is:", user_guess)
        attempts += 1

        if user_guess == secret_number:
            print("Congrats! You guessed correctly!")
            break
        elif user_guess > secret_number:
            print("Your guess was too high...")
        else:
            print("Your guess was too low...")

    print(f"Thanks for playing! You guessed {attempts} times.")

play_game()
