import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv("Tweets.csv")
df.head()

# Preprocessing the dataset to extract only
# the necessary columns
categories = [
	'negative',
	'neutral',
	'positive'
]

# Construct a pivot table with the column
# 'airline' as the index and the sentiments
# as the columns
gfg = pd.pivot_table(
	df,
	index='airline',
	columns='airline_sentiment',
	values='tweet_id',
	aggfunc='count'
)

# Include the sentiments - negative, neutral
# and positive
gfg = gfg[categories]

# Representing negative sentiment with negative
# numbers
gfg.negative = gfg.negative * -1

df = gfg

# Creating a Figure
Diverging = go.Figure()

# Iterating over the columns
for col in df.columns[4:]:

	# Adding a trace and specifying the parameters
	# for negative sentiment
	Diverging.add_trace(go.Bar(x=-df[col].values,
							y=df.index,
							orientation='h',
							name=col,
							customdata=df[col],
							hovertemplate="%{y}: %{customdata}"))
for col in df.columns:

	# Adding a trace and specifying the parameters
	# for positive and neutral sentiment
	Diverging.add_trace(go.Bar(x=df[col],
							y=df.index,
							orientation='h',
							name=col,
							hovertemplate="%{y}: %{x}"))

# Specifying the layout of the plot
Diverging.update_layout(barmode='relative',
						height=400,
						width=700,
						yaxis_autorange='reversed',
						bargap=0.5,
						legend_orientation='v',
						legend_x=1, legend_y=0
						)
Diverging
