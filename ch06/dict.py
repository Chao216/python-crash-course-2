
# python字典就是 key value pair

student_1 = {'name':'valadimir', 'age':28}

print(student_1['name'])
print(student_1['age'])

# 注意 字典需要花括号 {}， 而列表，元组是[]。

# 在字典中添加 key value pair
student_1['country'] = 'Finland'

print(student_1['country'])

# 修改字典中的值

student_1['age'] = 29

print(f"now the new age is {student_1['age']}")

# 使用get()来访问值

#如果字典中没有所查找的key，使用get()l可以避免报错。

print(student_1.get('language', 'cannot find what you are looking for !'))

# dict.get('the_key_you_search', 'optional return value if not found')

#遍历字典的键值 items()方法

for key, value in student_1.items():
    print(f"\nKey:{key}")
    print(f"\nValue:{value}")

# 访问所有key 

for key in student_1.keys():
    print(f"\n{key}")

# 访问排序过的key

for key in sorted(student_1.keys()):
    print(f"\n{key}")


# 遍历所有的值 values()

for value in student_1.values():
    print(f"\n{value}")

food = ['apple', 'apple', 'milk', 'coffee', 'coffee']

for el in set(food):
    print(f"\n{el}")

for i in range(1,10):
    print(i)

for i in range(10):
    print(i)

aliens = [] #创建一个空列表

for idx in range(100):
    new_alien = {'name':'alien', 'star':'M78', 'code':8964}
    aliens.append(new_alien)

for al in aliens[:15]:
    print(al)
    print("---------------")

print(f"\n in total, you have just created {len(aliens)} aliens.")
