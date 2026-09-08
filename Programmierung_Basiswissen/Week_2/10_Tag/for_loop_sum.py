# Write a program that accepts a number from the user
# and calculates the sum of all numbers from 1 up to that number.

user_input = int(input("Please enter a number: "))
s = 0

for i in range(1, user_input+1):
    s += i
print(f"The sum is {s}")
