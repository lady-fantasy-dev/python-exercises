#Create a program that takes an integer, and
#prints its multiplication table from 1 to 10.

user_input = int(input("Please enter a number: "))

for i in range(1, 11):
    print(i * user_input)