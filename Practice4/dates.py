from datetime import datetime, timedelta, timezone

now = datetime.now()        # current date/time
print(now)

my_date = datetime(2025, 12, 31, 23, 59)  # custom date
print(my_date)

formatted = now.strftime("%Y-%m-%d %H:%M:%S")  # format date
print(formatted)

future = datetime(2026, 1, 1)
diff = future - now         # time difference
print(diff.days)

tomorrow = now + timedelta(days=1)  # add 1 day
print(tomorrow)

utc_now = datetime.now(timezone.utc)  # UTC time
print(utc_now)