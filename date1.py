from datetime import datetime, timedelta

date = datetime.now()
date2 = date - timedelta(days=5)

print("Current Date:", date.strftime("%Y-%m-%d"))
print("Date 5 Days Ago:", date2.strftime("%Y-%m-%d"))