df.sort_values(["grade", "favorite_color"],
			axis = 0, ascending = True,
			inplace = True,
			na_position ='first')

# printing the dataframe
df



"""
In case of in-place sorting, Dataframe.sort_values() method returns nothing 
it performs changes in the actual dataframe

"""
