import os

for foldername, subfolders, files in os.walk("../"):
    print("the current folder is " + foldername)

    for subfolder in subfolders:
        print(subfolder + "is a subfolder of " + foldername)

    for entity in files:
        print(entity + " is inside " + foldername)

print("done with walk")


