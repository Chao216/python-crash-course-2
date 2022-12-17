import datetime as dt

def now():
    print(dt.datetime.now())

f = now # function is also object

print(type(now))

f()

print(type(f))

# function has a __name__ attribute

print(f.__name__,"\n",now.__name__)
