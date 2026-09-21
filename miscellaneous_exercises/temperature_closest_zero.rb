# Write a program that prints the temperature closest to 0 among input data.
# If two numbers are equally close to zero, positive integer has to be considered closest to zero
# (for instance, if the temperatures are -5 and 5, then display 5).

# Your program must read the data from the standard input
# and write the result on the standard output.

# Do the exercise in Ruby
temperature_string = "3 20 -2 5 -5 -3 -10 6 -1 1"

if temperature_string.size == 0
  print 0
end


temperatures = temperature_string.split

closest = temperatures[0].to_i

temperatures.each do |temperature|
  temperature = temperature.to_i

  if temperature.abs < closest.abs
    closest = temperature
  elsif temperature.abs == closest.abs
    closest = temperature.abs
  end
end
