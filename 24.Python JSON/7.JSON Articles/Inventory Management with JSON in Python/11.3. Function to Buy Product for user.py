def buy_product():
    import time
    import random
    import os.path

    if (os.path.isfile("user_data.json") is False):
        user_data = {}
    else:
        fd = open("user_data.json", 'r')
        txt = fd.read()
        user_data = json.loads(txt)
        fd.close()

    fd = open("data.json", 'r')
    txt = fd.read()
    data = json.loads(txt)
    fd.close()
    print("Enter Your User ID if You are Old Customer\
	else press '0' To New User ID :- ")
    p = int(input())

    if (p == 0):
        if (len(user_data.keys()) == 0):
            user_id = 1000
        else:
            user_id = int(list(user_data.keys())[-1]) + 1
    else:
        if str(p) in user_data.keys():
            user_id = p
        else:
            user_id = -1

    if (user_id != -1):
        user_id = str(user_id)
        price = []
        time_date = []
        purchase_no = []
        name = []
        category = []
        quantity_all = []
        prod_id = []
        transaction_id = ''.join(random.choice(
            '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10))
        print("Enter Number of Products You Want To Buy :- ")
        n = int(input())
        print("Enter Data As Follows :- ")

        if user_id not in user_data.keys():
            user_data[user_id] = {}
            g = 0
        else:
            g = int(list(user_data[user_id].keys())[-1]) + 1

        for i in range(n):
            print("Enter Product ID of Product " +
                  str(i + 1) + " that you want to buy")
            id = input()

            if id in data.keys():
                user_data[user_id][str(i + 1 + g)] = {}
                user_data[user_id][str(i + 1 + g)]['time_date'] = str(time.ctime())
                time_date.append(str(time.ctime()))
                if (float(data[id]['quantity']) == 0):
                    print("Product You Want is Currenty Out Of Stock...!!!")
                    continue

                purchase_no.append(i + 1 + g)
                name.append(data[id]['name'])
                user_data[user_id][str(i + 1 + g)]['name'] = data[id]['name']
                prod_id.append(id)
                user_data[user_id][str(i + 1 + g)]['product_id'] = id
                category.append(data[id]['category'])
                user_data[user_id][str(
                    i + 1 + g)]['category'] = data[id]['category']
                print("For Product " + str(data[id]['name']) +
                      " Available Quantity is :- " + str(data[id]['quantity']))
                print("Enter Quantity of Product " +
                      str(i + 1) + " that you want to buy")
                quantity = input()

                if (float(quantity) <= float(data[id]['quantity'])):
                    data[id]['quantity'] = str(
                        float(data[id]['quantity']) - float(quantity))
                    quantity_all.append(quantity)
                    user_data[user_id][str(i + 1 + g)]['quantity'] = str(quantity)
                    price.append(data[id]['price'])
                    user_data[user_id][str(i + 1 + g)]['price'] = data[id]['price']
                    user_data[user_id][str(
                        i + 1 + g)]['Transaction ID'] = str(transaction_id)
                else:
                    print(
                        "The Quantity You Have Asked is Quite High\
                        Than That is Avaiable in Stock")
                    print(
                        "Did you Want To buy According to The Quantity\
                        Available in Stock then Enter '0' Else '1'\
                        to skip This Product")
                    key = int(input())

                    if (key == 0):
                        print("Enter Quantity of Product " +
                              str(i + 1) + " that you want to buy")
                        quantity = intput()
                        if (float(quantity) <= float(data[id]['quantity'])):
                            data[id]['quantity'] = str(
                                float(data[id]['quantity']) - float(quantity))
                            quantity_all.append(quantity)
                            user_data[user_id][str(
                                i + 1)]['quantity'] = str(quantity)
                            price.append(data[id]['price'])
                            user_data[user_id][str(
                                i + 1)]['price'] = data[id]['price']
                            user_data[user_id][str(
                                i + 1 + g)]['Transaction ID'] = str(transaction_id)
                        else:
                            print("Invalid Operation Got Repeated...!!!")
                    elif (key == 1):
                        continue
                    else:
                        print("Invalid Choice...!!!")
            else:
                print("Invalid Product ID...!!!")
        if (len(purchase_no) != 0):
            generate_bill(user_id, prod_id, price, time_date, purchase_no,
                          name, category, quantity_all, transaction_id)
    else:
        print("User ID Doesn't Exists...!!!")
    js = json.dumps(data)
    fd = open("data.json", 'w')
    fd.write(js)
    fd.close()
    js = json.dumps(user_data)
    fd = open("user_data.json", 'w')
    fd.write(js)
    fd.close()
