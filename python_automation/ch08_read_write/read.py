noteFile = open("./note.txt")

# noteContent = noteFile.read()

# print(noteContent)

noteLines = noteFile.readlines()

print(type(noteLines))

print(noteLines)

for i in noteLines:
    print(f"\n\t{i}")
