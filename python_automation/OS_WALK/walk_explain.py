import os

while True:
    print("enter 'q', if you want to quit the program.")
    path = input("please enter path you want to walk:   ")

    if path == "q":
        break
    else:


        try:
            for root, dirs, files in os.walk(path):
                # print(root) every subfolder will be new root recursivly
                # print(dirs) a list of folders under CURRENT root
                # print(files) a list of files under CURRENT root
                #for folder in dirs:
                #   print(folder)
                #for name in files:
                #   print(name)
                #print(f"\n the root folders for files")
                #for name in files:
                #   print(os.path.abspath(root))

                #print(f"\n the root folder for subfolders:")
                #for folder in dirs:
                #   print(os.path.abspath(root))
                
                ##############################################################
                # os.walk will go though the directory tree recursivly
                # every level, there is only one root, could be many subfolder, files

                print("\n The current root folder is:   " + root + "\n")
                print("the absolute path of the current root folder is: ")
                print(os.path.abspath(root)+ "\n")

                for folder in dirs:
                    print(folder + " is a sub-folder under new root folder " + root + "\n")
                    print("the absolute path of this sub-folder is:  ")
                    print(os.path.abspath(root) + "\n")
                for name in files:
                    print(name + " is a file inside folder " + root + "\n")
                    print("the absolute path of the file is:   ")
                    print(os.path.abspath(root) + "\n")
        except:
            print("please check the path again.")
