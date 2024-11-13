from datetime import datetime

# current time and date
# datetime object
time = datetime.now()

# formating date using strftime
# format = MM/DD/YY
print(time.strftime("%m/%d/%y"))

# format = Month D, Yr
print(time.strftime("%B %d, %Y"))

# time formating
# HH:MM:SS
print(time.strftime("%H:%M:%S"))
