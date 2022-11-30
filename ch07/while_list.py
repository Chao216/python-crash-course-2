unregistered = ["Chao Jiang", "Vladimir Balin", "Apurva Potdar"]

registered = []

while unregistered:
    temp_user = unregistered.pop()
    print(f"\n{temp_user} is being registering")
    registered.append(temp_user)

print(f"\nThe following user has been registered:")

for name in registered:
    print(f"\n{name}")
