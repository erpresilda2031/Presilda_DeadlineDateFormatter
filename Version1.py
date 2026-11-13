# Version 2: Added date formatting using the datetime module
from datetime import datetime

event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_date = datetime(year, month, day)

print("Formatted Output:")
print("Event:", event_title.upper())
print("Date:", event_date.strftime("%B %-d, %Y"))
print("Year:", event_date.strftime("%Y"))
print("Month:", event_date.strftime("%B"))
print("Day:", event_date.strftime("%-d"))
print("Weekday:", event_date.strftime("%A"))