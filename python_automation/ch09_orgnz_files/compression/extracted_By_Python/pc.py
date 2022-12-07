#! /usr/bin/env python3

import pyperclip as pc

text1 = "hello"

pc.copy(text1)

text2 = pc.paste()

print(text2)

list1 = ['apple', 'banane', 'kiwi', 'milch', 'kaffee', 'tee']

if len(list1) > 0:
    pc.copy('\n'.join(list1))
    print('copied to clipboard')
    print('\n'.join(list1))
