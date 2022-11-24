#遍历所有元素 使用 for
nations = ['Finland', 'Russia', 'Hungary', 'Slovakia', 'Czecha', 'Germany', 'Italy', 'Greek', 'Austria', 'Lithunia', 'Latvia', 'Estonia', 'Poland']

for nation in nations:
    print(nation)

#注意 for结尾有：

#在for中使用format

for nation in nations:
    print(f"{nation.upper()}, what a beautiful country !\n")
    print(f"I would like to visit {nation.upper()} again\n")
#在for结束后再执行一些命令

for nation in nations:
    print(f"{nation.upper()}, what a beautiful country !\n")
    print(f"I would like to visit {nation.upper()} again\n")
print("\n在for结束后依然可以做一些其他事！")


