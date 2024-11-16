# counting number of values of all the columns
cnt_missing = (df[[1, 2, 3, 4,
				5, 6, 7, 8]] == 0).sum()
print(cnt_missing)
