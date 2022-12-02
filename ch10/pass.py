#你可以使用pass 来静默失败

try:
    print(3/0)
except ZeroDivisionError:
    pass

try:
    print(5/0)
except ZeroDivisionError:
    print("cannot be devided by 0")
