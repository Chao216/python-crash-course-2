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
