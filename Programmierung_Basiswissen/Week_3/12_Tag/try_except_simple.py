try:
    user_input = int(input("Enter a valid number: "))

    print(f"Ihre Zahl ist: {user_input}") 
except ValueError:
    print("Something went wrong")

print("Continuing the program...")