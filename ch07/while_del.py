# 使用 while来删除

pets = ['dog', 'cat', 'snale', 'bear', 'kid', 'cat', 'cat', 'cat', 'dog', 'hund']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(f"\n now are have:")
for el in pets:
    print(f"\n{el}")
