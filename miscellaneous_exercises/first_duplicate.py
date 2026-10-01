# Given a list of integers, return the first number that appears for the second time.
# If no number appears more than once, return None.

duplicates_list = [4, 7, 2, 7, 9, 2, 4, 5]

seen = []
first_duplicate = None

for num in duplicates_list:
  if num in seen:
    first_duplicate = num
    break
  else:
    seen.append(num)

print(first_duplicate)
