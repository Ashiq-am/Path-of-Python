data = """First Name,Last Name,Age,Salary
John,Doe,25,50000
Alice,Smith,30,55000
Bob,Brown,22,40000
Eve,Green,35,70000
Charlie,White,28,48000"""

import pandas as pd
df = pd.read_csv(pd.compat.StringIO(data))

display(df)