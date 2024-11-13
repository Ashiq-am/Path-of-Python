# menu function to display the menu
def menu():
    print("Welcome to Employ Management Record")
    print("Press ")
    print("1 to Add Employ")
    print("2 to Remove Employ ")
    print("3 to Promote Employ")
    print("4 to Display Employees")
    print("5 to Exit")

    # Taking choice from user
    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_Employ()

    elif ch == 2:
        Remove_Employ()

    elif ch == 3:
        Promote_Employee()

    elif ch == 4:
        Display_Employees()

    elif ch == 5:
        exit(0)

    else:
        print("Invalid Choice")
        menu()
