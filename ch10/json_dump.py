import json

numbers = [1, 3, 5, 9, 11, 13, 15]

with open("json_dump.json", "w") as file_object:
    json.dump(numbers, file_object)
