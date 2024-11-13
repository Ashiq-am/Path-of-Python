def display_specific_data():
    import pandas as pd
    import json
    fd = open("data.json", 'r')
    txt = fd.read()
    data = json.loads(txt)
    fd.close()
    print("Enter Product ID Whoes Details You Want to Have a Look on :- ")
    i = input()

    # Follwing Code will Filter out Product ID from Records
    if i in data.keys():
        temp = pd.DataFrame(columns=['ID'])
        temp['ID'] = [i]

        for j in data[i].keys():
            temp[j] = [data[i][j]]

        from IPython.display import display
        display(temp)
    else:
        print("You Have Entered Wrong Product ID \
		that is not Present in DataBase...!!!")

# display_specific_data() # Uncomment This Line To Run This Function
# Note :- Ensure You Have data.json File to Fetch Data
