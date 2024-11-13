# import packages and libraries
import pandas as pd
import plotly.express as px

# reading the dataset
df = pd.read_csv('country_density.csv', encoding='UTF-8')

# taking observations of first 5 countries
df = df.iloc[:5, :]

# plotting bar plot
fig = px.bar(df, x="Country", y="Density_(P/Km²)", color="Country",
			orientation="v",
			hover_name="Country", color_discrete_sequence=[
				px.colors.qualitative.Alphabet[6],
				px.colors.qualitative.Alphabet[11],
			px.colors.qualitative.Plotly[2],
				px.colors.qualitative.Plotly[7],
			px.colors.qualitative.G10[5]],
			title="Explicit color sequence"
			)

fig.show()
