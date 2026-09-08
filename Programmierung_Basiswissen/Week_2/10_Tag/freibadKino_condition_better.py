'''
Exercise: Weather Decision

Write a Python program that decides whether we should go to the outdoor swimming pool or the cinema.

Ask the user for the current temperature.
If the temperature is below 25°C, go to the cinema. Do not ask about rain.
If the temperature is 25°C or higher, ask whether it is raining.
If it is raining, go to the cinema.
If it is not raining, go to the outdoor swimming pool.

Requirements:

Use an integer or float variable for the temperature.
Use a Boolean variable for rain (True or False).
'''
temperature = int(input("Please enter today's temperature? "))

if temperature < 25:
    print("We are going to the cinema.")
else:
    rain = input("Is it raining? Enter yes/no ").strip().lower() == "yes"

    if rain:
        print("We are going to the cinema.")
    else:
        print("We are going to the beach!")


