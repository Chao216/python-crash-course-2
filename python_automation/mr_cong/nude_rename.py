import os

while True:
    print("enter 'q' to end the program.")
    path = input("please enter the path you want to operate:   ")

    if path == "q":
        break
    else:
        try:
            for root, dirs, files in os.walk(path):
                for folder in dirs:
                    folderPath = os.path.join(os.path.abspath(root), folder) # dirname of individual image file
                    #print(folderPath)
                    list1 = os.listdir(folderPath) # list all image files in the dirname
                    #print(len(list1))
                    num = 0 # init as 0
                    for i in range(0, len(list1)): # loop through the list
                        filePath = os.path.join(folderPath,list1[i] ) # dirname/basname
                        #print(filePath)
                        fileType = os.path.splitext(filePath)[1] # get filetype extension name
                        template = '{:0>3d}'
                        prefix = os.path.relpath(folderPath, root) # use relpath to get short folder name
                        newFileName = prefix + "_" + template.format(num+1) + fileType # generate new file name
                        #print(newFileName)
                        newFilePath = os.path.join(folderPath, newFileName) # create new dirname/basename
                        #print(newFilePath)
                        os.rename(filePath, newFilePath) # rename the files in loop
                        num += 1 # increase num by 1 every time

        except:
            print("check the path again !")
