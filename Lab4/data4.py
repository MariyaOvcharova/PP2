import datetime

time1 = datetime.datetime(1994, 2, 14, 18, 54, 32)
time2 = datetime.datetime.now().replace(microsecond=0)

time1 = time1.timestamp()
time2 = time2.timestamp()

time3 = time2 - time1

print(time3)