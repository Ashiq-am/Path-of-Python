# import the module
import pandas as pd

# create a DataFrame
df = pd.DataFrame({"A":[14, 4, 5, 4, 1],
					"B":[5, 2, 54, 3, 2],
					"C":[20, 20, 7, 3, 8],
					"D":[14, 3, 6, 2, 6]})

# making a green border
df.style.set_table_styles([{'selector' : '',
							'props' : [('border',
										'2px solid green')]}])
