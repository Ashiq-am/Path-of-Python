# Import Pygal
import pygal

# Student subject Scores data
math_scores = [40, 85, 68, 92, 78, 55, 39, 93, 67, 53]
english_scores = [75, 32, 48, 70, 85, 92, 99, 87, 59, 80]
science_scores = [88, 90, 32, 95, 78, 44, 91, 87, 68, 43]
hindi_scores = [88, 90, 62, 84, 78, 74, 91, 87, 68, 83]

# Create the instance of box plot
box_plot = pygal.Box(box_mode="tukey")
box_plot.title = ' Tukey Box Plot of Student Test Scores'

# Adding data with box plot
box_plot.add('Math', math_scores)
box_plot.add('English', english_scores)
box_plot.add('Science', science_scores)
box_plot.add('Hindi', hindi_scores)

# Rendering the plot to an SVG file
box_plot.render_to_file('Tukey_box_plot.svg')
