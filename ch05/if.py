cars = ['Audo', "Mercedez", 'Volkswagen', 'Ford', 'BYD', 'Tesla']

for car in cars:
    if car == 'Mercedez':
        print(car.upper())
    else:
        print(car.lower())

# 判断是否相等用==
# 判断是否不相等!=

print(23==23.0)
print(23!=23.0)

# 判断多个条件 and, or

a = True
b = False

print (a and b)

print (a or b)

# 判断一个值是否存在 in, not in

list1 = ['apple', 'water', 'coffee', 'tea' ]

if 'sugar' not in list1:
    print("sugar is not in list")

if 'water' in list1:
    print("water is in the list")


# if-else

age = 25 

if age >= 18:
    print("adult")
else:
    print("minor")


# if-elif-else

if age > 0 and age < 7:
    print("kid")
elif age >= 7 and age < 18:
    print("teen")
elif age >= 18 and age < 60:
    print("work hard")
elif age >= 60:
    print("enjoy your life")
else:
    print("are you a human-being? ")
