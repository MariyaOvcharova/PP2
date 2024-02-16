import datetime

time = datetime.datetime.now()

time1 = time.replace(microsecond=0)
print(time1)
print(time.strftime("%I:%M:%S"))
