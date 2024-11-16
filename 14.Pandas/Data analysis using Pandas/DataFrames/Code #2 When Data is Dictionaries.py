# Program to Create Data Frame with two dictionaries
from turtle import pd

dict1 ={'a':1, 'b':2, 'c':3, 'd':4}	 # Define Dictionary 1
dict2 ={'a':5, 'b':6, 'c':7, 'd':8, 'e':9} # Define Dictionary 2
Data = {'first':dict1, 'second':dict2} # Define Data with dict1 and dict2
df = pd.DataFrame(Data) # Create DataFrame
