#code for represeting states of USA
#pass list of states in locations
#list will have two-letter abbreviations of states
fig = px.choropleth(locations=["CA","TX","NY"], locationmode="USA-states", color=[1,2,3], scope="usa")

fig.show()
