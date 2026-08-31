numbers = [12, 5, 8, 20, 3, 15, 7, 11, 17, 23]

# the whole list
print(numbers[:])

# first & last elements 
print(numbers[::len(numbers)-1])

# Slicing eine neue Liste mit den Elementen 5 bis 20.
new_list = numbers[5:20]
print(new_list)

# Füge die Zahl 100 hinzu
numbers.append(100)
print(numbers)

# Entferne die Zahl 8 mit remove()
numbers.remove(8)
print(numbers)

# Entferne das letzte Element
numbers.pop()
print(numbers)

# Sortiere die Liste
numbers.sort()
print(numbers)

# Drehe die Liste um
numbers.reverse()
print(numbers)

# Prüfe, ob die Zahl 20 enthalten ist
# returns boolean
print(20 in numbers)

# Erstelle eine Kopie der Liste
new_list = numbers.copy()
print(new_list)

# Durchlaufe die Liste mit einer for-Schleife
for x in numbers:
    print(x)

# Zähle, wie viele Elemente die Liste enthält
print(f"the length of the list is: {len(numbers)}")