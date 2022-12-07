# read a zipfile

import zipfile as zf, os

exampleZip = zf.ZipFile("./chap7.zip")
print(exampleZip.namelist())

joinInfo = exampleZip.getinfo("join.py")

print("join.py file size. \n")
print(joinInfo.file_size)
print("join.py compressed size \n")
print(joinInfo.compress_size)

