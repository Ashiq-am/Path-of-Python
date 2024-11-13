import plotly.express as px


df = px.data.tips()
df["error"] = df["total_bill"]/100

fig = px.scatter(df, x="total_bill", y="day", color="sex",
				error_x="error", error_y="error")
fig.show()
