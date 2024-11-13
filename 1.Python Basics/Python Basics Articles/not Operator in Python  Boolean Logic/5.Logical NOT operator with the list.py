# Python code to demonstrate
# 'not' keyword


geek_list = [5, 10, 20, 59, 134, 83, 95]


# Function showing working of not keyword
def geek_Func():
    # Using not with if statement
    if not geek_list:
        print("Inputted list is Empty")
    else:
        for i in geek_list:
            if not (i % 5):

                # Using not with in statement
                if i not in (0, 10):
                    print("Multiple is not in range")
                else:
                    print(i)
            else:
                print("The number is not multiple of 5")


geek_Func()
