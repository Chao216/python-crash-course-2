# flag 标志可以作为程序运行的开关

prompt = "\nTell me anything, I will repat: "
prompt += "\nEnter 'quit' to end this program."

active = True

message = ""

while active:
    message = input(prompt)
    
    if message != "quit":
        print(message)
    else:
        active = False
