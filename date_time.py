'''
Python Dates

- A date in Python is not a data type of its own.
- We can import a module named datetime to work with dates as date objects.
- The date contains year, month, day, hour, minute, second, and microsecond.
'''
# from datetime import datetime   
import datetime
now = datetime.datetime.now()
print(now)
print(f'date without time: {now.date()}')
print(f'different format: {now.strftime("%D")}')

# Return the year and name of weekday
print(f'year : {datetime.datetime.now().year}')
print(f'month : {now.month}')
print(f'day in number: {now.day} || day of the week short: {now.strftime("%A")}')
print(f'day of the week full {now.strftime("%a")}')
print(f'get PM/AM: Captial: {now.strftime("%p")} and get pm/am small: {now.strftime("%P")}')
print(f'day of the week full {now.strftime("%D")}')

'''
Creating Date Objects
- To create a date, we can use the datetime() class (constructor) of the datetime module.
- The datetime() class requires three parameters to create a date: year, month, day
'''
my_birth_day = datetime.datetime(year= 1991, month= 7, day =20)
print(f"my birthday created using datetime cunstructor {my_birth_day.date()}")
print(f"Year: {my_birth_day.strftime('%Y')}")
print(f"Month: {my_birth_day.strftime('%B')} and in number: {my_birth_day.strftime('%m')}")
print(f"day: {my_birth_day.strftime('%A')} and in numbers: {my_birth_day.strftime('%w')}")