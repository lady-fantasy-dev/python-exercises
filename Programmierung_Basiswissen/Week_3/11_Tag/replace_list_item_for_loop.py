# Create a new list in which every occurrence of 9 is replaced with 10
list_1 = [12, 7, 23, 9, 42, 17, 5, 9, 42, 17, 5]

list_2 = [10 if x == 9 else x for x in list_1]
print(list_2)

