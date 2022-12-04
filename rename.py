import os
while True:
    print("enter 'q' if you want to quit the program.")
    path = input("path of files you want to rename: ")

    if path == 'q':
        break
    else:
        try:
            list1 = os.listdir(path)
            num = 0
            for i in range(0, len(list1)):
                filepath = os.path.join(path, list1[i])
                if os.path.isfile(filepath):
                    filetype = os.path.splitext(filepath)[1]
                    template = '{:0>3d}'
                    newfilename = 'HuaYang_Vol_042_' + template.format(num + 1) + filetype
                    newfilepath = os.path.join(path, newfilename)
                    os.rename(filepath, newfilepath)
                    num += 1

                print("we have renamed " + str(num) + " files")

        except:
            print("please enter a valid path!")
