from datetime import date

local=date.today()
print(local.year)
print(local.month)
print(local.day)

specific_date=date(2023,12,30)
print("specific_date:",specific_date)
print(specific_date.year)
print(specific_date.month)
print(specific_date.day)