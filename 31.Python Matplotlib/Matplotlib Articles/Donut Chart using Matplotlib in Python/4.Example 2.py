# library
import matplotlib.pyplot as plt

# list of name of students
names = ['Manish', 'Atul', 'Priya', 'Harshit']

# list of their respective marks
marks = [45, 66, 55, 77]

# Create a circle at the center of
# the plot
my_circle = plt.Circle((0, 0), 0.7, color='white')

# Give color names
plt.pie(marks, labels=names, autopct='%1.1f%%',
		colors=['red', 'green', 'blue', 'yellow'])

p = plt.gcf()
p.gca().add_artist(my_circle)

# Show the graph
plt.show()
