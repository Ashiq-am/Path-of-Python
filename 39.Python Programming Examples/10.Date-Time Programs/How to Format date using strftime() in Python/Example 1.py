from datetime import datetime

# current time and date
# datetime object
time = datetime.now()
print("Without formating:", time)

# formating date using strftime
print("After formating:", time.strftime("%b %d, %Y"))
