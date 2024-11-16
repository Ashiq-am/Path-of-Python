# import the packages
import pandas as pd

# read Dataset
data = pd.read_csv("drinksbycountry.csv")
data.head()

# peform groupby on continent and find median
# of total_litres_of_pure_alcohol
data.groupby(["continent"])["total_litres_of_pure_alcohol"].median()

# peform groupby on continent and find median
# of wine_serving
data.groupby(["continent"])["wine_servings"].median()
