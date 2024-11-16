import pandas as pd

# reading csv
s = pd.read_csv("stock.csv", squeeze = True)

# defining function to check price
def fun(num):

	if num<200:
		return "Low"

	elif num>= 200 and num<400:
		return "Normal"

	else:
		return "High"

# passing function to apply and storing returned series in new
new = s.apply(fun)

# printing first 3 element
print(new.head(3))

# printing elements somewhere near the middle of series
print(new[1400], new[1500], new[1600])

# printing last 3 elements
print(new.tail(3))
