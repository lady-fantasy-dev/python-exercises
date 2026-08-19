"""
In the code example below, we choose a random element from a list
"""

import random

team = [
    "Person", "Yasmin", "Fadi", "Niko","Sare",
    "Alex", "Maria", "David", "Sarah", "John",
    "Sare", "Yasmin", "Thomas", "Fadi", "Sare",
    "Alex", "Maria", "David", "Sarah", "John"
    ]

random_person = random.choice(team)

# Alternative, longer route:
# person_index = random.randint(0, len(team)-1)
# random_person = team[person_index]

# To test it out:
print(random_person)