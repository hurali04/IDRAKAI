from datetime import datetime, date

now = datetime.now()
print("Current Date and Time:", now)

custom_date = date(2025, 8, 2)
print("Custom Date:", custom_date)

difference = (custom_date - now.date()).days
print("Number of days:", difference)
