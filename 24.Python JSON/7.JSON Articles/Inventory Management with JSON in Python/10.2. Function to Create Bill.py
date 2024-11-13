def generate_bill(user_id, prod_id, price, time_date,
                  purchase_no, name, category,
                  quantity_all, transaction_id):
    print("================================\
================= Bill ================\
=================================")
    print("########################################")
    print(" User ID :-", user_id)
    print("############################################")
    amount = 0
    n = len(purchase_no)

    for i in range(n):
        print("--------------------------------------")
        amount = amount + float(price[i]) * float(quantity_all[i])
        print("Purchase number", purchase_no[i],
              "\nPurchase Time :-", time_date[i],
              "\nProduct ID :-", prod_id[i],
              "\nName Of Product :-",
              name[i], "\nCategory Of Product :-", category[i],
              "\nPrice of Product per Item :-", price[i],
              "\nPurchase Quantity :-", quantity_all[i])
        print("-------------------------------------------------")
    print("*********************************************************")
    print("	 Total Payable Bill :-",
          amount, "Transaction ID :-", transaction_id)
    print("*************************************")
