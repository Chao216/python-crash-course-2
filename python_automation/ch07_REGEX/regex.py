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

# 你也可以用 * 零次或多次， + 一次或多次
print("* 零次或多次 + 一次或多次")

# 使用花括号 匹配特定数量
print("使用{m,}匹配至少m次")
print("使用{,n}匹配至多m次")
print("使用{m,n}匹配m 到 n次")

# ?也可以用来表示非贪心匹配

non_greedy = re.compile(r'(ho){3,5}?') #非贪心匹配

ng1 = non_greedy.search("hhdfuhhohohodfdshohohohohohohohfdsf")

print(ng1.group())

# search() 默认返回找到的第一个结果， findall() 会返回所有发现结果，以列表呈现

# 再次使用之前定义的tel_num 正则对象

many_tel = tel_num.findall("the possible numbers are 0987-87654677, 3421-09876789, 4343-67564534")

for number in many_tel:
    print(number)

# ^开头， $结尾 [abcdeABCED] 属于之一， [^abcdeABCDE] 不属于任何一个
print(" ^开头， $结尾 [abcdeABCED] 属于之一， [^abcdeABCDE] 不属于任何一个")

# 通配字符 . 可以用来匹配除了换行\n 外所有字符

cap_any = re.compile(r'.at')

res_any = cap_any.findall('hat, batman, hoat, oat, mattress, chat')

for res in res_any:
    print(res)

# 可以结合 * AND . 匹配任意文本， 除了换行符\n

print(".* 可以匹配任意字符0个或多个， 除了换行\\n")

# 使用.DOTALL 匹配任意字符，包括换行\n
# re.DOTALL 记得要放在re.compile()的第二个argument里
newLine = re.compile(r".*", re.DOTALL)

newLine1 = newLine.search("hello mr potter. \n how are you doing? ")
print(newLine1.group())

# 使用 .IGNORECASE 或.I 忽略大小写

ignoreCase = re.compile(r'cat', re.I)

cases = ignoreCase.findall("CAT cat CAt caT CaT cAt")

for case in cases:
    print(case)

# 使用.sub() 替换

subsitute = re.compile("Will \w+")

replaced = subsitute.sub("An unknown person", "Will Smith told BBC that CNN is fake news.")

print(replaced)

# 可以使用 .VERBOSE 将复杂正则拆分成多行

#regPatter = re.compile(r'''(
#        first pattern
#        second
#        third
#        ...
#        last patter'''), re.VERBOSE)

print("regPatter = re.compile(r'''(\n\tfirst pattern\n\tsecond\n\tthird\n\t...\n\tlast patter'''), re.VERBOSE)")

# 组合使用 忽略大小写，换行，verbose
print("组合使用多个第二参数， re.compile(r'foo', re.I|re.DOTALL|re.VERBOSE)")
