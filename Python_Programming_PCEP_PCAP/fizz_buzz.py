# Write a function that returns "FizzBuzz" if a number is divisible by both 3 and 5,
# "Fizz" if divisible by 3, "Buzz" if divisible by 5,
# or the number itself otherwise.

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return("FizzBuzz")
    elif num % 3 == 0:
        return("Fizz")
    elif num % 5 == 0:
        return("Buzz!")
    else:
        return(num)

# Test the output:

print(fizz_buzz(15))
print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(2))
