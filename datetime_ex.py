import datetime
localdate=datetime.datetime.now()
print(localdate)
print(localdate.year,localdate.month,localdate.day)
print("Year:",localdate.year)
print("month:",localdate.month)
print("day:",localdate.day)
print("Hour:",localdate.hour)
print("Minutes:",localdate.minute)
print("second:",localdate.second)
print("TimeZone info:",localdate.tzinfo)

const=datetime.datetime(2023,9,24,12,23,45,10101)
print(const)
con=datetime.datetime(2023,9,24)
print(con)


