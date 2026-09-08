'''
The examples below show the distinction between printing different values using concatenation with +
and printing different values using ,

+ is for combining values and string concatenation, and requires compatible types; otherwise TypeError
The result in ONE string which you could manipulate with .upper() for example

, is not for concatenating strings, but here we are giving print() two separate arguments to display.
Internally, they're still two separate values - not concatenated.

print("Hello", 123, sep="---") => Hello---123 
'''

# Combining strings and numbers
x = "Hello"
y = 123

print(x, y)
# Hello 123

print(x + str(y))
# Hello123

print(x + " " + str(y))
# Hello 123

print(5 + 10) # 15
# not string concatenation, but addition

print(5, 10) # 5 10
