import csv

exampleFile = open("./addresses.csv")
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

print(exampleData)
