# Write a program that simulates rolling a pair of dice. Each time the program runs,
# it should randomly generate two numbers between 1 and 6 (inclusive),
# representing the result of each die.
# The program should then display the results and ask if the user would like to roll again.

# Optional Enhancements
# • Modify the program so the user can specify how many dice they want to roll.
# • Add a feature that keeps track of how many times the user has rolled the dice
# during the session. This will require a counter that increments each time the
# dice are rolled.

import random

def greet():
    print("Welcome to the game!")

# def roll_dice():
#     num1 = random.randint(1, 6)
#     num2 = random.randint(1, 6)
#     return num1, num2

# Modify the program so the user can specify how many dice they want to roll.
def roll_dice():
    number_of_dice = int(input("How many dice between 1 and 6 would you like to roll? "))
    if number_of_dice < 1 or number_of_dice > 6:
        raise ValueError("Please enter a number between 1 and 6.")
    else:
        return [random.randint(1, 6) for _ in range(number_of_dice)]

def ask_play_again():
    while True:
        user_input = input("Would you like to play again? ").lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Please enter y or n: ")

def raise_exception():
    raise ValueError("Please enter a valid response...")

def play_game():
    greet()
    times_played = 0

    while True:
            dice = roll_dice()
            times_played += 1

            print("You got the following two numbers on the dice:", *dice)
            print("You have played", times_played, "time(s)")

            if not ask_play_again():
                print("Thanks for playing!")
                break

play_game()
