import datetime as dt
import time as tm

tm.time()
dtnow = dt.datetime.fromtimestamp(tm.time())

print(dtnow.year, dtnow.month, dtnow.day, dtnow.hour)

delta = dt.timedelta(days=100)
today = dt.date.today()

print(today-delta)
print(today>today-delta)
