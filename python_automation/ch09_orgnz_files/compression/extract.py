import zipfile as zf

exampleZip = zf.ZipFile("./chap7.zip")

print(exampleZip.namelist())

exampleZip.extractall("./extracted_By_Python")
exampleZip.extract("pc2.py", "partial_extraction_by_Python")
