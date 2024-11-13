#importing all required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#creating dataframe
df=pd.DataFrame({
	'X':[i for i in range(10,110,10)],
	'Y':[i for i in range(100,0,-10)],
	'Z':[i for i in range(10,110,10)]
})

#creating subplots
ax=plt.subplots()

#plotting columns
ax=sns.barplot(x=df["X"],y=df["Y"],color = 'lime')
ax=sns.barplot(x=df["X"],y=df["Z"],color = 'green')

#renaming the axes
ax.set(xlabel="x-axis", ylabel="y-axis")

# visulaizing illustration
plt.show()
