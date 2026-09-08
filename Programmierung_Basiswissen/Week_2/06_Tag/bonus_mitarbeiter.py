'''
Employee 'Johann' has been with the company for 23 years.
He receives a €2,000 bonus every 5 years.
What is the total bonus amount he has received?
 
Hello colleague, what is your first name?
How long have you been with the company? (in whole years)
You have received a total bonus of €8,000 so far.
'''

bonus_eur = 2000
bonus_freq_years = 5

employee_name = input("Hello colleague, what is your first name?\n")
employed_years = input("Nice to meet you! How long have you been with the company? (Enter number in whole years)\n")

bonus_amount_eur = (int(employed_years) // bonus_freq_years) * bonus_eur

print(f"{employee_name}, you have received a total bonus of €{bonus_amount_eur} so far.") # using str interpolation

# alternative:
# print("You have received a total bonus of ", bonus_amount_eur, "so far.")



