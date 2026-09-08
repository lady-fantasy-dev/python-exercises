# Create a new list in which every occurrence of 9 is replaced with 10

# alternative solution using .append()

list_1 = [12, 7, 23, 9, 42, 17, 5, 9, 42, 17, 5]

list_2 = []

for x in list_1:
    if x == 9:
        list_2.append(10)
    else:
        list_2.append(x)
        
print(list_2)


