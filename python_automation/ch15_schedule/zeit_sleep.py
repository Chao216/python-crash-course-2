import time

for i in range(10):
    print("tick")
    time.sleep(2)
    print("Tock")
    time.sleep(2)

time.sleep(5)
print("done with sleep")
