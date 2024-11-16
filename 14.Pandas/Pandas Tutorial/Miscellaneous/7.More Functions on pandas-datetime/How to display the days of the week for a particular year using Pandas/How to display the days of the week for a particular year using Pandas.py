# importing module
import pandas as pd


# User define function
def Time_series(day, yy):
	date_range = pd.date_range(yy+'-01-01', periods=52, freq=day)
	result = pd.Series(date_range)
	print(f"All { day[2:] } in " + yy + ":")
	print(result)


# Input from user
day = "wed"
yy = "2020"

# Check the day form input variable
if day == 'monday' or day == 'mon':
	Time_series('W-mon', yy)
elif day == 'tuesday' or day == 'tue':
	Time_series('W-tue', yy)
elif day == 'wednesday' or day == 'wed':
	Time_series('W-wed', yy)
elif day == 'thursday' or day == 'thu':
	Time_series('W-thu', yy)
elif day == 'friday' or day == 'fri':
	Time_series('W-fri', yy)
elif day == 'saturday' or day == 'sat':
	Time_series('W-fri', yy)
else:
	Time_series('W-sun', yy)
