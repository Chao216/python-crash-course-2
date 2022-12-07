import zipfile as zf

exampleZip = zf.ZipFile("./chap7.zip")

print(exampleZip.namelist())

exampleZip.extractall("./extracted_By_Python") # extract all files to a designated folder
exampleZip.extract("pc2.py", "partial_extraction_by_Python") # extract some files to a designated folder
