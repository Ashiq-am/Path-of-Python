# import pygal module
import pygal

# Create a dot_chart object
dot_chart = pygal.Dot(x_label_rotation=30)

# Set title to chart, x-axis, and y-axis
dot_chart.title = 'GeeksforGeeks Hackathon results'
dot_chart.x_title = 'Students names'
dot_chart.y_title = 'Section'

# Set labels to x-axis
dot_chart.x_labels = ['Ramesh', 'Suresh',
					'Carry', 'Tiger',
					'Jonny', 'Lakhan',
					'Sita', 'Krishna']

# Add data to Dot Chart
dot_chart.add('Aptitude', [69, 82, 75, 72, 64, 60, 21, 86])
dot_chart.add('OOPs', [74, 99, 77, 51, 61, 44, 97, 94])
dot_chart.add('DSA', [34, 29, 42, 59, 58, 28, 90, 69])

# Save file to SVG
dot_chart.render_to_file('dot_chart.svg')
