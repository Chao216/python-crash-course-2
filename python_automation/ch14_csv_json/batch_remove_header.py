import csv, os
# loop through files in directory
for csvFilename in os.listdir("./many_csv_Dup"):
    if not csvFilename.endswith(".csv"):
        continue # skip non-csv files

    print("removing header from " + csvFilename + "...")

    # read csv
    csvRows = [] # create an empty list

    csvFileObj = open(os.path.join("./many_csv_Dup",csvFilename))
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1: # skip first line/row
            continue
        csvRows.append(row)
        print(csvRows)

    print(type(csvFileObj))
    csvFileObj.close()

    # write new csv

    csvFileObj = open(os.path.join("./many_csv_Dup", csvFilename), "w", newline = "")
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

