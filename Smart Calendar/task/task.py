import datetime


def timedelta_convert(duration):
    days, seconds = duration.days, duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return days, hours, minutes


date_time = datetime.datetime.now()
print(f"Current date and time:\n{date_time}")
print("Let's add a note to the calendar.")
year = input("Enter year:\n")
month = input("Enter month:\n")
day = input("Enter day:\n")
hour = input("Enter hour:\n")
minute = input("Enter minute:\n")
text = input("Enter a text:\n")
delta = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute)) - date_time
days, hours, minutes = timedelta_convert(delta)
print(f'Before the event note "{text}" remains:\n{days} day(s), {hours} hour(s) {minutes} minute(s)')
