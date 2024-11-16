def replace_nan_with_mean(arr):
	col_means = [sum(filter(lambda x: x is not None, col))/len(list(filter(lambda x: x is not None, col))) for col in zip(*arr)]
	for i in range(len(arr)):
		arr[i] = [col_means[j] if x is None else x for j, x in enumerate(arr[i])]
	return arr
arr=[[1.3, 2.5, 3.6, None],
	[2.6, 3.3, None, 5.5],
	[2.1, 3.2, 5.4, 6.5]]
print(replace_nan_with_mean(arr))
