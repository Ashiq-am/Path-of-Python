# import pandas module
import pandas as pd

# create dataframe with 3 columns
data = pd.DataFrame({
	"column1": [12, 23, 45, 67],
	"column2": [67, 54, 32, 1],
	"column3": [34, 23, 56, 23]
}
)
# display dataframe
print(data)

# correlation between column 1 and column2
print(data['column1'].corr(data['column2']))

# correlation between column 2 and column3
print(data['column2'].corr(data['column3']))

# correlation between column 1 and column3
print(data['column1'].corr(data['column3']))
