# import pandas module
import pandas as pd

# create dataframe with 3 columns
data = pd.DataFrame({
	"column1": [12, 23, 45, 67],
	"column2": [67, 54, 32, 1],
	"column3": [34, 23, 56, 23]
}
)
# get correlation between element wise
print(data.corr())
