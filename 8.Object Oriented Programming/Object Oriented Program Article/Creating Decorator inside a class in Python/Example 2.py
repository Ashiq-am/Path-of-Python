class Check_no:

    # decorator function
    def decor(func):
        def check(self, no):
            func(self, no)
            if no % 2 == 0:
                print('Yes, it\'s EVEN Number.')
            else:
                print('No, it\'s ODD Number.')

        return check

    @decor
    # instance method
    def is_even(self, no):
        print('User Input : ', no)


obj = Check_no()
obj.is_even(45)
obj.is_even(2)
obj.is_even(7)
