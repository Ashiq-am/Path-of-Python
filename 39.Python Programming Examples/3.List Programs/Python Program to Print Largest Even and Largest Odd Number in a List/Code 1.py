class LargestOddAndEven:

    # find largest even number of
    # the list
    def largestEven(self, list):

        # counter for current largest
        # even number
        curr = -1

        for num in list:

            # converting number to integer
            # explicitly
            num = int(num)

            # even number is divisible by 2 and
            # if larger than current largest
            if (num % 2 == 0 and num > curr):
                # replace current largest even
                curr = num

        print("Largest even number is ", curr)

    # find largest odd number of the list
    def largestOdd(self, list):

        # current largest odd number
        currO = -1
        for num in list:

            # converting number to integer
            # explicitly
            num = int(num)

            # even number is divisible by 2 and
            # if larger than current largest
            if (num % 2 == 1 and num > currO):
                # replace current largest even
                currO = num

        print("Largest odd number is ", currO)


list_num = [1, 3, 5, 8, 6, 10]

# creating an object of class
obj = LargestOddAndEven()

# calling method for largest even number
obj.largestEven(list_num)

# calling method for largest odd number
obj.largestOdd(list_num)
