message = input("What is your name? ")

print(f"\n hello {message}, how are you? ")

# input() 得到的是字符串， 可以使用int()将字符串转换为整数

number = input("what is your favorite number? ")

my_num = int(number) + 6

print(f"\nmy favorite number is {my_num}")

even_num = input('please enter a even number:')
even_num = int(even_num)

if even_num % 2 == 0:
    print(f"\n {even_num} is a even number ！")
else:
    print(f"\n {even_num} is not a even number ！")
    

