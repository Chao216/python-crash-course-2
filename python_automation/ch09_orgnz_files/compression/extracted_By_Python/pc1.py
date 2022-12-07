#! /usr/bin/env python3

import pyperclip as pc

list1 = ["apple", "apfel", "bier", "milch", "zucker", "kaffee", "weine"]
if len(list1) >0:
    pc.copy(', '.join(list1)) #想要复制一个列表，要用一个string分割列表中的每个文本， 再用.join()方法

result = pc.paste()

print(result)
