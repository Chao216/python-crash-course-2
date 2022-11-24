#使用range()

for num in range(1,1000):
    print(num)
print("I love you ! always forever !")

for num in range(1,3001):
    print(f"I love you {num}")

#使用range(), list() 常见数字数列

list1 = list(range(1,3001))
print(list1)

# 为range()添加间隔

list2 = list(range(1, 3001, 50))
print(list2)

#简单的统计

print(max(list2))

print(min(list2))
print(sum(list2))

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

#简单切片
print(alphabet[0:3])

print(alphabet[3:5])
print(alphabet[5:8])
print(alphabet[8:10])

#遍历切片

for letter in alphabet[2:10]:
    print(f"the letter is {letter}\n")

#复制列表

my_food = ['milk','coffee','meat']
friend_food = my_food[:]
print("my food:")
print(my_food)
print("friends food")
print(friend_food)

friend_food.append("apple")
print("my frinds new food")
print(friend_food)
print("my food")
print(my_food)
