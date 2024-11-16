# Compute average
c = avg = 0
for ele in df['Marks']:
	if str(ele).isnumeric():
		c += 1
		avg += ele
avg /= c

# Replace missing values
df = df.replace(to_replace="NaN",
				value=avg)

# Display data
df
