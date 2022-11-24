phones = ['apple', 'samsung', 'xiaomi', 'huawei', 'moto', 'nokia']
print(phones)
# 想要访问特定元素 用[index]
print(phones[0])
print(phones[1])
print(phones[2])
print(phones[3])
print(phones[4])
print(phones[5])

# 可以与string方法一起使用
message = f"I use {phones[0].title()} and {phones[2].title()}."
print(message)

#修改，添加与删除元素

#修改
phones[0] = "苹果"
print(phones)

# 添加元素

#在尾部添加 append
phones.append("OPPO")
print(phones)

# 在中间插入 insert(index,元素)
phones.insert(0,"Vivo")
print(phones)

#使用pop删除末尾元素
phones.pop()
print(phones)

#使用pop删除任意元素pop(index)
phones.pop(0)
print(phones)

#使用 sort 永久排序
phones.sort()
print(phones)
phones.sort(reverse=True)
print(phones)

# 使用 sorted临时排序
print(sorted(phones))
print(sorted(phones, reverse=True))

# 使用 reverse 反向打印列表，是永久的！
print("reverse 只是倒着打印，并不排序")
print(phones)
phones.reverse()
print(phones)

# 使用 len（）查看列表长度
print("现在列表的长度是： ")
print(len(phones))
