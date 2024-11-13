from datetime import time

# Creating Time object
Time = time(12,24,36,1212)
print("Original time:", Time)

# Rplacing hour
Time = Time.replace(hour = 13, second = 12)
print("New Time:", Time)

# Formatting Time
Ftime = Time.strftime("%I:%M %p")
print("Formatted time", Ftime)
