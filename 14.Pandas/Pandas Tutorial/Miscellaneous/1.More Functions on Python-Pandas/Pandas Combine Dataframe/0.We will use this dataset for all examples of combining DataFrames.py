data = """Name,Age,Gender,Salary
John,25,Male,50000
Alice,30,Female,55000
Bob,22,Male,40000
Eve,35,Female,70000
Charlie,28,Male,48000"""

import pandas as pd
df = pd.read_csv(pd.compat.StringIO(data))

display(df)