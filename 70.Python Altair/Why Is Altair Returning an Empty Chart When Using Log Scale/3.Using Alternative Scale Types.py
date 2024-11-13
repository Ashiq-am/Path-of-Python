import altair as alt

chart = alt.Chart(df_filtered).mark_bar().encode(
    x=alt.X('value', scale=alt.Scale(type='symlog')),
    y='group'
)
chart
