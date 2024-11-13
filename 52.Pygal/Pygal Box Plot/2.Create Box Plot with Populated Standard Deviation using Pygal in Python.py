# Import Pygal
import pygal

# Student subject Scores data
math_scores = [40, 85, 68, 92, 78, 55, 39, 93, 67, 53]
english_scores = [75, 32, 48, 70, 85, 92, 99, 87, 59, 80]
science_scores = [88, 90, 32, 95, 78, 44, 91, 87, 68, 43]

# Create box plot object
box_plot = pygal.Box(box_mode="pstdev")

# Set tittle of box plot
box_plot.title = 'Student Test Scores'

# Add data to Box plot
box_plot.add('Math', math_scores)
box_plot.add('English', english_scores)
box_plot.add('Science', science_scores)

# Save output to svg file
box_plot.render_to_file('box_plot.svg')
