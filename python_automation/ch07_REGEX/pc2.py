#! /usr/bin/env python3

import pyperclip as pc

list1 = ['Hello', "Hallo", "你好", "Moi"]

if len(list1) > 0:
    pc.copy(', '.join(list1))

result = pc.paste()

print(result)
