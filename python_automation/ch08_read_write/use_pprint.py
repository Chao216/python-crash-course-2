import pprint

dogs = [{"name":"Bobbie", "age":3},{"name":"nana", "age":2}]

print(pprint.pformat(dogs))

fileObj = open("myDogs.py", "w")
fileObj.write("dogs = " + pprint.pformat(dogs) + "\n")

fileObj.close()
