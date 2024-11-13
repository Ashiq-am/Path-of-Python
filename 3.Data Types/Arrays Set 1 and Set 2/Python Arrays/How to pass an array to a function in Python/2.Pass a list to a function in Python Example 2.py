def Product(nums):
    p = 1
    for i in nums:
        # Multiplication of every element
        # of nums with each other
        p *= i
    print("Product: ", p)


# Created a list of integers
nums = [4, 5, 6]

# Passed the entire list as a parameter
Product(nums)
