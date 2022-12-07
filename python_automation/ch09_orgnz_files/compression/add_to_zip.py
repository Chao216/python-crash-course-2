import zipfile

newZip = zipfile.ZipFile("new.zip", "w") # must set write mode
newZip.write("compress.py", compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
