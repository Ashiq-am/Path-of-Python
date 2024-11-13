def display_data():
    import pandas as pd
    import json
    fd = open("data.json", 'r')  # Open file in read mode
    txt = fd.read()  # reading data from file
    data = json.loads(txt)

    # This will parse the JSON data,
    # populates a Python dictionary with the data
    fd.close()
    print("Enter '0' To Display Data Category Wise or '1' \
	To Show Data As its Sequence Of Insertion :- ")
    n = int(input())

    # Display All Records
    if (n == 1):
        table = pd.DataFrame(
            columns=['ID', 'name', 'price', 'category',
                     'quantity', 'date'])

        # Creating Pandas dataframe to show data in table
        # format later
        for i in data.keys():
            '''Fetch all keys in dictionary'''
            temp = pd.DataFrame(columns=['ID'])
            temp['ID'] = [i]

            for j in data[i].keys():
                temp[j] = [data[i][j]]
            table = table.append(temp)
        table = table.reset_index(drop=True)

        # This will reset index of dataframe
        from IPython.display import display
        display(table)
    elif (n == 0):

        # Display Records by Category
        table = pd.DataFrame(
            columns=['ID', 'name', 'price', 'category',
                     'quantity', 'date'])
        cat = []

        for i in data.keys():
            temp = pd.DataFrame(columns=['ID'])
            temp['ID'] = [i]
            for j in data[i].keys():
                temp[j] = [data[i][j]]
                if (j == 'category'):
                    cat.append(data[i][j])
            table = table.append(temp)
            table = table.reset_index(drop=True)
            cat = set(cat)
            cat = list(cat)

        for k in cat:
            temp = pd.DataFrame()
            temp = table[table['category'] == k]
            print("Data Of Products Of Category " + k + " is:- ")
            from IPython.display import display
            display(temp)
    else:
        print("Enter Valid Choice...!!!")

# display_data() # Uncomment This Line To Run This Function
# Note :- Ensure You Have data.json File to Fetch Data
