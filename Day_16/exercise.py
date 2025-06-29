from datetime import datetime, timedelta
now = datetime.now()
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Timestamp:", now.timestamp())

formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted Date:", formatted_date)

time_string = "5 December, 2019"
converted_time = datetime.strptime(time_string, "%d %B, %Y")
print("Converted Time:", converted_time)

next_new_year = datetime(now.year + 1, 1, 1)
time_diff_new_year = next_new_year - now
print("Time until New Year:", time_diff_new_year)

epoch = datetime(1970, 1, 1)
time_diff_epoch = now - epoch
print("Time since Unix Epoch:", time_diff_epoch)

print("\nUses of datetime module:")
print("- Time series analysis")
print("- Logging timestamps of user actions in applications")
print("- Scheduling events (like reminders, blog post scheduling)")
print("- Measuring execution time of code or processes")
print("- Formatting dates for reports or user interfaces")