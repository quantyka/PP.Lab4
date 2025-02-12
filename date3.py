from datetime import datetime

date = datetime.now().replace(microsecond=0)

print("Datetime without microseconds:", date)