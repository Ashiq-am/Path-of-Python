import plotly.express as px

df = px.data.tips()
df["e"] = df["total_bill"]/100

fig = px.bar(df, x="total_bill", y="day", color="sex",
			error_x="e", error_y="e")
fig.show()
