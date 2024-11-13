#Python 3 code to flatten nested list
#contributed by S Lakshman Rao - kaapalx
ini_list=[[1, 2, 3],
		[3, 6, 7],
		[7, 5, 4]]

#Using lambda

flatten_list = lambda y:[x for a in y for x in flatten_list(a)] if type(y) is list else [y]

print("Initial list ",ini_list) #priniting initial list

print("Flattened List ",flatten_list(ini_list)) # printing flattened list
