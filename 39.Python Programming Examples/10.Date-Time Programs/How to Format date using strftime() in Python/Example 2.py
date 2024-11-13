from datetime import datetime

# current time and date
# datetime object
time = datetime.now()
print("Without formating:", time)

# formating date using strftime
print("Year", time.strftime("%Y"))
print("Month name", time.strftime("%B"))
print("Day", time.strftime("%d"))
