import pandas as pd

data = [[1, "ABC KUMAR", "xYZ"], [2, "BCD", "XXY"],
		[3, "CDE KUMAR", "ZXX"], [3, "DEF", "xYZZ"]]

cfile = pd.DataFrame(data, columns = ["SN", "FirstName", "LastName"])

cfile
