# use def to define a function

def greet_user():
    print("Hello, how are you doing?")

greet_user()

# pass parameters

def greet_1(username):
    print(f"\nHello {username}, how are you?")

greet_1("Chao")

# username in greet_1() is a parameter, while "Chao" is an argument that calls the function.

# positional parameter, arguments share the same order as its corresponding parameters.

def describe_pets(animal, name):
    print(f"\nI have a {animal.lower()}")
    print(f"\nMy {animal.lower()}'s name is {name.title()}")

describe_pets("Hund", "Sherlock")

# keywords parameter

def describe_friend(name, country):
    print(f"\nI have a friend from {country}.")
    print(f"\nHis/her name is {name}.")

describe_friend(name = "Vova", country = "Russia")
describe_friend(country = "India", name = "Apurva")


