# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba1.1.csv")

df = pd.DataFrame(data, index = [0, 1, 2, 3, 4, 5, 6,
								7, 8, 9, 10, 11, 12])

df(True, False, True, False, True, False, True, False, True, False, True, False, True)
