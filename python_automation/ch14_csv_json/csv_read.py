import csv

exampleFile = open("./addresses.csv") # open file
exampleReader = csv.reader(exampleFile) # parse CSV
exampleData = list(exampleReader) # list data in cells

print(exampleData)
print(exampleData[0][0])
print(exampleData[0][1])
print(exampleData[0][2])
print(exampleData[2][0])
print(exampleData[2][1])
print(exampleData[3][2])

for row in exampleReader:
    print("row #" + str(exampleReader.line_num) + "  " + str(row) )
