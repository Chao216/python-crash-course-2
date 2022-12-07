#! /usr/bin/env python3

# join a list

list1 = ["hello", "where", "are", "you", 'from']

str1 = ' % '

longStr1 = str1.join(list1)

print(longStr1)

# the general pattern for joining a string list is 'string_sep'.join(list_name)

# join a tuple 

tuple1 = ("Hallo", "wei", "heissen", "Sie", "?")

str2 = ' ,'

longStr2 = str2.join(tuple1)

print(longStr2)

# join a set

set1 = {"Nespresso", 'makes', "good", "coffee","!"}

str3 = " + "

longStr3 = str3.join(set1)

print(longStr3)

# join a dictionary

dict1 = {"name":"chao", "age":25, "edu level":"Master", "height":173, "weight":70}

# you don't have to pre-define the spring for seperation

longStr5 = " # ".join(dict1)

print(longStr5)
