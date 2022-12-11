import subprocess, time

calProc = subprocess.Popen("/usr/bin/gnome-calculator")

time.sleep(5)
print(f"\n the poll is {calProc.poll()}")
print(f"\n the wait is {calProc.wait()}")


time.sleep(5)
print(f"\n the poll is {calProc.poll()}")
print(f"\n the wait is {calProc.wait()}")
time.sleep(5)
print(f"\n the poll is {calProc.poll()}")
print(f"\n the wait is {calProc.wait()}")
time.sleep(5)
print(f"\n the poll is {calProc.poll()}")
print(f"\n the wait is {calProc.wait()}")
time.sleep(5)
print(f"\n the poll is {calProc.poll()}")
print(f"\n the wait is {calProc.wait()}")
time.sleep(5)
print(f"\n the poll is {calProc.poll()}")
print(f"\n the wait is {calProc.wait()}")
