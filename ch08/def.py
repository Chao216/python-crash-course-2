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

# defalut values for parameter

def describe_weather(city = "Shanghai", weather='GOOD'):
    print(f"\nThe weather in {city} is {weather.lower()} today.")

describe_weather(weather = "Sunny")

# return value in function

def format_name(firstname, lastname):
    full_name = f"{firstname.title()} {lastname.title()}"
    return full_name

me = format_name("CHAO", "jiang")

print(me)

# pass list into function

def greeting_people(names):
    for name in names:
        print(f"\nHello {name}, wlecome to the party !")

guests = ["Tony", "Lam", "Egor", "Harry", "Tom"]

greeting_people(guests)



# 传递任意数量的实参，*

def confirm_drinks(*drinks):
    for drink in drinks:
        print(f"\n\tyou have ordered {drink}")

confirm_drinks("cola", "rum", "wine", "coffee")

# 传递任意数量的关键词实参 **

def user_profile(first, last, **user_info):## ** 创建空字典
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

chao = user_profile(["chao"], ['jiang'], country=["China"], languages=['Chinese', 'English', 'German'])

for keys, values in chao.items():
    print(keys)
    for value in values:
        print(f"\n\t{value}")
