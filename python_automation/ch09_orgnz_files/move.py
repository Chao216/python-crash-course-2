import shutil as su, os

print(os.listdir("./"))

su.move("./folder1/toBeMoved.txt", "./folder3") # move a file to another destionation

print(os.listdir("./"))

