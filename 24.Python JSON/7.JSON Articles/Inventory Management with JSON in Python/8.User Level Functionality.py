def user():
    print("===============\
	Welcome to the User Inventory Management System\
	===============================================")

    while (1):
        print("1)Display All Products With Deatils")
        print("2)Display Specific Product With Deatils")
        print("3)Display All Purchase Bills")
        print("4)Buy The Product")
        print("5)Exit")
        print("Enter Your Choice :- ")
        n = int(input())
        if (n == 1):
            display_data()
        elif (n == 2):
            display_specific_data()
        elif (n == 3):
            display_user_data()
        elif (n == 4):
            buy_product()
        elif (n == 5):
            break
        else:
            print("Invalid Choice...!!!")
