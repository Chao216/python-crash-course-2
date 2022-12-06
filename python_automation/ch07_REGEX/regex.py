# 首先引入 re模块

import re

phone_num = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d') # phone_num 是用re.compile 创建的一个正则对象

num1 = phone_num.search("my phone number is 123-4567-8901") #使用正则对象内的serach 查找被inspect 目标

print(f"\nthe number found with regex is {num1.group()}") # ！！！ 查到的结果使用group() 方法显示全部

# 使用括号分组

#括号顺序决定分组顺序，0 或 空白 表示全部分组

tel_num = re.compile(r'(\d\d\d\d)-(\d\d\d\d\d\d\d\d)')

tel1 = tel_num.search("the number is 0573-88765432")

print(f'\nwe have get the number {tel1.group()} ')
print(f'\nthe first group is {tel1.group(1)}')
print(f'\nthe second group is {tel1.group(2)}')
print(f'\nthe 2 group is {tel1.group(0)}')
print(f'\nthe 2 group is {tel1.group()}')

# 使用管道匹配多个分组  |

weather = re.compile(r"sunny|rainy")

weather1 = weather.search("the weather is rainy")
weather2 = weather.search("the weather is sunny")

print(weather1.group())
print(weather2.group())

# ?匹配零次或者一次

zeroOne = re.compile(r'super(wo)?man')

zeroOne1 = zeroOne.search("superman")
zeroOne2 = zeroOne.search("superwoman")
print(zeroOne1.group())
print(zeroOne2.group())
