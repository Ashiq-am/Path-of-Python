# importing package
import pandas

# creating data
from tensorboard.notebook import display

data = pandas.DataFrame({
	"Student": ["A", "B", "C", "D"],
	"Physics": [89,34,23,56],
	"Chemistry": [34,56,98,56],
	"Math": [34,94,50,59]
	})

# view data
display(data)

# adding new column by existing
# columns evaluation
data['Total']=pandas.eval("data.Physics+data.Chemistry+data.Math")

# view data
display(data)

# adding new column by existing
# columns evaluation
pandas.eval("Avg=data.Total/3",target=data,inplace=True)

# view data
display(data)
