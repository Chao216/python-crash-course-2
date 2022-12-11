import json

exampleFile = open("./json_sample.json")
exampleData = exampleFile.read()
json_data = json.loads(exampleData)
print(json_data)
