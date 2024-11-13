# importing the module
import timeit


# using the timeit method and lambda
# expression to get the execution time of
# the function.
t = timeit.timeit(lambda: "print('Hello World!')")

# printing the execution time
print(t)
