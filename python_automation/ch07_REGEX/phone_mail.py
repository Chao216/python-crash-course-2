#! /usr/bin/env python3
import re, pyperclip # 引入正则模块

phoneRegex = re.compile(r'(1\d{10})')

emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+ # username
        @                 # @ at symbol
        [a-zA-Z0-9._]+    # domain name
        (\.[a-zA-Z.]{2,5}) # .com .cn .co.uk 之类
        )''', re.VERBOSE)


text = str(pyperclip.paste()) #stringfy paste buffer contents
matches = [] #空列表

for num in phoneRegex.findall(text):
    phoneNum = num[1]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("copied to clipboard:")
    print('\n'.join(matches))

else:
    print("no number or emails found.")

