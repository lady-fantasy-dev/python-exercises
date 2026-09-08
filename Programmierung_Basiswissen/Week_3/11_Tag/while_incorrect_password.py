'''
Write a Python program that asks the user to enter a password.

The correct password is:

Spiderman_123

The user has a limited number of attempts to enter the correct password.

Keep asking for the password while the number of attempts is below the allowed limit.

If the user enters the wrong password three times, display:

"You have been locked out!"

Otherwise, if the password is correct, the user should be allowed to continue / be redirected to the website.
Use .strip() to remove unnecessary whitespace from the user's input.
'''
correct_password = "Spiderman_123"
attempts = 0

while attempts < 3:
    user_input = input("Please enter a password: ")
    attempts +=1

    if user_input.strip() == correct_password:
        print("Password is correct")
        break

    print("Incorrect! Try again: ")
    
else:  
    print("You entered the wrong password 3 times.")
        