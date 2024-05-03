import datetime

today = datetime.datetime.now()
# yesterday = today - datetime.timedate(days = 1)  #создает день чтобы отнять его от сегодняшнего

print(today)
# print(yesterday)
# print(today - yesterday)


print(today.strftime("%d.%m.%Y, %I:%M:%S"))