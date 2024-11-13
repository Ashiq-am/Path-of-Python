def delete_prod():
    import json
    fd = open("data.json", 'r')
    txt = fd.read()
    data = json.loads(txt)
    fd.close()
    print("Enter The Product ID of The Product Which You Want To Delete :- ")
    temp = input()

    if temp in data.keys():

        # here we are removing that particular data
        data.pop(temp)
        print("Product ID " + str(temp) + " Deleted Successfully...!!!")
    else:
        print("Invalid Product ID...!!!")
    js = json.dumps(data)
    fd = open("data.json", 'w')
    fd.write(js)
    fd.close()

# delete_prod() # Uncomment This Line To Run This Function
# Note :- Ensure You Have data.json File to Fetch Data
