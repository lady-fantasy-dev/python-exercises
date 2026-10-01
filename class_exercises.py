# Create a class called Dog with no attributes or methods.
# Then create an instance of the class and store it in a variable called my_dog.

class Dog:
  pass

my_dog = Dog()
print(my_dog)

# The Constructor __init__
# Create a class called Person.
# Its constructor should take name and age as parameters and store them as instance attributes.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

shadow = Person("Shadow", 13)
print(shadow)

# Create a class called Greeter.
#  It should have a name attribute, set through __init__.
#  Add a method called greet().
#  The method should return the string: Hello, <name>!

class Greeter:

  def __init__(self, name):
    self.name = name

  def greet(self):
    return(f"Hello, {self.name}!")

yasmine = Greeter("Yasmine")
print(yasmine.greet())

# Methods That Change State
# Create a class called Counter.
# * The counter should start at 0.
# * Store the current value in an attribute called value.
# * Add an increment() method that increases value by 1.
# * Add a reset() method that sets value back to 0.

class Counter:
  counter = 0
  # value = 

  def __init__(self, value):
    self.value = value

  def increment(value):
    value += 1
    return value

  def reset(value):
    value = 0
    return value

my_value = Counter.increment(2)
print(my_value)

# Default Parameter Values
# Create a class called Rectangle with width and height.
# * height should default to the same value as width if no height is provided.
# * Therefore, Rectangle(4) should represent a 4 × 4 square.
# * Add an area() method.
# * Add a perimeter() method.

class Rectangle:
  def __init__(self, width, height):
    if height == None:
      height = width

  def area(width, height):
    return width * height

  def perimeter(width, height):
    return width + height

my_rectangle = Rectangle.area(4,6)
print(my_rectangle)

# The __str__ Method
# Create a class called Book with:
# * title
# * author
# Implement __str__() so that it returns "<title>" by <author>

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

# Returns a string that represents the object in a human-readable format
  def __str__(self):
    return f"{self.title} by {self.author}"

my_book = Book("Gone with the Wind", "Margaret Mitchell")
print(my_book)


# Class Attributes vs. Instance Attributes
# Create a class called Car. It should have:
# * A class attribute wheels with the value 4.
# * An instance attribute brand.
# * A class attribute count that starts at 0.
# * Every time a new Car object is created, count should increase by 1.

class Car:
  wheels = 4
  count = 0

  def __init__(self, brand):
    self.brand = brand
    Car.count += 1

car1 = Car("Opel")
car2 = Car("Audi")
print(car1.brand)
print(Car.wheels)
print(Car.count)
