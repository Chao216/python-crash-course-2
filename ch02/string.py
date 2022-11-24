name = "chao jiang"
print(name.title())
print(name.lower())
print(name.upper())

first = "Lei"
last = "Yu"
full = f"{last} {first}"
print(full.title())
print(full.upper())
print(full.lower())

# 制表符与换行符
# 可以使用\n 换行print \t 对齐

print("\n\tCountries: \n\tRussia \n\tFinland \n\tHungary \n\tSlovakia \n\tCzech \n\tGermany \n\tEstonia \n\tItaly \n\tGreek \n\tAustria \n\tLativa \n\tLithunia \n\tPoland")

# 去除不需要的空格符 rstrip()

space = "   \ni don't really want to use the space between words, but it is conventional in English   "

print(space)
print(space.rstrip())
print(space.lstrip())
print(space.strip())


