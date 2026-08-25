'''
Create a number-guessing game in Python.

The computer should randomly choose a secret number.

The player has 5 attempts to guess the number.

For each attempt:

Ask the player to enter a number.
If the guess is correct, tell the player they have won and end the game.
If the guess is too high, tell the player that the number is too high.
If the guess is too low, tell the player that the number is too low.

If the player does not guess the number within five attempts, tell them that they lost and reveal the correct number.

Points

The player receives points depending on which attempt they get the answer right:

Attempt	Points
1st	100
2nd	40
3rd	30
4th	20
5th	5

Add this points system to the existing game.
'''
import random

secret_number = random.randint(0, 20)
print(f"The secret number is {secret_number}")
attempt = 0

points = [[1, 100],[2, 40],[3, 30],[4, 20],[5, 5]]

while attempt < 5:
    user_input = int(input("Guess the secret number between 0 and 20. You have 5 attempts: "))
    attempt += 1

    if user_input == secret_number:
        print("You guessed right!")
        print(f"attempt no: {attempt}")
        
        for i in points:
            if i[0] == attempt:
                point = i[1]
        print(f"You got {point} points!")
        break
    
    elif user_input < secret_number:
        print("The number is too low. Try again!")
    else:
        print("The number is too high. Try again!")
else:
    print("You have no more attempts left. You lose!")
    
    