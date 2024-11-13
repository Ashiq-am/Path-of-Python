import altair as alt
import pandas as pd

# creating a custom dataframe
data = pd.DataFrame([[264, 'Rohit', 'ODI'],
					[183, 'Virat', 'ODI'],
					[118, 'Rohit', 'T20'],
					[94, 'Virat', 'T20'],
					[212, 'Rohit','Test'],
					[254, 'Virat','Test']],
					columns=['Highest Score', 'Player', 'Format'])

print(data)
