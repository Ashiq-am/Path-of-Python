# IMPORT THE PANDAS LIBRARY
# TO USE THE DATAFRAME TOOL
import pandas as pd

# IMPORT THE DIABETES DATA FROM THE
# SKLEARN MODULE
from sklearn.datasets import load_diabetes

# CREATE THE `convert_to_dataframe()
# FUNCTION
from sklearn.utils._bunch import Bunch


def convert_to_dataframe(sk_data: Bunch):
	if not isinstance(sk_data, Bunch):
		raise Exception("Not a sklearn dataset")
	return pd.DataFrame(data=sk_data.data,
						columns=sk_data.feature_names)


# LOAD THE DIABETES DATA USING
# THE `convert_to_dataframe()` FUNCTION
diabetes_data = convert_to_dataframe(sk_data=load_diabetes())

# DISPLAY FIRST 5 RECORDS OF THE DATAFRAME
diabetes_data.head()
