from datetime import timedelta, datetime
date1=datetime(2024,9,24)
date2=datetime(2025,9,24)
time_diff=date1-date2
print(time_diff)
delta=timedelta(days=20,hours=12,minutes=12)
newdate=date2+delta
print(newdate)
datenew=newdate-delta
print(datenew)
print(delta)
print(delta.days)
print(delta.seconds)
print(delta.total_seconds())
print(str(delta))
if delta > timedelta(days=10):
    print("delta")