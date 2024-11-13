# Python code to demonstrate
# 'not' keyword

# Function showing working of not keyword
def geek_Func():

	# Not with String boolean value
	geek_Str = "geek"
	print('Negation of String : ', not geek_Str)

	# Not with list boolean value
	geek_List = [1, 2, 3, 4]
	print('Negation of list : ', not geek_List)

	# Not with dictionary
	geek_Dict = {"geek": "sam", "collage": "Mit"}
	print('Negation of dictionary : ', not geek_Dict)

	# Not with Empty String
	geek_EDict = ""
	print('Negation of Empty String : ', not geek_EDict)

	# Not with Empty list
	geek_EList = []
	print('Negation of Empty List : ', not geek_EList)

	# Not with Empty dictionary
	geek_EStr = {}
	print('Negation of Empty Dictionary : ', not geek_EStr)

geek_Func()
