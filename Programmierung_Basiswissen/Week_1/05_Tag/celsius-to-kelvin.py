def celsius_to_kelvin(user_input):
    return float(user_input) + 273.15


user_input = input("What temperature in Celsius would you like to convert to Kelvin? ")

print("The temperature in Kelvin is", celsius_to_kelvin(user_input))


'''
alternative (more basic) solution

user_input = input("What temperature in Celsius would you like to convert to Kelvin? ")

print("The temperature in Kelvin is", float(user_input) + 273.15)

'''
