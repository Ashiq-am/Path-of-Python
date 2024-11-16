import pandas as pd

# Create a dataframe using three lists
df = pd.DataFrame(
	{'List1': [ 1 , 2 , 3 , 4 , 5 , 6 ],
	'List2': [ 5 , 10 , 15 , 20 , 25 , 30 ],
	'List3': [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' ]})

# use plot() method on the dataframe.
# List3 is in the x-axis and List2 in the y-axis
df.plot( 'List3' , 'List2' )
