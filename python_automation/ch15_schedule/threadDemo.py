import threading, time

print("program started")

def takeANap():
    print("I am going to take a nap")
    time.sleep(10)
    print("I am done with my nap")

thread_1 = threading.Thread(target = takeANap)

thread_1.start()

print("end of program")
