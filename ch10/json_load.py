import json

with open("json_dump.json") as file_object:
    num = json.load(file_object)

print(num)

for n in num:
    print(f"\n\t{n}")
