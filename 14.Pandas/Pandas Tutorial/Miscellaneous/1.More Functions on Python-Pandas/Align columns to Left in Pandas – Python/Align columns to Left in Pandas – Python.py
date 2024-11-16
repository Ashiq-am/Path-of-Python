# Python code demonstrate creating
# DataFrame from dict and left aligning
import pandas as pd

# intialise data of lists.
data = {'Name': ['Tania', 'Ravi',
                 'Surbhi', 'Ganesh'],

        'Articles': [50, 30, 45, 33],

        'Location': ['Kanpur', 'Kolkata',
                     'Kolkata', 'Bombay']}

# Create DataFrame
df = pd.DataFrame(data)
display(df)
