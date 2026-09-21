# Write a program that prints the temperature closest to 0 among input data.
# If two numbers are equally close to zero, positive integer has to be considered closest to zero
# (for instance, if the temperatures are -5 and 5, then display 5).

# Your program must read the data from the standard input
# and write the result on the standard output.

temperature_string = "3 20 -2 5 -5 -3 -10 6"

if len(temperature_string) == 0:
    print(0)

temperatures = temperature_string.split()

closest = int(temperatures[0])

for i in temperatures:
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)


    if abs(t) < abs(closest):
        closest = t
    elif abs(t) == abs(closest):
        closest = abs(t)

print(closest)
