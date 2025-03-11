import datetime
import calendar

current_time = datetime.datetime.now()
print("Current time: ", current_time)
print(current_time.date())
print(current_time.isoweekday())
print(current_time.ctime())

#print(calendar.calendar(100))
