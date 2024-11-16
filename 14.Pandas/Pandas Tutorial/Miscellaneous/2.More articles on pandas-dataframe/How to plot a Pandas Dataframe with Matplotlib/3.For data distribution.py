# importing pandas library
import pandas as pd
# importing matplotlib library
import matplotlib.pyplot as plt

# creating dataframe
df = pd.DataFrame({
	'Object': ['Bulb', 'Lamp', 'Table', 'Pen', 'Notebook'],
	'Price': [45, 38, 90, 60, 40]
})

# plotting a pie chart
plt.pie(df["Price"], labels=df["Object"])
plt.show()
