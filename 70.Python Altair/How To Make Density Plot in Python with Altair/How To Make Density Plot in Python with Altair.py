import pandas as p # loading pandas library
import altair as a # loading altair library

# download dataset from https://drive.google.com/drive/folders/1Dddv1l9hpEPVWh_uuK9Iv1A1xUNy55v7?usp=sharing
# OR replace name with your own dataset.
data_set = 'insurance.csv'
d = p.read_csv(data_set)
d = d[["charges"]]

a.Chart(d).transform_density('charges', as_=['CHARGES', 'DENSITY'],
							).mark_area(color='green').encode(
	x="CHARGES:Q",
	y='DENSITY:Q',
)
