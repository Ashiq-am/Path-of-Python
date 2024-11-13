class LargestOddAndEven:

    # find largest even number of the list
    def largestEvenandOdd(self, list):

        # counter for current largest even
        # number
        curr = -1

        # counter for current largest odd
        # number
        currO = -1
        for num in list:

            # converting number to integer
            # explicitly
            num = int(num)

            # even number is divisible by 2 and
            # if larger than current largest
            if (num % 2 == 0 and num > curr):

                # replace current largest even
                curr = num

            elif (num % 2 == 1 and num > currO):

                # replace current largest even
                currO = num

        print("Largest odd number is ", currO)
        print("Largest even number is ", curr)


# input a list of numbers
list_num = [123, 234, 236, 694, 809]

# creating an object of class
obj = LargestOddAndEven()

# calling method for largest even and odd number
obj.largestEvenandOdd(list_num)
