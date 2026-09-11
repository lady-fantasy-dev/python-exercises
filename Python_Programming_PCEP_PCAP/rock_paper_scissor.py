import random
# Write a program to simulate a game of Rock, Paper, Scissors.

# Greet user
# in a dict => map "r", "p", "s" to emojis
# prompt user to choose "r", "p", "s"
# select randomly using random.choice()
# diplay both choices using emojis
# determine who wins
# ask whether to continue (y/n)

choices = {
    "r": "🪨",
    "p": "📄",
    "s": "✂️"
}

def generate_computer_choice():
    return random.choice(list(choices))

def get_user_choice():
    while True:
        choice = input("Please enter 'r', 'p', or 's': ")

        if choice in choices:
                return choice

        print("You can only enter 'r', 'p', or 's'. Try again...")

def ask_to_continue():
    while True:
        answer = input("Do you want to continue? y/n: ")

        if answer == "y":
            return True
        if answer == "n":
            return False

        print("Please enter 'y' or 'n'.")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "p" and computer_choice == "r")
        or (user_choice == "s" and computer_choice == "p")
    ):
        return "win"

    return "lose"



def play_game():
    print("Welcome to the game of Rock, Paper, Scissors!")

    attempts = 0

    while attempts < 3:
        user_choice = get_user_choice()
        print("You chose:", choices[user_choice])

        computer_choice = generate_computer_choice()
        print("The computer chose:", choices[computer_choice])

        attempts += 1
        print("attempts:", attempts)

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("Tie!")
        elif result == "win":
            print("You win!")
        else:
            print("The computer wins!")

        if not ask_to_continue():
            print("Thanks for playing!")
            break
    else:
        print("Maximum number of rounds reached.")

play_game()
