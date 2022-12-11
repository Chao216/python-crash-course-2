import csv

outputFile = open("write_by_Py.csv", "w", newline = "")
outputWriter = csv.writer(outputFile)
outputWriter.writerow([123,456,789,12])
outputWriter.writerow(["Hello", "Sir", "How", "are", "You"])

outputFile.close()
