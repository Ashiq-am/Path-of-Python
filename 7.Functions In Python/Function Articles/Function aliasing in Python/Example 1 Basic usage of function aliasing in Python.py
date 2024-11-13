def fun(name):
	print(f"Hello {name}, welcome to GeeksForGeeks!!!")


cheer = fun
print(f'The id of fun() : {id(fun)}')
print(f'The id of cheer() : {id(cheer)}')

fun('Geeks')
cheer('Geeks')
