import os, shutil as su

while True:
    print("enter 'q' to end this program.")
    path = input("please enter the path you want to operate: ")

    if path == "q":
        break
    else:
        try:
            for root, dirs, files in os.walk(path):
                #print("the root is " + root )
                for i in files:
                    filePath = os.path.join(os.path.abspath(root), i)
                    delPath = os.path.abspath(root)
                    #print(filePath)
                    parentPath = os.path.join(os.path.abspath(root), "../")
                    #print(parentPath)
                    su.move(filePath, parentPath)
                if (len(os.listdir(root))) == 0:
                    os.rmdir(root)
        except:
            print("please check the path again !")
