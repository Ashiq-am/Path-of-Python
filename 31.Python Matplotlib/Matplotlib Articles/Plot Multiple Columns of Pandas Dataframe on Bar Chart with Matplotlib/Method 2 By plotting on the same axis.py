# importing pandas library
import pandas as pd
# import matplotlib library
import matplotlib.pyplot as plt

# creating dataframe
df = pd.DataFrame({
	'Name': ['John', 'Sammy', 'Joe'],
	'Age': [45, 38, 90],
	'Height(in cm)': [150, 180, 160]
})

# plotting Height
ax = df.plot(x="Name", y="Height(in cm)", kind="bar")
# plotting age on the same axis
df.plot(x="Name", y="Age", kind="bar", ax=ax, color="maroon")
