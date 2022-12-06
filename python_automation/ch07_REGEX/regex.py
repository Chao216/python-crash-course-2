# 首先引入 re模块

import re

phone_num = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')

num1 = phone_num.search("my phone number is 123-4567-8901")

print(f"\nthe number found with regex is {num1.group()}")
