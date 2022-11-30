# 使用while 添加字典信息

dictionary = {} #先定义一个空字典

adding = True

while adding:
    word = input('please enter a word')
    meaning = input('please enter its meaning')

    dictionary[word] = meaning

    confirm = input("do you want to keep adding new word? yes/no")

    if confirm == "no":
        adding = False

print(f"\n-----We have a new dictionar-----")
for word, meaning in dictionary.items():
    print(f"\n{word}")
    print(f"\n :{meaning}")
