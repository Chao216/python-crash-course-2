import json

pythonData = {"name":"Chao", "age":25, "height":173, "weight":70, "isMarried":False}

str_jsonData = json.dumps(pythonData)

with open("write_by_Py.json", "w") as fileObj:
    fileObj.write(str_jsonData)
