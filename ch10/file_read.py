with open("pi_digits.txt") as file_opened: # as 将打开文件创建一个对象（名）
    content = file_opened.read() # read()函数会读取已经打开的文件
print(content)
print(content.rstrip())

with open("pi_digits.txt") as file_pi:
    for line in file_pi:
        print(line)

with open("pi_digits.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(f"\n\t{line}")

with open("pi_digits.txt") as pi_file:
    lines = pi_file.readlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
