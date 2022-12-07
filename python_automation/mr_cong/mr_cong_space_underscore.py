import os, re

pattern = re.compile(r"([a-zA-Z]+)(\s)([a-zA-Z]+)(\.)([0-9]+)(\.rar)")

while True:
    print("enter 'q' if you want to quit the program.")
    path = input("path of files you want to rename: ")

    if path == "q":
        break
    else:
        try:
            for root, dirs, files in os.walk(path):
                for entity in files:
                    mo = pattern.search(entity)
                    #print(mo.group(1))
                    #print(mo.group(2))
                    #print(mo.group(3))
                    #print(mo.group(4))
                    #print(mo.group(5))
                    #print(mo.group(6))
                    newFileName = mo.group(1) + "_" + mo.group(3) + "_" + mo.group(5) + mo.group(6)
                    oldFilePath = os.path.join(path, entity)
                    newFilePath = os.path.join(path, newFileName)
                    os.rename(oldFilePath, newFilePath)

        except:
            print("please enter a correct path !")

