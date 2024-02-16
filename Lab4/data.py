import datetime

today = datetime.datetime.now()

fivedays = today - datetime.timedelta( days = 5)

print("5 days before was:" ,fivedays.strftime("%d.%m.%Y"))


