# Write a program to remove duplicates in a list

# Convert list to set, and then back to list
my_list = [1, 1, 2, 3, 4, 4]

my_set = set(my_list)
my_list = list(my_set)

# Alternative 1:
# Create a dictionary, using the List items as keys.
my_list = list( dict.fromkeys(my_list) )
print(my_list)

# Alternative 2:
# Loop over the list and add unique elements to a new list

uniques = []

for i in my_list:
    if i not in uniques:
        uniques.append(i)
print(uniques)
