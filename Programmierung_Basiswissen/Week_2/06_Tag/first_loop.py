import random

lucky_number = random.randint(1, 13)

print("Please enter a number between 1 and 13 to guess the lucky number.")

attempt = 0
# if attempt is set to 1, then the while condition shouldbe < 4

while attempt < 3: # 0, 1, 2
    user_input = int(input("Your guess: "))

    attempt += 1
    
    if user_input < 1 or user_input > 13:
        print("Only numbers between 1 and 13 are accepted")
        
    if lucky_number == user_input :
        print("Du bist ein Glückspilz!")
        break
else:
    print("Sorry, try again...") # print this only once at the end if the player loses
        