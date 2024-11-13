#importing packages
import plotly.express as px

# using medals_wide dataset
wide_df = px.data.medals_wide()

# plotting the bar chart
fig = px.histogram(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Geeksforgeeks")

# hiding legend
fig.update_traces(showlegend=False)

fig.show()
