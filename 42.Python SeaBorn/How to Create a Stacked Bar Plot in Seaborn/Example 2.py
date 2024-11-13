# import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# create DataFrame
students = pd.DataFrame({'Boys': [67, 78],
						'Girls': [72, 80], },
						index=['First Year', 'Second Year'])


# create stacked bar chart for students DataFrame
students.plot(kind='bar', stacked=True, color=['red', 'pink'])

# Add Title and Labels
plt.title('Intermediate Students Pass %')
plt.xlabel('Year')
plt.ylabel('Percentage Ranges')
