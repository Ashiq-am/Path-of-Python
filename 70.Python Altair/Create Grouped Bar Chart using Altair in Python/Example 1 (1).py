gp_chart = alt.Chart(data).mark_bar().encode(
alt.Column('Format'), alt.X('Player'),
alt.Y('Highest Score', axis=alt.Axis(grid=False)),
alt.Color('Player'))

gp_chart.display()
