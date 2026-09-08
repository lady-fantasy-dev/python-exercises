string = "Spiderman"

count = 0

for char in string:
    count += 1
    if string[0] == char:
        print(f"{count}. Buchstabe = {char.upper()}")
    else:
        print(f"{count}. Buchstabe = {char}")
