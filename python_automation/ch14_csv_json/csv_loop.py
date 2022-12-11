import csv

exampleFile = open("./addresses.csv")
exampleReader = csv.reader(exampleFile)

for row in exampleReader:
    print("row #" + str(exampleReader.line_num) + "  " + str(row) )
