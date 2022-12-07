# read a zipfile

import zipfile as zf, os

exampleZip = zf.ZipFile("./chap7.zip")
print(exampleZip.namelist())

joinInfo = exampleZip.getinfo("join.py")

print(joinInfo.file_size)
print(joinInfo.compress_size)

