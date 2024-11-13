# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
	print(a, b, c, d)

# Driver Code
my_list = [1, 2, 3, 4]

# Unpacking list into four arguments
fun(*my_list)





'''As another example, consider the built-in range() function that expects separate start and stop arguments. 
If they are not available separately, 
write the function call with the *-operator to unpack the arguments out of a list or tuple:'''





range(3, 6) # normal call with separate arguments
[3, 4, 5]
args = [3, 6]
range(*args) # call with arguments unpacked from a list
[3, 4, 5]
