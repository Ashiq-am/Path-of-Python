def admin():
    print("============= Welcome to the Admin Inventory Management System =====")

    while (1):
        print("1)Display DataBase/All Products with there details")
        print("2)Display Specific Product with its details")
        print("3)Insert Data Into DataBase")
        print("4)Update Product in Database")
        print("5)Delete Product in DataBase")
        print("6)Display User Purchase Reports")
        print("7)Exit")
        print("Enter Your Choice :- ")

        n = int(input())
        if (n == 1):
            display_data()
        elif (n == 2):
            display_specific_data()
        elif (n == 3):
            add_new()
        elif (n == 4):
            update_prod_data()
        elif (n == 5):
            delete_prod()
        elif (n == 6):
            display_reports_admin()
        elif (n == 7):
            break
        else:
            print("Invalid Choice...!!!")
