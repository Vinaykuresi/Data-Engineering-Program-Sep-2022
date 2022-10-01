
# date and time
import time
import datetime

# time in secs
print(time.time())

# start time
print(time.gmtime(0))

# local time
print(time.localtime())

# gmt
print(time.gmtime())

# convert secs in time
print(time.ctime(1664585898.0144057))

# datetime
print(datetime.date.today())

# specify the format
print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))

# sleep
for num in range(5):
    time.sleep(2)
    print(num)