from datetime import time

# Creating Time object
Time = time(12,24,36,1212)

# Converting Time object to string
Str = Time.isoformat()
print("String Representation:", Str)
print(type(Str))

Time = "12:24:36.001212"

# Converting string to Time object
Time = time.fromisoformat(Str)
print("\nTime from String", Time)
print(type(Time))
