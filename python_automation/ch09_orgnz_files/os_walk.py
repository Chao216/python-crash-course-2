import os

for folderName, subfolders, files in os.walk("/home/chao"):
    print("the current folder is: " + folderName)

    for subfolder in subfolders:
        print(subfolder + "is a SUBFOLDER of " + folderName)


    for single_file in files:
        print(single_file + " is inside folder" + folderName)

print(" ")

