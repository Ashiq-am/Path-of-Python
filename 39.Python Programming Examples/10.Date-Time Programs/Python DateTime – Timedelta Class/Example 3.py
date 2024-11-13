from datetime import timedelta

# Getting minimum value
obj = timedelta(hours=1)
print(obj.total_seconds())

obj = timedelta(minutes=1)
print(obj.total_seconds())

obj = timedelta(days=1)
print(obj.total_seconds())
