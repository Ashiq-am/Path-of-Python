# Importing altair and pandas library
import altair as alt
import pandas as pd

# Making a Pandas DataFrame
score_data = pd.DataFrame({
	'Website': ['StackOverflow', 'FreeCodeCamp',
				'GeeksForGeeks', 'MDN', 'CodeAcademy'],
	'Score': [65, 50, 99, 75, 33]
})

# Making the Simple Bar Chart
alt.Chart(score_data).mark_bar().encode(
	# Mapping the Website column to x-axis
	x='Website',
	# Mapping the Score column to y-axis
	y='Score'
)
