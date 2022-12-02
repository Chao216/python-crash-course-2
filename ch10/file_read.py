with open("pi_digits.txt") as file_opened: # as 将打开文件创建一个对象（名）
    content = file_opened.read() # read()函数会读取已经打开的文件
print(content)
print(content.rstrip())


