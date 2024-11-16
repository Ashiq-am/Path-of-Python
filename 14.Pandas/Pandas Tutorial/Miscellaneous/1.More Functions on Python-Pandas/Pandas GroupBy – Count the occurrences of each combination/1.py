# Import library
import pandas as pd
import numpy as np

# intialise data of lists.
Data = {'Products':['Box','Color','Pencil','Eraser','Color',
					'Pencil','Eraser','Color','Color','Eraser','Eraser','Pencil'],

	'States':['Jammu','Kolkata','Bihar','Gujrat','Kolkata',
				'Bihar','Jammu','Bihar','Gujrat','Jammu','Kolkata','Bihar'],

	'Sale':[14,24,31,12,13,7,9,31,18,16,18,14]}

# Create DataFrame
df = pd.DataFrame(Data, columns=['Products','States','Sale'])

# Display the Output
display(df)
