dictionary = {
        'first':[1],
        'second':[2],
        'third':[1, 2, 3, 4, 5]
        }

for key, value in dictionary.items():
    print(key)
    for el in value:
        print(f"\t{el}")
