import plotly.express as px
import pandas as pd


A = ["A", "B", "C", "D", None, "E",
		"F", "G", "H", None]

B = ["A1", "A1", "B1", "B1", "N",
		"A1", "A1", "B1", "B1", "N"]
C = ["N", "N", "N", "N", "N",
		"S", "S", "S", "S", "S"]
D = [1, 13, 21, 14, 1, 12, 25, 1, 14, 1]

df = pd.DataFrame(
	dict(A=A, B=B, C=C, D=D)
)

fig = px.sunburst(df, path=['C', 'B', 'A'], values='D')
fig.show()
