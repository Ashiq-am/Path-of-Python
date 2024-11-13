# Import Pygal
import pygal

# Create a dot chart object
dot_chart = pygal.Dot()

# Set title to dot chart
dot_chart.title = 'Monthly Courses Sales Data'

# Set labels to x-axis
dot_chart.x_labels = ['System Design',
					'Java Backend',
					'CIP',
					'DSA self paced', 'CP']

# Adding data to dot chart
dot_chart.add('Sales', [105, 210, 390, 540, 198])

# Save dot chart to svg file
dot_chart.render_to_file('dotChart.svg')
