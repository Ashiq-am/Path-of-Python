import pygal

# Sample Sales data for different cources on GFG
months = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept']
DSA_Self_Paced = [12000, 15000, 18000, 14000, 16000, 20000]
Java_Backend = [8000, 10000, 12000, 9000, 11000, 13000]
CIP = [8800, 14000, 12500, 8500, 10900, 12900]
DSA_Offline = [5000, 6000, 7000, 5500, 6500, 7500]
Web_Dev_Offline = [4500, 6100, 5100, 7500, 3500, 2500]

# Create a stacked line chart
line_chart = pygal.StackedLine(fill=True)

# Title and labels
line_chart.title = 'Monthly Sales by Product Category'
line_chart.x_labels = months

# Add data to the chart
line_chart.add('DSA Self Paced', DSA_Self_Paced)
line_chart.add('Java Backend', Java_Backend)
line_chart.add('Complete Interview Preparation', CIP)
line_chart.add('DSA Offline', DSA_Offline)
line_chart.add('Web Dev Offline', Web_Dev_Offline)

# Save the chart to a file
line_chart.render_to_file('stacked_line_chart.svg')
