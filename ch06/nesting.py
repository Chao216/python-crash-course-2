# list in dictionary
dictionary = {
        'first':[1],
        'second':[2],
        'third':[1, 2, 3, 4, 5]
        }

for key, value in dictionary.items():
    print(key)
    for el in value:
        print(f"\t{el}")

# dictionary in dictionary

drink_order = {
        'chao':{'drink':'espresso', 'unit':2, 'serving':'hot'},
        'vova':{'drink':'green tea', 'unit':1, 'serving':'hot'},
        'apurva':{'drink':'masala chai', 'unit':1, 'serving':'hot'}
        }

for people, drinks in drink_order.items():
    print(f"\n{people}")
    print(f"\t{drinks['drink']}")
    print(f"\t{drinks['unit']}")
    print(f"\t{drinks['serving']}")
    print('\n let us use a smart way to print !')
    for key in drinks.keys():
        print(f"\n\t{drinks[key]}")
