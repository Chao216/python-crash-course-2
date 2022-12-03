a = [1,1,1,2,2,2,3,3,3]

print("loop through a list")
for i in a:
    print(i)

b = (1,1,1,2,2,2,3,3,3)

print("loop through a tuple")
for i in b:
    print(i)

c = {1,1,1,2,2,2,3,3,3}

print("loop through a set")
for i in c:
    print(i)

d = {"a":1, "b":2, "c":3,"d":4,"e":5,"f":6}

print("loop through a dictionary")
for i, j in d.items():
    print(f"Key: {i}")
    print(f"\n\tValue: {j}")
