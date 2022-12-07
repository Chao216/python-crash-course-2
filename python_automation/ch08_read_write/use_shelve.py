import shelve

shelfFile = shelve.open("mydata")

people = ["chao", "vova", "apurva"]

shelfFile['human'] = people

shelfFile.close()

newSF = shelve.open("mydata")

print(type(newSF))
print(newSF["human"])

newSF.close()

slFile = shelve.open("mydata")

print(list(slFile.keys()))
print(list(slFile.values()))

slFile.close()

