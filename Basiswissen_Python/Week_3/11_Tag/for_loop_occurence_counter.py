# Count occurrences of a specific element in a list
# Practice Problem: Given a list of numbers, use a loop to count how many times a specific number (e.g., 10) appears.

# Given Input:
list1 = [10, 20, 10, 30, 10, 40, 50]
# target = 10

count = 0
target = 10

for num in list1:
    if num == 10:
        count += 1
print(f"Number 10 occurs {count} times in the list")
    