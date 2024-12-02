from IPython.display import display
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'X': [5, 6], 'Y': [7, 8]})
df3 = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6],'C': [7, 8, 9]})

display(df1, df2,df3)

print(df1)
print(df2)
print(df3)