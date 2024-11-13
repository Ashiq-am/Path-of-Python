# Python3 code to demonstrate working of
# Column Mean in tuple list
# using zip() + map() + sum()

def avg(list):
    return sum(list) / len(list)


# initialize list
test_list = [(1, 2, 3), (6, 7, 6), (1, 6, 8)]

# printing original list
print("The original list : " + str(test_list))

# Column Mean in tuple list
# using zip() + map() + sum()
res = list(map(avg, zip(*test_list)))

# printing result
print("The Cummulative column mean is : " + str(res))
