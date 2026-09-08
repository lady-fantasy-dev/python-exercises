import random
import datetime

secret_number = random.randint(0, 20)
print(f"The secret number is {secret_number}")
attempt = 0

points = {
    1: 100,
    2: 40,
    3: 30,
    4: 20,
    5:5
    }

user_name = input("What's your name? ")

while attempt < 5:
    user_input = int(input("Guess the secret number between 0 and 20. You have 5 attempts: "))
    attempt += 1

    with open("luckyGame.txt", "a") as file:
        now = datetime.datetime.now().strftime("%d.%m.%Y at %H:%M")
        if user_input == secret_number:
            print("You guessed right!")
            print(f"attempt no: {attempt}")
            
            point = points[attempt]
            
            print(f"You got {point} points!")
            file.write(f"\nOn {now} {user_name} has won {point} points")
            break
        
        elif user_input < secret_number:
            print("The number is too low. Try again!")
            file.write(f"\nOn {now} {user_name} has guessed too low on {now}...")
        else:
            print("The number is too high. Try again!")
            file.write(f"\nOn {now} {user_name} has guessed too high on {now}...")
else:
    print("You have no more attempts left. You lose!")
    
    

