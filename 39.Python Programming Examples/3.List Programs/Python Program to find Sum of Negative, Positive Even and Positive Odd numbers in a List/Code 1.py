class Sumofnumbers:
    # find sum of numbers
    # according to categories
    def Sum(self, list):

        # counter for sum
        # of negative numbers
        neg_sum = 0

        # counter for sum of
        # positive even numbers
        pos_even_sum = 0

        # counter for sum of
        # positive odd numbers
        pos_odd_sum = 0

        for num in list:

            # converting number
            # to integer explicitly
            num = int(num)

            # if negative number
            if (num < 0):

                # simply add
                # to the negative sum
                neg_sum += num
            # if positive number
            else:

                # if even positive
                if (num % 2 == 0):

                    # add to positive even sum
                    pos_even_sum += num
                else:

                    # add to positive odd sum
                    pos_odd_sum += num
        print("Sum of negative numbers is ",
              neg_sum)
        print("Sum of even positive numbers is ",
              pos_even_sum)
        print("Sum of odd positive numbers is ",
              pos_odd_sum)


# input a list of numbers
list_num = [1, -1, 50, -2, 0, -3]

# creating an object of class
obj = Sumofnumbers()

# calling method for
# largest sum of all numbers
obj.Sum(list_num)
