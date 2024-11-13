# Adding a Y-Axis Label to
# the Secondary Y-Axis in Matplotlib
# importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

# creating dataframe for plot
dataset = pd.DataFrame({'Name': ['Rohit', 'Seema',
                                 'Meena', 'Geeta',
                                 'Rajat'],

                        'Height': [155, 129, 138, 164, 145],
                        'Weight': [60, 40, 45, 55, 60]})

# creating axes object and defining plot
ax = dataset.plot(kind='line', x='Name',
                  y='Height', color='Blue',
                  linewidth=3)

ax2 = dataset.plot(kind='line', x='Name',
                   y='Weight', secondary_y=True,
                   color='Red', linewidth=3,
                   ax=ax)

# title of the plot
plt.title("Student Data")

# labeling x and y-axis
ax.set_xlabel('Name', color='g')
ax.set_ylabel('Height', color="b")
ax2.set_ylabel('Weight', color='r')

# defining display layout
plt.tight_layout()

# show plot
plt.show()
