#! /usr/bin/env python3

import os

path = os.path.join("Home", "Chao", "Documents")

print(path)
print(type(path))

print(os.path.abspath("./"))
print(os.path.isabs("./"))

print(os.path.relpath("./", "/home/chao"))

current_path = os.path.abspath("./")
print(current_path)

filePath = current_path + "/path.py"

print(filePath)

print(f"\n basename: {os.path.basename(filePath)}")
print(f"\n dirname: {os.path.dirname(filePath)}")

print(filePath.split(os.path.sep))

print(f"\ncheck path (file) size ondisk with os.path.getsize()")
print(f"\n{os.path.getsize(filePath)}")

print(f'\n list files on directory with os.listdir()')
print(f"\n{os.listdir(current_path)}")

print(f"\n check validity of path and file with os.path.exists(), os.isdir(), os.isfile()")

print(f"\n{os.path.exists(current_path)}")
print(f"\n{os.path.isfile(filePath)}")
print(f"\n{os.path.isdir(current_path)}")
