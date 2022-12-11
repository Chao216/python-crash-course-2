import csv

exampleFile = open("./addresses.csv")
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

print(exampleData)
print(exampleData[0][0])
print(exampleData[0][1])
print(exampleData[0][2])
print(exampleData[2][0])
print(exampleData[2][1])
print(exampleData[3][2])
