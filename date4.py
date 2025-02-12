from datetime import datetime

dateFromat = "%Y-%m-%d %H:%M:%S"

date1 = datetime.strptime(input("Enter first date (YYYY-MM-DD HH:MM:SS): "), dateFromat)
date2 = datetime.strptime(input("Enter second date (YYYY-MM-DD HH:MM:SS): "), dateFromat)

difference = abs((date1 - date2).total_seconds())

print("Difference in seconds:", difference)