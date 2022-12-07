#shutil 可以理解为 shell utilities shell下的工具箱

import shutil as su, os

su.copy("./first.txt", "./A/B/C") # copy file to new destionation

su.copy("./first.txt", "./A/B/renamed.txt") # copy file to new destination and renamed the file

print(os.listdir("./"))

su.copytree("./A", "./Back_Up") # copy an entire folder and child folders, file

print(os.listdir("./"))

