# 基本 while 循环

current = 0

while current <= 10:
    print(f"\n current number is {current}")
    current += 1

# 复读机
prompt = ("please say something, and I will repeat it.")
prompt += ("if you want to stop, enter 'quit'.")

message = ""

while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)
