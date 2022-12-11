import datetime, time

print("datetime.datetime.now() will print current date and time")
print(datetime.datetime.now())

# use while, time, datetime to stop program until specific time, 

# time.sleep(1) will stop the program
while datetime.datetime.now() < datetime.datetime(2022,12,11,15,50,0):
    time.sleep(1)

print("Hello")
