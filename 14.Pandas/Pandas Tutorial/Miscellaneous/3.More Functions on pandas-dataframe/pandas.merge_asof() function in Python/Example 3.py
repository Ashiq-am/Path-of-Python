# importing package
import pandas

# creating data
left = pandas.DataFrame({'left_val': ['a', 'b', 'c']},
						index=[1, 5, 10])

right = pandas.DataFrame({'right_val': [1, 2, 3, 6, 7]},
						index=[1, 2, 3, 6, 7])

# view data
print(left)
print(right)

# applying merge_asof on data
print(pandas.merge_asof(left, right, left_index=True,
						right_index=True))
