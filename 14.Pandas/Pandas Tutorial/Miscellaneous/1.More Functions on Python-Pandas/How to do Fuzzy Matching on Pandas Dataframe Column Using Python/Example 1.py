from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas

dict1 = {'name': ["aparna", "pankaj",
				"sudhir", "Geeku"]}

dict2 = {'name': ["aparn", "arup", "Pankaj",
				"sudhir c", "Geek", "abc"]}

# converting to pandas dataframes
dframe1 = pd.DataFrame(dict1)
dframe2 = pd.DataFrame(dict2)

# empty lists for storing the
# matches later
mat1 = []
mat2 = []

# printing the pandas dataframes
dframe1.show()
dframe2.show()
