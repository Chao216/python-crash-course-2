import os, re

pattern = re.compile(r'([a-zA-Z]+)(-)([a-zA-Z]+)(\.)([0-9]+)([a-zA-Z.-]+)(\d{3,4})(.jpg)')

while True:
    print("enter 'q' to quit the program")
    path = input("please enter the path you want to operate:   ")

    if path == "q":
        break
    else:
        try:
            for root, dirs, files in os.walk(path):
                # print(root)
                for name in files:
                    # print(name)
                    # print(os.path.abspath(root))
                    # print(len(os.listdir(root)))
                    filePath = os.path.join(os.path.abspath(root), name)
                    # print(filePath)
                    mo = pattern.search(name)
                    #print(mo.group())
                    newFileName = mo.group(1) + "_" + mo.group(3) + "_" + mo.group(5) + "_" + mo.group(7) + mo.group(8)
                    # print(newFileName)
                    newFilePath = os.path.join(os.path.abspath(root), newFileName)
                    # print(newFilePath)
                    os.rename(filePath, newFilePath)
        except:
            print("please check the path.")
