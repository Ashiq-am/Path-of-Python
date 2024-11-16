import pandas as pd
import ydata_profiling
# Sample DataFrame
data = {'ID': [1, 2, 3, 4, 5],
		'Category': ['A', 'B', 'A', 'C', 'B'],
		'Value': [10, 20, 15, 25, 30]}
df = pd.DataFrame(data)
# Generate a profiling report
profile = ydata_profiling.ProfileReport(df)
# Save the report to an HTML file (optional)
profile.to_file("data_profiling_report.html")
# Display the report
profile.to_widgets()
