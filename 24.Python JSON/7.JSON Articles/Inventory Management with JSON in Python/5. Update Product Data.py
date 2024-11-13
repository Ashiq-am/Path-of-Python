def update_prod_data():
    import json
    fd = open("data.json", 'r')
    txt = fd.read()
    data = json.loads(txt)
    fd.close()
    print("Enter The Product ID of The Product\
	Which You Want To Update :- ")
    temp = input()

    if temp in data.keys():
        print("Want to update whole product data\
		press '0' else '1' for specific data :- ")
        q = int(input())
        if (q == 0):

            print("Enter Product Name :- ")
            name = input()

            print("Enter Price of Product(price for product quantity as 1) :- ")
            price = input()

            print("Enter Category of Product :- ")
            category = input()

            print("Enter Quantity of Product :- ")
            quantity = input()

            print("Enter The Date on Which Product is Added in Inventory :- ")
            date = input()

            data[temp] = {'name': name, 'price': price,
                          'category': category, 'quantity': quantity,
                          'date': date}
            print(
                "Please Press '0' to Add more Attributes\
                /Properties of Product or Press '1' to Continue :- ")
            z = int(input())
            if (z == 0):
                print("Enter Number of New Attributes/Properties of Product :- ")
                n = int(input())

                for i in range(n):
                    print("Enter Attribute Name That you Want To Add :- ")
                    nam = input()
                    print("Enter The " + str(nam) + " of Product :- ")
                    pro = input()
                    data[temp][nam] = pro
            print("Product ID " + str(temp) + " Updated Successfully...!!!")

        elif (q == 1):
            print("Enter Which Attribute of Product You want to Update :- ")
            p = input()

            if p in data[temp].keys():
                print("Enter " + str(p) + " of Product :- ")
                u = input()
                data[temp][p] = u
                print("Product ID " + str(temp) + "'s attribute " +
                      str(p) + " is Updated Successfully...!!!")
            else:
                print("Invalid Product Attribute...!!!")
        else:
            print("Invalid Choice...!!!")
    else:
        print("Invalid Product ID...!!!")
    js = json.dumps(data)
    fd = open("data.json", 'w')
    fd.write(js)
    fd.close()

# update_prod_data() # Uncomment This Line To Run This Function
# Note :- Ensure You Have data.json File to Fetch Data
