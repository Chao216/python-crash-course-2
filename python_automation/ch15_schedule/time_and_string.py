import time, datetime

now = datetime.datetime.now()

now_string = now.strftime('%Y%m%d @ %H:%M:%S')

print("strftime() will convert datetime into string")
print(now)
print(now_string)


print("strptime() will convert string into datetime")
date_string = "2019/12/12 13:56:21"

date = datetime.datetime.strptime(date_string, "%Y/%m/%d %H:%M:%S")

print(date)
