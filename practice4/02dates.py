#1
import datetime
today=datetime.date.today()
new_date=today-datetime.timedelta(days=5)
print("Before 5 days:" , new_date)

#2
from datetime import date,timedelta
today=date.today()
yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)
print("Yesterday:",yesterday)
print("Today:",today)
print("Tomorrow:",tomorrow)
#3
from datetime import datetime
now=datetime.now()
no_microsec=now.replace(microsecond=0)
print(no_microsec)
#4
from datetime import datetime
d1=datetime(2026,1,1,0,0,0)
d2=datetime(20206,1,2,0,0,0)
difference=d2-d1
print(difference.total_seconds())
