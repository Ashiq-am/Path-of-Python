# import necessary packages
import pandas as pd
import matplotlib.pyplot as plt

# create a dataframe
Marks = pd.DataFrame({'Raju': [8, 10, 7, 7, 10],
					'Hari': [6, 4, 6, 7, 6],
					'Bablu': [9, 9, 9, 9, 9],
					'Dora': [10, 9, 10, 9, 10]})

# plot marks of each student
plt.plot(Marks['Raju'], label="Raju Marks", color="Red")
plt.plot(Marks['Hari'], label="Hari Marks", color="Blue")
plt.plot(Marks['Bablu'], label="Bablu Marks", color="Yellow")
plt.plot(Marks['Dora'], label="Dora Marks", color="Black")

# labelling the axes
plt.xlabel("Tests")
plt.ylabel("Marks")

# add legend to plot
plt.legend()
plt.show()
