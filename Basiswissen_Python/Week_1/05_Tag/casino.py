def age_diff(age):
    diff = str(21 - age)

    if diff == 1:
        return "1 year"
    else:
        return diff + " years"

alter = int(input("Wie alt bist du? "))

if alter >= 21:
    print("Willkommen!")
elif alter >= 18 and alter <= 20:
    # can't concatenate strings and integers with a +
    # either interpolate with f, or as below:
    print("See you in", age_diff(alter), "!")
else:
    print("Sorry, sie dürfen nicht rein.")